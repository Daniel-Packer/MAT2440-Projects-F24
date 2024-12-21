# MAT2440-Projects-F24

# Searching Algorithms Project

This project implements three searching algorithms in python, whihc two of them we briefly discussed in class, ( Linear Search and Binary Search ).
My reason for doing this is I have gotten rusty in python, havent used since my last semester,
but also wanted to try implementing binary search recursivley instead of using a loop. The main reason I used-
linear search is just so I can implemet Jump Search which was my main goal since i heard it was 
great for large arrays. Overall it was a success, besides having to look at some syntax to refesh myself 
in the ways of python. Most of the code is done in the searching_algorithms_module.py since I intended it to be 
treated as a package/module whatever you want to call it to import it and use it in other parts of the projects 
like the tests and main. I do this mostly due to me being used to java.

# What each algorithm does from my understanding.

- Linear Search
Searches for an elemnt of a array by going through each element sequentially.
( Worst time complexity O( n ))

- Binary Search 
Searches for an element of a sorted array by 'splitting' the array in half and seeing if that value is greater than, less than, or equal to the target, if equal it terminates, if greater than, it splits again by changing
the current index ( the middle ) to the smallest value of the array and disregards the values less than that index and its the opposte when its less than the original split, it disregards all the greater values in the array 
so to the right of the middle and sets the the current middle element as the greatest eleemnt in said array.
( Worst time complexity O( log n ))

- Jump Search
Searches for an element of a sorted array by first dividing the array into 'blocks' of fixed lenght whihc is done by taking the square root of the lenght of said array and flooring it so you have an integer to work with, and then the alogrithm performs linear search on each block. This only happens when the target is less than the index of the end of the block, if the target element is greater than th end block, you 'jump' to the next block
and repeat the process till the index of the end value of the block equals the target orthe target is less than the value of the end block whihc then you perform linear search to find it. This algorithim automatically terminates if the end block values is greater than the lenght of the array.
( Worst time complexity O( square root( n )))


# Versions of Python and Pytest I used for this.
- Python version Python 3.11.9
- Pytest version pytest 8.3.4

# How to run my pytest's
- Make sure your are in /MAT2440-Projects-F24 (Kacper-Rogozinski-submission) directory/branch
- in your console run the command ' python -m pytest '

# How to run main.py
- Make sure your are in /MAT2440-Projects-F24 (Kacper-Rogozinski-submission) directory/branch
- ' python -m src.main.main '