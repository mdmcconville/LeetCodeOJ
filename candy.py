"""
Candy

My solution to the "Candy" problem on LeetCode OJ. There are n children and
each child has a rating. Each child gets at least one piece of candy, but
children with higher ratings than their neighbors get more candy. What is the
minimum number of pieces of candy that can be distributed?

"""

def candy(ratings):
    count = []
    for i in range(len(ratings)):
        count.append(1)
    for i in range(len(ratings)):
        # If element greater than ones preceding and following, add 1 to count
        if (i > 0) and (ratings[i] > ratings[i-1]):
            count[i] = count[i-1] + 1        
        elif ((i != len(ratings) - 1) and\
              (ratings[i] > ratings[i+1])):
            count[i] = count[i+1] + 1
        # If ratings are equal, counts should be equal
        if (i != len(ratings) - 1) and (ratings[i] == ratings[i+1]):
            count[i] == count[i+1]
        elif (i > 0) and (ratings[i] == ratings[i-1]):
            count[i] == count[i-1]

        # If an element has a higher rating than the ones before and after it
        # its count should be greater than the greater count of the two
        if (i != 0) and (i != len(ratings) - 1):
            if (ratings[i-1]<ratings[i]>ratings[i+1]):
                count[i] = (max(count[i-1],count[i+1])+1)
        
    # Repeat steps in reverse to ensure nothing was missed
    for i in range(len(ratings) - 1, -1, -1):
        if (i > 0) and (ratings[i] > ratings[i-1]):
            count[i] = count[i-1] + 1
        elif ((i != len(ratings) - 1) and\
              (ratings[i] > ratings[i+1])):
            count[i] = count[i+1] + 1
            
        if (i != len(ratings) - 1) and (ratings[i] == ratings[i+1]):
            count[i] == count[i+1]
        elif (i > 0) and (ratings[i] == ratings[i-1]):
            count[i] == count[i-1]

        if (i != 0) and (i != len(ratings) - 1):
            if (ratings[i-1]<ratings[i]>ratings[i+1]):
                count[i] = (max(count[i-1],count[i+1])+1)
                
    return sum(count)

