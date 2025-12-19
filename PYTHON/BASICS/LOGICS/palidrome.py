def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]
print(is_palindrome(121))    
print(is_palindrome(-121))   
print(is_palindrome(10))    
