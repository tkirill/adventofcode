from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterable
from itertools import islice
import more_itertools

from aoc.io import *


@dataclass
class DoublyLinkedNode:
    value: int
    prev: DoublyLinkedNode | None = None
    next: DoublyLinkedNode | None = None

    def forward(self) -> Iterable[DoublyLinkedNode]:
        cur = self
        while cur is not None:
            yield cur
            cur = cur.next
    
    def backward(self) -> Iterable[DoublyLinkedNode]:
        cur = self
        while cur is not None:
            yield cur
            cur = cur.prev


class CircuralDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def nodes(self) -> Iterable[DoublyLinkedNode]:
        if self.head is None:
            return
        yield from islice(self.head.forward(), self.size)
    
    def append(self, node: DoublyLinkedNode):
        if self.head is None:
            self.size = 1
            self.head = node
            node.next = node
            node.prev = node
        else:
            self.insert_before(self.head, node)
    
    def insert_before(self, pos: DoublyLinkedNode, node: DoublyLinkedNode):
        self.size += 1
        prev = pos.prev
        prev.next = node
        pos.prev = node
        node.prev = prev
        node.next = pos
    
    def insert_after(self, pos: DoublyLinkedNode, node: DoublyLinkedNode):
        self.size += 1
        tmp = pos.next
        pos.next = node
        tmp.prev = node
        node.prev = pos
        node.next = tmp
    
    def remove(self, node: DoublyLinkedNode):
        self.size -= 1
        node.prev.next = node.next
        node.next.prev = node.prev

        if self.head is node:
            if self.head.next is self.head:
                self.head = None
            else:
                self.head = self.head.next
        node.prev = None
        node.next = None
    
    def find(self, value: int) -> DoublyLinkedNode:
        for n in self.head.forward():
            if n.value == value:
                return n
    
    def __str__(self):
        return ' '.join(str(x.value) for x in self.nodes())
    
    @classmethod
    def from_values(cls, values: Iterable[int]):
        result = CircuralDoublyLinkedList()
        for v in values:
            result.append(DoublyLinkedNode(value=v))
        return result


def mix(file: CircuralDoublyLinkedList, times: int):
    nodes = list(file.nodes())
    for _ in range(times):
        for cur in nodes:
            if abs(cur.value) == file.size:
                continue
            steps = cur.value % (file.size - 1)
            if steps > 0:
                tmp = more_itertools.nth(cur.forward(), steps)
                file.remove(cur)
                file.insert_after(tmp, cur)
            elif steps < 0:
                tmp = more_itertools.nth(cur.backward(), -steps)
                file.remove(cur)
                file.insert_before(tmp, cur)


def grove_coordinates(file: CircuralDoublyLinkedList) -> int:
    zero = file.find(0)
    tmp = list(islice(zero.forward(), 3001))
    return tmp[1000].value + tmp[2000].value + tmp[3000].value


file = CircuralDoublyLinkedList.from_values(read())
mix(file, 1)
print('Star 1:', grove_coordinates(file))

decryption_key = 811589153
file = CircuralDoublyLinkedList.from_values(x * decryption_key for x in read())
mix(file, 10)
print('Star 2:', grove_coordinates(file))