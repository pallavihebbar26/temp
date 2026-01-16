import pytest
from temp import temperature

def test_temp():
    assert temperature(15) == "Cold"
