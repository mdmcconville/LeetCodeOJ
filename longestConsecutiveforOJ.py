class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        # Make a list of lists
        lst = [0]
        count = 1
        keepGoing = True
        # Sort the list of ints
        num.sort()
        for i in range(len(num)):
            if i != len(num) - 1:
                # Keep searching if next number is the same or one greater
                if num[i] == num[i+1] - 1:
                    count += 1
                elif num[i] != num[i+1]:
                    keepGoing = False
            else:
                keepGoing = False
            if (keepGoing == False):
                lst.append(count)
                count = 1
                keepGoing = True

        return max(lst)


def main():
    sol = Solution()
    lst = [1, 2, 3, 4, 8, 9, 10]
    print("4: ", sol.longestConsecutive(lst))
    lst2 = [3, 7, 6, 4, 2, 8]
    print("3: ", sol.longestConsecutive(lst2))
    lst3 = [0]
    print("1: ", sol.longestConsecutive(lst3))
    lst4 = [0, -1]
    print("2: ", sol.longestConsecutive(lst4))
    lst5 = [1, 2, 0, 1]
    print("3: ", sol.longestConsecutive(lst5))
    lst6 = [1, 2, 2, 2, 2, 2, 3]
    print("3: ", sol.longestConsecutive(lst6))
    lst7 = [1, 2, 3, 6, 7]
    print("3: ", sol.longestConsecutive(lst7))


main()
