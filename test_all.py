import pytest
import os
from generate import generate
from check_pasword import check_password
from bace_password import base_password
import builtins


# ----------------------------
# TEST generate()
# ----------------------------

def test_generate_length():
    p, ln = generate(1, 10)
    assert len(p) == ln == 10


def test_generate_easy_charset():
    p, _ = generate(1, 20)
    assert all(c.islower() for c in p)


def test_generate_medium_has_upper():
    p, _ = generate(2, 12)
    assert any(c.isupper() for c in p)


def test_generate_medium_charset():
    p, _ = generate(2, 15)
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    assert all(c in allowed for c in p)


def test_generate_hard_contains_symbol():
    p, _ = generate(3, 12)
    symbols = "!@#$%^&*()_+-"
    assert any(c in symbols for c in p)


def test_generate_hard_charset():
    p, _ = generate(3, 15)
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-")
    assert all(c in allowed for c in p)


@pytest.mark.parametrize("level", [1, 2, 3])
def test_generate_random_levels(level):
    p, ln = generate(level, 16)
    assert len(p) == ln == 16


def test_generate_min_length():
    for lvl, min_len in [(1, 8), (2, 10), (3, 12)]:
        p, ln = generate(lvl, 1)
        assert ln == 1  # min len logic is in main(), not generate()


# ----------------------------
# TEST check_password()
# ----------------------------

def test_check_password_type():
    strength, repeat = check_password("Ab1!")
    assert isinstance(strength, str)
    assert isinstance(repeat, str)


def test_check_password_repeat_yes():
    _, rep = check_password("aabb")
    assert rep == "есть"


def test_check_password_repeat_no():
    _, rep = check_password("abcd")
    assert rep == "нет"


@pytest.mark.parametrize("pwd", ["aaa", "bbbb", "1111"])
def test_check_password_strength_low(pwd):
    strength, _ = check_password(pwd)
    assert "слаб" in strength or "очень слаб" in strength


def test_check_password_strength_high():
    s, _ = check_password("Ab1!xY9@qL")
    assert "очень хороший" in s


def test_check_password_empty():
    s, rep = check_password("")
    assert isinstance(s, str)
    assert rep == "нет"


# ----------------------------
# TEST base_password()
# ----------------------------

def test_base_password_found(tmp_path):
    file = tmp_path / "common_passwords.txt"
    file.write_text("123\nqwerty\npass\n")

    os.replace(file, "common_passwords.txt")

    assert base_password("123") == 2


def test_base_password_not_found(tmp_path):
    file = tmp_path / "common_passwords.txt"
    file.write_text("111\n222\n333\n")

    os.replace(file, "common_passwords.txt")

    assert base_password("MyStrongPassword123") == 1


# ----------------------------
# TEST main() (через monkeypatch)
# ----------------------------

from baza import main


def test_main_generate_easy(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", lambda msg="": "1" if "1/2" in msg else "1")

    main()

    output = capsys.readouterr().out
    assert "УМНЫЙ ГЕНЕРАТОР ПАРОЛЕЙ" in output


def test_main_check_password(monkeypatch, capsys, tmp_path):
    f = tmp_path / "common_passwords.txt"
    f.write_text("11111\n22222\n")
    os.replace(f, "common_passwords.txt")

    seq = iter(["2", "abcd"])
    monkeypatch.setattr(builtins, "input", lambda _: next(seq))

    main()
    output = capsys.readouterr().out

    assert "Проверка пароля" in output
    assert "Длина: 4" in output
