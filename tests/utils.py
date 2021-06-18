import random


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
