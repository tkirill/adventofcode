from abc import ABC, abstractproperty
from dataclasses import dataclass


@dataclass
class Vector2D[TScalar]:

    v1: TScalar
    v2: TScalar

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    @classmethod
    def zero() -> Vector2D[TScalar]:
        return Vector2D(TScalar(), TScalar())


class IntVector2D(Vector2D[int]):
    pass