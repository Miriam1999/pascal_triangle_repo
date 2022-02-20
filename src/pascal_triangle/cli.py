from .helpers import TriangleBuilder


class CLI:

    def get_element(self,
                    i: int,
                    j: int) -> int:
        return 1 if j == 0 and i == j else \
            self.get_element(i=i-1, j=j) + self.get_element(i=i-1, j=j-1)

    def naive(self, level: int, index: int = 0):
        if index < level:
            row = [
                self.get_element(i=index, j=j)
                for j in range(index+1)
            ]
            print(*row, sep=" ")
            self.naive(level=level, index=index+1)

    @staticmethod
    def optimized(level: int, index: int = 0):
        builder = TriangleBuilder()

        def recursive(i: int):
            if i >= level:
                return
            row = builder.get_row(index=i)
            print(*row, sep=" ")
            recursive(i=i+1)
        return recursive(i=index)
