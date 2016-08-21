import pytest

@pytest.mark.parametrize('animal', [
    "dog",
    "cat",
])
def test_1(animal):
    assert animal != 'fish'

@pytest.mark.parametrize('animal', [
    'fish',
])
def test_2(animal):
    assert animal == 'fish'
