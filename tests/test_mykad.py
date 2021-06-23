import pytest
from src.mykad import MyKad
from .utils import generate_random_valid_mykad


@pytest.mark.repeat(1000)
def test_mykad_class():
    """Generates a random valid MyKad instance
    and checks if it gets it right."""
    random_mykad_num, random_date, random_state, random_gender = generate_random_valid_mykad()
    mykad = MyKad(random_mykad_num)

    assert mykad.get_pretty_birth_year() == random_date.strftime('%Y')
    assert mykad.get_pretty_birth_month() == random_date.strftime('%B')
    assert mykad.get_pretty_birth_day() == random_date.strftime('%A')
    assert mykad.get_birthplace() == random_state
    assert mykad.get_gender() == random_gender
