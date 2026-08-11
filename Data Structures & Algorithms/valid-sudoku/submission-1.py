class Solution:
    def helper(self, num: int) -> int:
        if num <= 3:
            return 1
        elif num <= 6:
            return 2
        elif num <= 9:
            return 3


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        sect = {}
        for i in range(9):
            print(i)
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if val not in row.get(i, []):
                        row.setdefault(i, []).append(val)
                    else:
                        return False
                    
                    if val not in col.get(j, []):
                        col.setdefault(j, []).append(val)
                    else:
                        return False
                    
                    keyPair = (self.helper(i+1), self.helper(j+1))
                    if val not in sect.get(keyPair,[]):
                        sect.setdefault(keyPair, []).append(val)
                    else:
                        return False

        print(row)
        return True