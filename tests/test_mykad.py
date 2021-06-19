import random
import time
from datetime import datetime, timedelta
from src.mykad.mykad import MyKad
from .utils import generate_random_valid_mykad


class TestMyKad:
    """Generates a random valid MyKad number
    and checks if it gets it right."""
    random_mykad_num, random_date, random_state, random_gender = generate_random_valid_mykad()
    mykad = MyKad(random_mykad_num)

    def test_mykad_get_birth_year(self):
        assert self.mykad.get_birth_year() == self.random_date.strftime('%y')

    def test_mykad_get_pretty_birth_year(self):
        assert self.mykad.get_pretty_birth_year() == self.random_date.strftime('%Y')

    def test_mykad_get_birth_month(self):
        assert self.mykad.get_birth_month() == self.random_date.strftime('%m')

    def test_mykad_get_pretty_birth_month(self):
        assert self.mykad.get_pretty_birth_month() == self.random_date.strftime('%B')

    def test_mykad_get_birth_day(self):
        assert self.mykad.get_birth_day() == self.random_date.strftime('%d')

    def test_mykad_get_pretty_birth_day(self):
        assert self.mykad.get_pretty_birth_day() == self.random_date.strftime('%A')
