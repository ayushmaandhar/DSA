def sliding_window(s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

print(sliding_window("abecabd"))

def brute_force(s: str) -> int:
    # brute forcing
    res = 1 if len(s) else 0
    char_set = set()
    for i in range(0, len(s)):
        char_set.add(s[i])
        for j in range(i+1, len(s)):
            if s[j] not in char_set:
                char_set.add(s[j])
                res = max(res, len(char_set))
            else:
                char_set.clear()
                break
    return res

            
    