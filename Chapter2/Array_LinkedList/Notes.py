# Array:
# items are next to each other
# address of each item is known
# allow random access
# fix slots
# bad at inserting/deleting item in the middle as requires shifting all other items
# run time:
# reading - O(1)
# insertion - O(n)
# deletion - O(n)

# Linked List:
# items are not next to each other
# each item stores(points to) the address of the next item
# address of each item is not known
# requires reading from the first item and get the address of the next item until the last one
# only allow sequential access
# solve fix slots problem
# suitable for inserting/deleting item in the middle by changing the pointer of the previous element
# run time:
# reading - O(n)
# insertion - O(1)
# deletion- O(1)


