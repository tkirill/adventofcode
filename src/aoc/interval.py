from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Interval:

    begin: int
    end: int

    def __contains__(self, key: int) -> bool:
        return self.begin <= key < self.end
    
    def __and__(self, other: Interval) -> Interval:
        if self.end < other.begin or self.begin > other.end:
            return None
        return Interval(max(self.begin, other.begin), min(self.end, other.end))
    
    def __len__(self) -> int:
        return self.end - self.begin
    
    @classmethod
    def of_length(cls, begin: int, length: int) -> Interval:
        return Interval(begin, begin + length)


def is_overlapped(a: Interval, b: Interval) -> bool:
    pass