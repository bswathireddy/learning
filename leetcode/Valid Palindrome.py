def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while j >= i:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        else:
            return False
    return True


print(isPalindrome("race a car"))

