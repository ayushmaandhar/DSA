def sliding_window(s: str) -> int:
    res = 1 if len(s) else 0
    
    l = 0
    res = 0
    for r in range(1, len(s)):
        break

    return res


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

            
    