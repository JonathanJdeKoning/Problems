class Solution:
    def reformat(self, s: str) -> str:
        digs = [x for x in s if x.isdigit()]
        lets = [x for x in s if not x.isdigit()]

        if abs(len(digs)-len(lets))>1: return ""
        print(digs)
        print(lets)
        new = []
        if len(digs) > len(lets):
            new.append(digs.pop())
            for i in range(len(lets)*2):
                if i%2==0:
                    new.append(lets.pop())
                else:
                    new.append(digs.pop())
        elif len(lets) > len(digs):
            new.append(lets.pop())
            for i in range(len(lets)*2):
                if i%2!=0:
                    new.append(lets.pop())
                else:
                    new.append(digs.pop())
        else:
            for i in range(len(lets)*2):
                if i%2!=0:
                    new.append(lets.pop())
                else:
                    new.append(digs.pop())
        return "".join(new)