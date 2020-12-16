class Weight:
    def __init__(self, m):
        self.m = m

    def to_centner(self):
        self.m=self.m/100
        return self.m

    def __add__(self, n):
        res = self.m/100 + n/100
        return res

    def __sub__(self, n):
        if n > self.m:
            raise ValueError
        res = self.m/100 - n/100
        return res

    def __mul__(self, n):
        res = self.m/100 * n/100
        return res

print(Weight(100).to_centner())
print(Weight(267).__add__(300))