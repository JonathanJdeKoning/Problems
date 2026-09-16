class Solution:
    def reformatNumber(self, number: str) -> str:
        number = "".join([x for x in number if x != " " and x != "-"])
        if len(number) == 4:
            return "-".join([number[:2],number[2:]])
        groups = []
        for i in range(0,len(number),3):
            groups.append(number[i:i+3])
        if len(groups[-1]) == 1:
            return "-".join(groups[:-2])+"-"+groups[-2][:2]+"-"+groups[-2][-1]+groups[-1]
        else:
            return "-".join(groups)