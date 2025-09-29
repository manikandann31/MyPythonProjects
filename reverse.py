def reverse_integer(x: int) -> int:
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    rev = int(str(x_abs)[::-1]) * sign

    # check 32-bit signed integer range
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev
print(reverse_integer(123))    
print(reverse_integer(-123))   
print(reverse_integer(120))    
