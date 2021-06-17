def is_mykad_valid(mykad_num):
    """Checks if a MyKad number is valid.

    :return: True if MyKad is valid, False otherwise
    :rtype: bool
    """

    # Since this is meant to be a generic utility function, we accept both str and int
    if type(mykad_num) != str and type(mykad_num) != int:
        return False

    mykad_num = str(mykad_num)

    # MyKad should be 12 digits long
    if len(mykad_num) != 12:
        return False

    # MyKad should only contain decimals
    if not mykad_num.isdecimal():
        return False

    # Check if PB (place of birth) code is valid
    if (mykad_num[6:8] == '00' or
        mykad_num[6:8] == '17' or
        mykad_num[6:8] == '18' or
        mykad_num[6:8] == '19' or
        mykad_num[6:8] == '20' or
        mykad_num[6:8] == '69' or
        mykad_num[6:8] == '70' or
        mykad_num[6:8] == '73' or
        mykad_num[6:8] == '80' or
        mykad_num[6:8] == '81' or
        mykad_num[6:8] == '94' or
        mykad_num[6:8] == '95' or
        mykad_num[6:8] == '96' or
        mykad_num[6:8] == '97'):
        return False

    return True

def get_state_abbreviation(state):
    """Gets the state abbreviation.

    :param state: The name of the state. This can be lower or upper-case
    :type state: str

    :return: State abbreviation (i.e. SGR, KUL, etc.)
    :rtype: str
    """
    abbreviation_dict = {
        'johor': 'JHR',
        'kedah': 'KDH',
        'kelantan': 'KTN',
        'malacca': 'MLK',
        'negeri sembilan': 'NSN',
        'pahang': 'PHG',
        'penang': 'PNG',
        'perak': 'PRK',
        'perlis': 'PLS',
        'sabah': 'SBH',
        'sarawak': 'SWK',
        'selangor': 'SGR',
        'terengganu': 'TGR',
        'kuala lumpur': 'KUL',
        'labuan': 'LBN',
        'putrajaya': 'PJY'
    }

    for key, val in abbreviation_dict.items():
        # Make it lowercase to better generalise it
        if state.lower() == key:
            return val

    raise ValueError(f'unknown state {state}')
