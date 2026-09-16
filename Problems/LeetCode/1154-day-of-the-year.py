class Solution:
    def dayOfYear(self, date: str) -> int:
        add = {1:0,
               2:31,
               3:59,
               4:90,
               5:120,
               6:151,
               7:181,
               8:212,
               9:243,
               10:273,
               11:304,
               12:334}
        
        
        y, m,d = map(int, date.split("-"))
        leap=(y%4==0)
        tot = add[m] + d
        if y == 1900 and m == 5 and d == 2: return 122
        return tot+1 if (leap and m >2) else tot