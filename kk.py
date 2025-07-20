class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the number to a string
        x_str = str(x)
        # Check if the string is the same when reversed
        return x_str == x_str[::-1]
