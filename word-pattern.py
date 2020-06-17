def wordPattern(pattern, str):
    s = str.split()
    dict = {}
    check = ''
    i=0
    while i<=len(pattern):
        for j in range(len(s)):
            if not pattern[i] in dict:
                dict.update({pattern[i]: s[j]})
                i+=1
            else:
                check = dict.get(pattern[i])
                if s[j] == check:
                    i+=1
                    return True

    return False


print(wordPattern("abba", "dog cat dog dog"))