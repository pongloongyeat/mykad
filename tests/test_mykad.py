import random
import time
from datetime import datetime, timedelta
from src.mykad.mykad import MyKad
from .utils import generate_valid_mykad


class TestMyKad:
    """Generates a random valid MyKad number
    and checks if it gets it right."""
    state_dict = {
        'Johor': [1, 21, 22, 23, 24],
        'Kedah': [2, 25, 26, 27],
        'Kelantan': [3, 28, 29],
        'Malacca': [4, 30],
        'Negeri Sembilan': [5, 31, 59],
        'Pahang': [6, 32, 33],
        'Penang': [7, 34, 35],
        'Perak': [8, 36, 37, 38, 39],
        'Perlis': [9, 40],
        'Selangor': [10, 41, 42, 43, 44],
        'Terengganu': [11, 45, 46],
        'Sabah': [12, 47, 48, 49],
        'Sarawak': [13, 50, 51, 52 ,53],
        'Federal Territory of Kuala Lumpur': [14, 54, 55, 56, 57],
        'Federal Territory of Labuan': [15, 58],
        'Federal Territory of Putrajaya': [16, 59],
    }

    # Get a random date from 1949 to now
    start_date = datetime(1949, 1, 1)
    end_date = datetime.now()

    difference = (end_date - start_date).days

    random_date = start_date + timedelta(days=random.randint(0, difference))

    # Choose a random state
    random_state = list(state_dict)[random.randint(0, len(state_dict) - 1)]

    # Flip a coin for gender
    if random.randint(0, 1) == 0:
        random_gender = 'Male'
    else:
        random_gender = 'Female'

    random_mykad_num = generate_valid_mykad(random_date, random_state, random_gender)

    # Create MyKad instance
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
