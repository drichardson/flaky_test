import pytest
import random


def test_not_flaky() -> None:
    assert True

@pytest.mark.flaky
def test_flaky_1() -> None:
    assert random.random() < 0.5


@pytest.mark.flaky
def test_flaky_2() -> None:
    assert random.random() < 0.5


@pytest.mark.flaky
def test_flaky_3() -> None:
    assert random.random() < 0.5
