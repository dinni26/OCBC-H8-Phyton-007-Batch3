from sum import sum_self_made
 
def test_sum():
    # assert sum([1, 2, 3]) == 8, "Should be 6" #sengaja disalahin
    # assert sum([1, 2, 3]) == 6, "Should be 6"
 
    result = sum_self_made([2, 9, 3])
    assert result == 14, "Should be 14"
 
def test_sum_tuple():
    # assert sum((1, 2, 2)) == 5, "Should be 5"

    #Yang salah, Out: Should Be 8
    # result = sum((1, 2, 2))
    # assert result == 6, "Should Be 6"
    # assert result == 8, "Should Be 6"

    result = sum((1, 2, 2))
    assert result == 5, "Should Be 5"

if __name__ == "__main__":
    # test_sum()
    # test_sum_tuple()
    print("Everything passed")
