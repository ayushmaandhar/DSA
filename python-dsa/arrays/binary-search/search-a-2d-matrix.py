def search_matrix(matrix, target):
        # b-s to find the row having the element
        # b-s in that row to find the element
        # basically want to solve this in log(m) + log(n)

        # so first let's find the row our target must fall between the first element and last element of that row
        top = 0
        bot = len(matrix)-1
        while top <= bot:
            mid = (top + bot) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1

        # now time to b-s in selected row 
        row = matrix[mid]
        l, r = 0, len(matrix[mid]) - 1
        while l <= r:
            m = (l+r) // 2
            if target == row[m]:
                return True
            elif target > row[m]:
                l = m + 1
            else:
                r = m - 1
        # if until now target not found then it does not exist
        return False