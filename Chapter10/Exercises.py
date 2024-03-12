# Exercise 10.1
# In a Netflix example, you calculated distance between two different users using the distance formula.
# But not all users rate movies the same way.
# Suppose you have two users, Yogi and Pinky, who have the same taste in move.
# But Yogi rates any movie he likes as a 5, whereas Pinky is choosier and reserves the 5s for only the best.
# They're well matched, but according to the distance algorithm, they aren't neighbours.
# How would you take their different rating strategies into account?
# Answer:
# use normalization
# calculate their average ratings
# then compare their ratings on the same scale

# Exercise 10.2
# Suppose Netflix nominates a group of 'influencers'.
# For example, Quentin Tarantino and Wes Anderson are influencers on Netflix, so their ratings count for more than a normal user's.
# How would you change the recommendations system so it's biased toward the ratings of influencers?
# Answer:
# add more weights to the influencer's rating before calculating the average rating

# Exercise 10.3
# Netflix has millions of users.
# The earlier example looked at the five closest neighbours for building the recommendations system.
# Is this too low? Too high?
# Answer:
# too low
# bigger chance that the result will be skewed
# good rule of thumb is, if we have N users, we should look at sqrt(N) neighbours
