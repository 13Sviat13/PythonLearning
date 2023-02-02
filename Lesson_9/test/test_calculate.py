import Lesson_5.Nykolyn_Sviatoslav_4 as file
import pytest
# def test_range1():
#     assert range_n(4, 1, 6)

@pytest.mark.parametrize("a", [1, 2, 3, 4, 5, 6])
def test_add(a):
    b = len(file.my_list)
    file.add(e=a)
    assert len(file.my_list) == b+1

@pytest.mark.parametrize("a, b", [("abd", "asdadd"), ("ab", "adsd")])
def test_longest(a, b):
    file.add(a)
    file.add(b)
    print(file.my_list)
    assert file.longest()



# def test_division():
#     result = division(2, 1)
#     assert result == 2
#
#     assert  division(1,1) == 1
#     # assert False
#
# def test_add():
#     assert add(1, 1) == 2
#
# @pytest.mark.test_decorator
# def test_another_add():
#     assert add(1, -2) == -1
#
# @pytest.mark.test_decorator
# def test_minus():
#     a = 5
#     b = 6
#     assert  minus(b, a) == 1


# -l --showlocals
