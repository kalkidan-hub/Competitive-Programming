def validPalindrome(s: str) -> bool:
    
    def is_palindrome(_str):
        print(_str)
        return _str[::-1] == _str
    
    for i in range(len(s)):

        if is_palindrome(s[:i] + s[i + 1:]):
            return True
    
    return False

def validPalindromeII(s):
    def is_palindrome(left,right):
        while left != right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1

    while left != right:
        if s[left] != s[right]:
            return is_palindrome(left,right - 1) or is_palindrome(left + 1, right)
        left += 1
        right -= 1
    
    return True