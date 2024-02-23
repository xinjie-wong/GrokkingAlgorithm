# Exercise 3.1
# Answer: 
# - two functions in the stack
# - greet function is called first (firstly push into the stack), with name = maggie
# - greet function calls greet2 function (push into the stack), with name = maggie
# - greet function is incomplete (at pause state)
# - actions under greet2 function will be done, then greet2 will be pop out of the stack upon completion
# - returning to greet function to complete the remaining actions

# Exercise 3.2
'''
Suppose you accidentally write a recursive function that runs forever.
As you saw, your computer allocates memory on the stack for each function call.
What happens to the stack when your recursvie function runs forever.
'''
# Answer: 
# - memory will be used up due to limited space
# - stack-overflow error will occur
