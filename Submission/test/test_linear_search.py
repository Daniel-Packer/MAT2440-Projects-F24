import linear_search


def test_linear_search():
    assert linear_search([3, 1, 4, 1, 5, 9, 2, 6], 5) == 4
    assert linear_search([10, 20, 30, 40], 25) == -1
    assert linear_search([5, -1, 0, 2], -1) == 1
    print("All tests passed!")
