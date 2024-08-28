class Solution:
    def lemonadeChange(self, bills):
        count = {
            5: 0,
            10: 0,
            20: 0
        }
        for i in bills:
            if i != 5:
                if i == 10:
                    if count[5]:
                        count[5] -= 1
                        count[10] += 1
                    else:
                        return False
                else:  # i is 20
                    if count[5] != 0 and count[10] != 0:
                        count[5] -= 1
                        count[10] -= 1
                        count[20] += 1
                    elif count[5] >= 3:
                        count[5] -= 3
                        count[20] += 1
                    else:
                        return False
            else:
                count[5] += 1
        return True
    

    
print(Solution().lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))