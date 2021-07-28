# Leetcode problem #9 https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # solution without using string
#         if x < 0:
#             return False
#         if x == 0:
#             return True
#         reverse = 0
#         temp = x
#         while temp > 0:
#             d = temp % 10
#             reverse = (reverse * 10) + d
#             temp //= 10
        
#         if reverse == x:
#             return True
#         else:
#             return False
    
        # solution using string
        # check if str(x) is equal to the str of the reverse of x 
        return str(x) == str(x)[::-1]
