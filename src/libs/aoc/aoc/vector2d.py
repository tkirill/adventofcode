from typing import get_args, get_origin
from types import get_original_bases
from dataclasses import dataclass


@dataclass
class Vector2D[TScalar]:

    v1: TScalar
    v2: TScalar

    def __init__(self, v1: TScalar, v2: TScalar):
        self.v1 = v1
        self.v2 = v2
    
    def __add__(self, other: Vector2D[TScalar]):
        if not isinstance(other, self.__class__):
            raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")
        return self.__class__(self.v1 + other.v1, self.v2 + other.v2)
    
    def increment(self, v: TScalar):
        return self.__class__(self.v1 + v, self.v2 + v)
    
    @classmethod
    def same(cls, v: TScalar):
        return cls(v, v)
    
    @classmethod
    def zero(cls) -> IntVector2D:
        type_args = get_args(cls)
        
        if not type_args:
            for base in get_original_bases(cls):
                if get_origin(base) is Vector2D:
                    type_args = get_args(base)
                    break
        scalar = type_args[0]
        return cls(scalar(), scalar())


class IntVector2D(Vector2D[int]):
    pass