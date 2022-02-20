from typing import Optional, Dict, Tuple, List, Callable


class TriangleBuilder:

    def __init__(self, memory: Optional[Dict] = None):
        self.memory = memory or {}

    def get(self, i: int, j: int, default: Callable = lambda: None):
        if j == 0 or i == j:
            return 1
        key = (i, j)
        return self.memory.get(key, default)()

    def save(self, key: Tuple[int, int], value: int) -> int:
        self.memory[key] = lambda: value
        return value

    def create(self, i: int, j: int) -> int:
        if j == 0 or i == j:
            return 1
        upper_left = self.get_or_create(i=i-1, j=j-1)
        upper_center = self.get_or_create(i=i-1, j=j)
        return self.save(key=(i, j), value=upper_left+upper_center)

    def get_or_create(self, i: int, j: int) -> int:
        return self.get(i=i, j=j, default=lambda: self.create(i=i, j=j))

    def get_row(self, index: int) -> List[int]:
        return [
                self.get_or_create(i=index, j=j)
                for j in range(index+1)
            ]
