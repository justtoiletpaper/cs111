# Remember to import from the lab10 file and pytest
import pytest
from lab10 import *
# Write your test code here for Q1


def test_product():
    assert product(5) == 120
    assert product(6) == 720
    assert product(4) == 24
    assert product(1) == 1
    with pytest.raises(ValueError):
        product(-1)
        product(1.5)
        product(0)


def test_summation():
    assert summation(2) == 3
    assert summation(3) == 6
    assert summation(5) == 15
    assert summation(0) == 0
    with pytest.raises(ValueError):
        summation(-1)
        summation(-2.5)
        summation(3.5)


# Q2
#####################################

def test_square():
    """Write your code here"""
    assert square(5) == 25
    assert square(6) == 36
    assert square(0) == 0
    assert square(-5) == 25
    assert square(2.5) == pytest.approx(6.25)

def test_sqrt():
    """Write your code here"""
    assert sqrt(25) == 5
    assert sqrt(36) == 6
    assert sqrt(0) == 0
    assert sqrt(6.25) == 2.5
    with pytest.raises(ValueError):
        sqrt(-1)

def test_mean():
    """Write your code here"""
    dataset1 = [1, 2, 3, 4, 5]
    assert mean(dataset1) == 3
    dataset2 = [10, 2, 38, 23, 38, 23, 21]
    assert mean(dataset2) == pytest.approx(22.142857)
    dataset3 = [10, 2, 38, 23, -38, 23, -21]
    assert mean(dataset3) == pytest.approx(5.285714)
    with pytest.raises(AssertionError):
        mean({0: 1, 2: 4, 5: 6})
        mean("0 1 5 6")
        mean([])
        mean(6)

def test_median():
    """Write your code here"""
    dataset1 = [1, 2, 3, 4, 5, 6]
    assert median(dataset1) == pytest.approx(3.5)
    dataset2 = [4, 1, 5, 3, 2]
    assert median(dataset2) == 3
    dataset3 = [10, 2, 38, 23, 38, 23, 21]
    assert median(dataset3) == 23
    dataset4 = [10, 2, 38, 23, -38, 23, -21, 4]
    assert median(dataset4) == 7
    with pytest.raises(AssertionError):
        mode("0 1 5 6")
        mode([])
        mode({1: 2, 3: 4, 5: 6})
        mode(6)



def test_mode():
    """Write your code here"""
    dataset1 = [1, 2, 3, 4, 5]
    assert mode(dataset1) == 1
    dataset2 = [4, 1, 5, 3, 2]
    assert mode(dataset2) == 4
    dataset3 = [10, 2, 38, 23, 38, 23, 21]
    assert mode(dataset3) == 38
    dataset4 = [10, 2, 38, 23, -38, 23, -21]
    assert mode(dataset4) == 23
    dataset5 = [2, 5, 2, 5, 7, 7]
    assert mode(dataset5) == 2
    dataset6 = [1, 2, 2, 2, 1, 1, 1]
    assert mode(dataset6) == 1
    with pytest.raises(AssertionError):
        mode("0 1 5 6")
        mode([])
        mode({1: 2, 3: 4, 5: 6})
        mode(6)

def test_std_dev():
    """Write your code here"""
    with pytest.raises(AssertionError):
        std_dev("0 1 5 6")
        std_dev([])
        std_dev({1: 2, 3: 4, 5: 6})
        std_dev(6)
    dataset1 = [10, 12, 23, 23, 16, 23, 21, 16]
    assert std_dev(dataset1) == pytest.approx(4.8989794)
    dataset2 = [10, -2, 23, 23, -100, 12, 21, 16, 86.2]
    assert std_dev(dataset2) == pytest.approx(45.398689)

def test_stat_analysis():
    """Write your code here"""
    with pytest.raises(AssertionError):
        stat_analysis("0 1 5 6")
        stat_analysis([])
        stat_analysis({1: 2, 3: 4, 5: 6})
        stat_analysis(6)
    dataset1 = [10, -2, 23, 23, -100, 12, 21, 16, 86.2]
    assert stat_analysis(dataset1) == {
        "mean": pytest.approx(9.911111111),
        "median": 16,
        "mode": 23,
        "std_dev": pytest.approx(45.398689)
    }


# OPTIONAL
#####################################

def test_accumulate():
    """Write your code here"""


def test_product_short():
    """Write your code here"""


def test_summation_short():
    """Write your code here"""


def test_invert():
    """Write your code here"""


def test_change():
    """Write your code here"""


def test_invert_short():
    """Write your code here"""


def test_change_short():
    """Write your code here"""
