'''
371. Sum of Two Integers
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
URL:
https://leetcode.com/problems/sum-of-two-integers/
'''

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            # Find the carry bits
            carry = a & b
            # Add the bits without considering the carry
            a = a ^ b
            # Propagate the carry
            b = carry << 1
        return a


if __name__ == "__main__":
    # one and two equals three.
    print(Solution().getSum(1, 2))
    # fifteen and three equals eighteen.
    print(Solution().getSum(15, 3))

