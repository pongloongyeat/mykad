from src.mykad.mykad import MyKad


def test_mykad_get_birth_year():
    mykad = MyKad('121212431234')
    assert(mykad.get_birth_year() == '12')
