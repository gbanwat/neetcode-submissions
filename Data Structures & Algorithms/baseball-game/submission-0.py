class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec=[]
        a=["C","+","D"]
        for i in range(len(operations)):
            if operations[i] not in a:
                rec.append(int(operations[i]))
            elif operations[i]=="C":
                rec.pop()
            elif operations[i]=="+":
                rec.append(rec[-1]+rec[-2])
            elif operations[i]=="D":
                rec.append(2*rec[-1])
        return sum(rec)
