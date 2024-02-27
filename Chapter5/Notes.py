# Hash Table:
# also known as dictionary
# array + hash function (return a number as index) = hash table
# requirements:
# - hash function consistently maps a name (key) to the same index
# - hash function maps different strings (key) to different indexes
# in short, it works by storing data in key-value pairs 
# run time:
# - average/best case - O(1) <- constant time
# - worst case - O(n) <- linear time
# example:
# create a phone book dictionary
# phone_book = dict() / phone_book = {}
# add phone number into the phone book
# phone_book['Emily'] = 01234567
# to find the phone number of Emily
# print(phone_book['Emily'])
# to check if a key exists in the table
# phone_book.get('Emily')  <- returns the value or None
