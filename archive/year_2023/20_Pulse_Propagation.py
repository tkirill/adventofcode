from __future__ import annotations

from aoc.io import *
from dataclasses import dataclass
import abc
from collections import deque
import math


@dataclass
class ModuleABC(abc.ABC):
    def receive(self, src: str, signal: int) -> int:
        ...

    def register_input(self, src: str):
        ...


@dataclass
class Broadcaster(ModuleABC):
    def receive(self, src: str, signal: int) -> int:
        return signal


@dataclass
class FlipFlop(ModuleABC):
    on: False

    def receive(self, src: str, signal: int) -> int:
        if signal == 0:
            self.on = not self.on
            return int(self.on)


@dataclass
class Conjunction(ModuleABC):
    memory: dict[str, int]

    def register_input(self, src: str):
        self.memory[src] = 0

    def receive(self, src: str, signal: int) -> int:
        self.memory[src] = signal
        return 0 if all(x == 1 for x in self.memory.values()) else 1


def build_mesh():
    modules: dict[str, ModuleABC] = {}
    destinations: dict[str, list[str]] = {}

    for src, *dsts in read(sep="(?: -> )|(?:, )"):
        module = None
        name = None
        match src[0]:
            case "%":
                module = FlipFlop(False)
                name = src[1:]
            case "&":
                module = Conjunction({})
                name = src[1:]
            case _:
                module = Broadcaster()
                name = src
        modules[name] = module
        destinations[name] = dsts
    modules["button"] = Broadcaster()
    destinations["button"] = ["broadcaster"]
    for src, dsts in list(destinations.items()):
        for d in dsts:
            if d not in modules:
                modules[d] = Broadcaster()
                destinations[d] = []
            modules[d].register_input(src)

    return modules, destinations


def push_button():
    q = deque([("button", "broadcaster", 0)])
    while q:
        cur = q.popleft()
        yield cur
        src, dst, input_signal = cur
        output_signal = modules[dst].receive(src, input_signal)
        if output_signal is not None:
            for nxt in destinations[dst]:
                q.append((dst, nxt, output_signal))


modules, destinations = build_mesh()
total_low, total_high = 0, 0
for i in range(1000):
    for src, dst, signal in push_button():
        total_low += signal == 0
        total_high += signal == 1
print("Star 1:", total_low * total_high)


modules, destinations = build_mesh()
pulse_stat = {k: None for k in ["lk", "zv", "sp", "xt"]}
for i in range(5000):
    for src, dst, signal in push_button():
        if signal == 1 and src in pulse_stat and pulse_stat[src] is None:
            pulse_stat[src] = i + 1
print("Star 2:", math.lcm(*pulse_stat.values()))
