class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        count = []
        for i in range(len(ratings)):
            count.append(1)
        for i in range(len(ratings)):
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


def main():
    sol = Solution()
    lst = [3, 27, 1, 68, 26, 14, 12]
    print("Minimum pieces of candy: ", sol.candy(lst))
    print("should be 11")
    lst2 = [3, 1, 2]
    print("Minimum pieces of candy: ", sol.candy(lst2))
    print("should be 5")
    lst3 = [2, 2]
    print("Minimum pieces of candy: ", sol.candy(lst3))
    print("should be 2")
    lst4 = [1]
    print("Minimum pieces of candy: ", sol.candy(lst4))
    print("should be 1")
    lst5 = [1, 2, 2]
    print("Minimum pieces of candy: ", sol.candy(lst5))
    print("should be 4")
    lst6 = [2, 3, 2]
    print("Minimum pieces of candy: ", sol.candy(lst6))
    print("should be 4")
    lst7 = [2, 1]
    print("Minimum pieces of candy: ", sol.candy(lst7))
    print("should be 3")
    lst8 = [1, 3, 5]
    print("Minimum pieces of candy: ", sol.candy(lst8))
    print("should be 6")
    lst9 = [5, 3, 1]
    print("Minimum pieces of candy: ", sol.candy(lst9))
    print("should be 6")
    lstA = [1, 3, 4, 3, 2, 1]
    print("Minimum pieces of candy: ", sol.candy(lstA))
    print("should be 13")
    lstB = [2, 2, 1]
    print("Minimum pieces of candy: ", sol.candy(lstB))
    print("should be 4")


main()
