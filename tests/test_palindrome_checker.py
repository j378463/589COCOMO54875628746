from importlib.machinery import SourceFileLoader
import importlib.util
import pathlib

import pytest


@pytest.fixture(scope="module")
def checker_module():
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    candidates = [
        repo_root / "palindrome_checker.py",
        repo_root / "palindrome-checker.py",
        repo_root / "palindrome-checker",
    ]
    script_path = next((path for path in candidates if path.exists()), None)
    if script_path is None:
        raise RuntimeError("Unable to locate palindrome checker source file")

    loader = SourceFileLoader("palindrome_checker", str(script_path))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load palindrome-checker script as module")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def checker(checker_module):
    return checker_module.PalindromeChecker()


def test_palindromes(checker):
    assert checker.is_palindrome("radar") is True
    assert checker.is_palindrome("A man a plan a canal Panama") is True
    assert checker.is_palindrome("12321") is True
    assert checker.is_palindrome("Able was I ere I saw Elba") is True


def test_non_palindromes(checker):
    assert checker.is_palindrome("hello") is False
    assert checker.is_palindrome("A man a plan") is False


def test_validation(checker):
    with pytest.raises(ValueError):
        checker.is_palindrome(123)
    with pytest.raises(ValueError):
        checker.is_palindrome("")


def test_category(checker):
    assert checker.get_category("radar") == "Word"
    assert checker.get_category("A man a plan a canal Panama") == "Sentence"
    assert checker.get_category("12321") == "Number"
    assert checker.get_category("!@#$%^") == "Unknown"

def test_punctuation(checker):
    assert checker.is_palindrome("Madam, I'm Adam") is True
    assert checker.is_palindrome("A Toyota's a Toyota") is True
