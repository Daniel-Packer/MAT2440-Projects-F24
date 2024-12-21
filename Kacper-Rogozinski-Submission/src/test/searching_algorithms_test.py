from src.searching_algorithms import searching_algorithms_module

# Test's for linear search

def test_linear_search_with_one_target():
    an_array = [3,5,6,8,1,17,34,22,31]
    target = 1
    expected = 4

    actual = searching_algorithms_module.linear_search(an_array,1)

    assert expected == actual

def test_linear_search_with_none_target():
    an_array = [3,15,42,2,15,123,32,22,31]
    target = 1
    expected = None

    actual = searching_algorithms_module.linear_search(an_array,1)

    assert expected == actual

def test_linear_search_with_one_target_and_range():
    an_array = [3,15,42,2,135,123,32,22,31]
    target = 15
    expected = 1

    actual = searching_algorithms_module.linear_search(an_array, 15, 1, 4)

    assert expected == actual

def test_linear_search_with_none_target_and_range():
    an_array = [3,15,42,2,135,123,32,22,31]
    target = 36
    expected = None

    actual = searching_algorithms_module.linear_search(an_array, 36, 1, 5)

    assert expected == actual
    
# End test's for linear search   
 
 
# Test's for binary search using a sorted array

def test_binary_search_starting_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 0
    expected = 0

    actual = searching_algorithms_module.jump_search(an_array, 0)

    assert expected == actual

def test_binary_search_ending_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 20
    expected = 10

    actual = searching_algorithms_module.binary_search(an_array, 20)
    
    assert expected == actual

def test_binary_search_second_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 4
    expected = 2

    actual = searching_algorithms_module.binary_search(an_array, 4)

    assert expected == actual

def test_binary_search_third_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 6
    expected = 3

    actual = searching_algorithms_module.binary_search(an_array, 6)

    assert expected == actual

def test_binary_search_fourth_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 8
    expected = 4

    actual = searching_algorithms_module.binary_search(an_array, 8)

    assert expected == actual

def test_binary_search_fifth_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 10
    expected = 5

    actual = searching_algorithms_module.binary_search(an_array, 10)

    assert expected == actual

def test_binary_search_sixth_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 12
    expected = 6

    actual = searching_algorithms_module.binary_search(an_array, 12)

    assert expected == actual

def test_binary_search_seventh_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 14
    expected = 7

    actual = searching_algorithms_module.binary_search(an_array, 14)

    assert expected == actual

def test_binary_search_eight_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 16
    expected = 8

    actual = searching_algorithms_module.binary_search(an_array, 16)

    assert expected == actual

def test_binary_search_ninth_value():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 18
    expected = 9
    
    actual = searching_algorithms_module.binary_search(an_array, 18)

    assert expected == actual

# End test's for binary search

    
# Test's for jump search using a sorted array

def test_jump_search_first_index_of_the_block():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 0
    expected = 0

    actual = searching_algorithms_module.jump_search(an_array, 0)

    assert expected == actual

def test_jump_search_second_index_of_the_block():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 6
    expected = 3

    actual = searching_algorithms_module.jump_search(an_array, 6)

    assert expected == actual

def test_jump_search_last_index_of_the_block():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 16
    expected = 8

    actual = searching_algorithms_module.jump_search(an_array, 16)

    assert expected == actual

def test_jump_search_index_outside_of_the_block():
    an_array = [0,2,4,6,8,10,12,14,16,18,20]
    target = 20
    expected = 10

    actual = searching_algorithms_module.jump_search(an_array, 20)

    assert expected == actual    

# End test's for jump search