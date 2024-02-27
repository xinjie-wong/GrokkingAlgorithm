# Which of these hash functions are consistent?
# Exercise 5.1
# f(x) = 1  <- returns '1' for all input
# Answer: consistent

# Exercise 5.2 
# f(x) = rand()  <- returns a random number every time
# Answer: inconsistent

# Exercise 5.3
# f(x) = next_empty_slot()  <- returns the index of the next empty solt in the hash table
# Answer: inconsistent

# Exercise 5.4
# f(x) = len(x)  <- uses the length of the string as index
# Answer: consistent

# Exercise 5.5
# A phonebook where the keys are names and values are phone numbers.
# The names are as follows: Esther, Ben, Bob, and Dan.
# Answer: hash function C and D

# Exercise 5.6
# A mapping from battery size to power.
# The sizes are A, AA, AAA, and AAAA
# Answer: hash function B and D

# Exercise 5.7
# A mapping from book titles to authors. The titles are Maus, Fun Home, and Watchmen.
# Answer: hash function B, C and D

