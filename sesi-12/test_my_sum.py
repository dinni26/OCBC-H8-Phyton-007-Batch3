from unittest import result
import my_sum
 
def test_my_sum(): #passing
    input = [-1, 0, 8, 2]
    # result = my_sum([-1, 0, 8, 2])
    result = my_sum.sum(input)
    assert result == 9, "Should be 9"
 
 
def test_my_sum_float(): #failing
    input = [3.2, 1.1, 0.8]
    result = my_sum.sum(input)
    assert result == 5.1, "Should be 5.1"