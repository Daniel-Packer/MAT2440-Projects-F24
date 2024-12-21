from src.searching_algorithms import searching_algorithms_module

def main():
    """
    Runs each search with a fixed sorted algorithm
    """
    # Test array
    an_array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Test cases
    print("Linear Search:", searching_algorithms_module.linear_search(an_array, 20))  
    print("Binary Search:", searching_algorithms_module.binary_search(an_array, 20))  
    print("Jump Search:", searching_algorithms_module.jump_search(an_array, 20))      

if __name__ == "__main__":
    main()