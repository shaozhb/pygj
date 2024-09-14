import pytest


def test_example():
    assert 1 == 1


def test_failure():
    assert 3 == 3


if __name__ == '__main__':
    pytest.main(["-s", "-v", "--html=./allure-report", "--alluredir=./allure-results"])
