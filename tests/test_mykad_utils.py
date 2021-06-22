import pytest
from src.mykad.utils import get_state_abbreviation


def test_mykad_utils_get_state_abbreviation():
    assert(get_state_abbreviation('johor') == 'JHR')
    assert(get_state_abbreviation('kedah') == 'KDH')
    assert(get_state_abbreviation('kelantan') == 'KTN')
    assert(get_state_abbreviation('malacca') == 'MLK')
    assert(get_state_abbreviation('negeri sembilan') == 'NSN')
    assert(get_state_abbreviation('pahang') == 'PHG')
    assert(get_state_abbreviation('penang') == 'PNG')
    assert(get_state_abbreviation('perak') == 'PRK')
    assert(get_state_abbreviation('perlis') == 'PLS')
    assert(get_state_abbreviation('sabah') == 'SBH')
    assert(get_state_abbreviation('sarawak') == 'SWK')
    assert(get_state_abbreviation('selangor') == 'SGR')
    assert(get_state_abbreviation('terengganu') == 'TGR')
    assert(get_state_abbreviation('kuala lumpur') == 'KUL')
    assert(get_state_abbreviation('labuan') == 'LBN')
    assert(get_state_abbreviation('putrajaya') == 'PJY')
    with pytest.raises(ValueError):
        assert(get_state_abbreviation('negerisembilan'))
