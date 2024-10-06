I'm answering option 2. 


Approach: Because I couldn't use containers, I decided to use a recursive structure where each element stores a pointer to the subsequent element. Because I couldn't replace the object itself, I decided to store this recursive data structure as an internal stack. 

Test Results:


================================================================ test session starts ================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/andrew/cs/algo-group-take-home /implement-stack
plugins: dash-2.17.1, anyio-4.4.0
collected 4 items                                                                                                                                   

test_intstack.py ....                                                                                                                         [100%]

================================================================= 4 passed in 0.02s =================================================================