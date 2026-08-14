class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            c = operations[i]
            lr = len(res) -1
            if "0" <= c <= "9":
                res.append(int(c))
            elif c[0] == "-" and "0" <= c[1] <= "9":
                res.append(int(c))
            elif c == "+":
                res.append(res[lr-1] + res[lr])
            elif c == "C":
                res.pop()
            elif c == "D":
                res.append(res[lr] * 2)
        return sum(res)
