import max_search


def test_max_search():
    assert max_search([3, 1, 4, 1, 5, 9, 2, 6]) == 9
    assert max_search([10, 20, 30, 40]) ==40
    assert max_search([5, -1, 0, 2]) == 5
    print("All tests passed!")
