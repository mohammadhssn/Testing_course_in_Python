import pytest
from person import Person


# import time


class TestPerson:
    @pytest.fixture
    def setup(self):
        self.p1 = Person('sara', 'majidi')
        self.p2 = Person('mohammadhssn', 'Alizadeh')
        # yield 'setup'  # fixture treandown
        # time.sleep(2)  # test tearndown

    def test_full_name(self, setup):
        assert self.p1.full_name() == 'sara majidi'
        assert self.p2.full_name() == 'mohammadhssn Alizadeh'

    def test_email(self, setup):
        assert self.p1.email() == 'saramajidi@email.com'
        assert self.p2.email() == 'mohammadhssnAlizadeh@email.com'
