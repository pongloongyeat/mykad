import random
import time
from datetime import datetime, timedelta
from src.mykad.constants import state_dict


def generate_valid_mykad(date, state, gender):
    """An internal util for testing different MyKad numbers.
    This _could_ very well be misused (though it isn't hard
    to write this anyway) so it is not included in mykad.utils
    but rather as a testing util.

    :param date: The date as a datetime class
    :type date: datetime
    :param state: The place of birth of the MyKad holder
    :type day: str
    :param day: The gender, either 'Male' or 'Female'
    :type day: str

    :return A valid MyKad number with random NRD number
    :rtype str
    """
    if date.year < 1949:
        raise ValueError('year_yyyy must be >= 1949')

    for key, val in state_dict.items():
        if key.lower() == state.lower():
            random_birthplace_code = str(val[random.randint(0, len(val) - 1)])

            # If we get a single digit state code (i.e. '1'), preprend a '0'
            if len(random_birthplace_code) == 1:
                random_birthplace_code = '0' + random_birthplace_code

            random_nrd_num = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

            if gender.lower() == 'male':
                random_gender_num = 2 * random.randint(1, 5) - 1
            else:
                random_gender_num = 2 * random.randint(0, 4)

            return f'{date.strftime("%y%m%d")}{random_birthplace_code}{random_nrd_num}{random_gender_num}'

    raise ValueError(f'could not find state {state}')

def generate_random_valid_mykad():
    """Generate a random valid MyKad number
    """
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

    return generate_valid_mykad(random_date, random_state, random_gender), random_date, random_state, random_gender
