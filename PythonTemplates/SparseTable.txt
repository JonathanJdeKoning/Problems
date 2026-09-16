
class SparseTable:
    def __init__(self, arr, func=min):
        self.func = func
        self.N = len(arr)
        
        if self.N == 0:
            self.A = []
            self.log = []
            return

        self.log = [0] * (self.N + 1)
        for i in range(2, self.N + 1):
            self.log[i] = self.log[i // 2] + 1

        K = self.log[self.N] + 1

        self.A = [None] * K
        
        self.A[0] = list(arr) 

        for i in range(1, K):
            curr_len = 1 << i
            prev_len = 1 << (i - 1)
            num_entries = self.N - curr_len + 1
            
            self.A[i] = [0] * num_entries

            for j in range(num_entries):
                self.A[i][j] = self.func(self.A[i - 1][j], self.A[i - 1][j + prev_len])
        
    def query(self, L, R):
        if L > R:
            raise ValueError(f"Invalid query range: L={L}, R={R}")
        
        if L < 0 or R >= self.N:
            raise IndexError("Query out of bounds")
        
        if self.N == 0:
            raise ValueError("Query on empty table")

        n = R - L + 1
        lg = self.log[n]
        k_len = 1 << lg
        
        return self.func(self.A[lg][L], self.A[lg][R - k_len + 1])
