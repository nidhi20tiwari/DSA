class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_num = int(str(x_abs)[::-1]) * sign

        # Check for 32-bit integer overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num
