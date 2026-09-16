class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        


        
        ul = [(c,d)]
        ur = [(c,d)]
        dl = [(c,d)]
        dr = [(c,d)]
        x = d
        y = c


        for i in range(8):
            x += 1
            y += 1

            if x > 8 or y > 8:
                break
            else:
                dr.append((y,x))
                if (y,x) == (e,f):
                    break

        x = d
        y = c


        for i in range(8):
            x -= 1
            y -= 1

            if x < 1 or y < 1:
                break
            else:
                ul.append((y,x))
                if (y,x) == (e,f):
                    break

        x = d
        y = c


        for i in range(8):
            x -= 1
            y += 1

            if x < 1 or y > 8:
                break
            else:
                dl.append((y,x))
                if (y,x) == (e,f):
                    break
        x = d
        y = c



        for i in range(8):
            x += 1
            y -= 1
            if x < 1 or y > 8:
                break
            else:
                ur.append((y,x))
                if (y,x) == (e,f):
                    break
        if a == e:
            if c == a:
                if b < d < f or f < d < b:
                    return 2
                else:
                    return 1
            else:
                return 1

        if b == f:
            if d == b:
                if a <c < e or e < c < a:

                    return 2
                else:
                    return 1
            else:
                return 1

        if (e,f) in ul:
            if (a,b) in ul:
                return 2
            return 1
        if (e,f) in ur:
            if (a,b) in ur:
                return 2
            return 1
        if (e,f) in dr:
            if (a,b) in dr:
                return 2
            return 1
        if (e,f) in dl:
            if (a,b) in dl:
                return 2
            return 1
        return 2





