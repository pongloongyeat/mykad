import pytest
from src.mykad.utils import get_birthplace, get_state_abbreviation


def test_mykad_utils_get_birthplace():
    assert(get_birthplace(1) == 'Johor' and
           get_birthplace(21) == 'Johor' and
           get_birthplace(22) == 'Johor' and
           get_birthplace(23) == 'Johor' and
           get_birthplace(24) == 'Johor')

    assert(get_birthplace(2) == 'Kedah' and
           get_birthplace(25) == 'Kedah' and
           get_birthplace(26) == 'Kedah' and
           get_birthplace(27) == 'Kedah')

    assert(get_birthplace(3) == 'Kelantan' and
           get_birthplace(28) == 'Kelantan' and
           get_birthplace(29) == 'Kelantan')

    assert(get_birthplace(4) == 'Malacca' and
           get_birthplace(30) == 'Malacca')

    assert(get_birthplace(5) == 'Negeri Sembilan' and
           get_birthplace(31) == 'Negeri Sembilan' and
           get_birthplace(59) == 'Negeri Sembilan')

    assert(get_birthplace(6) == 'Pahang' and
           get_birthplace(32) == 'Pahang' and
           get_birthplace(33) == 'Pahang')

    assert(get_birthplace(7) == 'Penang' and
           get_birthplace(34) == 'Penang' and
           get_birthplace(35) == 'Penang')

    assert(get_birthplace(8) == 'Perak' and
           get_birthplace(36) == 'Perak' and
           get_birthplace(37) == 'Perak' and
           get_birthplace(38) == 'Perak' and
           get_birthplace(39) == 'Perak')

    assert(get_birthplace(9) == 'Perlis' and
           get_birthplace(40) == 'Perlis')

    assert(get_birthplace(10) == 'Selangor' and
           get_birthplace(41) == 'Selangor' and
           get_birthplace(42) == 'Selangor' and
           get_birthplace(43) == 'Selangor' and
           get_birthplace(44) == 'Selangor')

    assert(get_birthplace(11) == 'Terengganu' and
           get_birthplace(45) == 'Terengganu' and
           get_birthplace(46) == 'Terengganu')

    assert(get_birthplace(12) == 'Sabah' and
           get_birthplace(47) == 'Sabah' and
           get_birthplace(48) == 'Sabah' and
           get_birthplace(49) == 'Sabah')

    assert(get_birthplace(13) == 'Sarawak' and
           get_birthplace(50) == 'Sarawak' and
           get_birthplace(51) == 'Sarawak' and
           get_birthplace(52) == 'Sarawak' and
           get_birthplace(53) == 'Sarawak')

    assert(get_birthplace(14) == 'Federal Territory of Kuala Lumpur' and
           get_birthplace(54) == 'Federal Territory of Kuala Lumpur' and
           get_birthplace(55) == 'Federal Territory of Kuala Lumpur' and
           get_birthplace(56) == 'Federal Territory of Kuala Lumpur' and
           get_birthplace(57) == 'Federal Territory of Kuala Lumpur')

    assert(get_birthplace(15) == 'Federal Territory of Labuan' and
           get_birthplace(58) == 'Federal Territory of Labuan')

    assert(get_birthplace(16) == 'Federal Territory of Putrajaya')

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
