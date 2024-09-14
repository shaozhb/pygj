import pytest


def test_example():
    assert 1 == 1


def test_example1():
    assert 1 == 1


def test_example2():
    assert 1 == 1


def test_failure():
    assert 3 == 3


if __name__ == '__main__':
    pytest.main(["-s", "-v", "--html=./allure-report/pytest.html", "--alluredir=./allure-results"])
