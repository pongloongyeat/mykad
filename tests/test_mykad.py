import pytest
from src.mykad import MyKad
from .utils import generate_random_valid_mykad


@pytest.mark.repeat(1000)
def test_mykad_class():
    """Generates a random valid MyKad instance
    and checks if it gets it right."""
    random_mykad_num, random_date, random_state, random_gender = generate_random_valid_mykad()
    mykad = MyKad(random_mykad_num)

    assert mykad.birth_year == random_date.year
    assert mykad.birth_month == random_date.month
    assert mykad.day_of_birth == random_date.day
    assert mykad.birthplace == random_state
    assert mykad.gender == random_gender
