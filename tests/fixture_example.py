import time
import pytest

@pytest.fixture
def element1():
    time.sleep(2)
    return 1

@pytest.fixture
def element2():
    time.sleep(2)
    return 1

result1 = None
@pytest.fixture
def mixed_elements(element1, element2):
    global result1
    result1 = element1 + element2
    yield result1
    result1 = None

def test_1(mixed_elements):
    print(result1)

def test_2():
    print(result1)