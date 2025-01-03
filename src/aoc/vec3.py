from __future__ import annotations

from aoc.primitives import Vec3


def up(v: Vec3):
    return Vec3(v.x, v.y-1, v.z)


def down(v: Vec3):
    return Vec3(v.x, v.y+1, v.z)


def left(v: Vec3):
    return Vec3(v.x-1, v.y, v.z)


def right(v: Vec3):
    return Vec3(v.x+1, v.y, v.z)


def forward(v: Vec3):
    return Vec3(v.x, v.y, v.z+1)


def backward(v: Vec3):
    return Vec3(v.x, v.y, v.z-1)


def near6(v: Vec3):
    yield up(v)
    yield down(v)
    yield left(v)
    yield right(v)
    yield forward(v)
    yield backward(v)