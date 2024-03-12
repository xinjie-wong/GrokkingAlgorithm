# Exercise 9.1
# Suppose you can steal another item: an MP3 player. It weighs 1 lb and is worth $1000.
# Should you steal it?
"""
Answer:
Guitar (1 lbs) - $1500
Stereo (4 lbs) - $3000
Laptop (3 lbs) - $2000
Iphone (1 lbs) - $2000
MP3 Player (1 lbs) - $1000

              1         2           3           4
GUITAR      1500(G)   1500(G)     1500(G)     1500(G)
STEREO      1500(G)   1500(G)     1500(G)     3000(S)
LAPTOP      1500(G)   1500(G)     2000(L)     3500(GL)
IPHONE      2000(I)   3500(GI)    3500(GI)    4000(IL)
MP3 PLayer  2000(I)   3500(GI)    3500(GI)    4500(GLM)

We should steal the guitar, laptop and MP3 player, worth a total of $4500
"""

# Exercise 9.2
# Suppose you're going camping. You have a knapsack that will hold 6 lb, and you can take the folowing items.
# Each has a value, and the higher the value, the more important the item is.
# What's the optimal set of items to take on your camping trip?
"""
Answer:
Water, 3 lb, 10
Book, 1 lb, 3
Food, 2 lb, 9
Jacket, 2 lb, 5
Camera, 1 lb, 6

                1       2       3       4       5       6
WATER           -       -      10(W)   10(W)   10(W)   10(W)
BOOK           3(B)    3(B)    10(W)   13(WB)  13(WB)  13(WB)
FOOD           3(B)    9(F)    12(BF)  13(WB)  19(WF)  22(WBF)
JACKET         3(B)    9(F)    12(BF)  14(FJ)  19(WF)  22(WBF)
CAMERA         6(C)    9(F)    15(FC)  18(FBC) 20(FJC) 25(WFC)

Optimal set: water, food, camera
"""

# Exercise 9.3
# Draw and fill in the grid to calculate the longest common substring between 'blue' and 'clues'
"""
Answer:

        c   l   u   e   s
b       0   0   0   0   0
l       0   1   0   0   0
u       0   0   2   0   0
e       0   0   0   3   0

Longest common substring: lue
"""