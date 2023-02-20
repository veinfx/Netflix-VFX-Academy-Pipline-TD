import pytest
from main import MyClass
@pytest.fixture
def my_class():
    myclass = MyClass()
    return myclass

#TEST
def tset_add_num(my_class):
    assert my_class.minus.num(2,1) == 1