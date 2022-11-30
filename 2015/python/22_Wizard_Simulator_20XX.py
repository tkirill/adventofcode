from dataclasses import dataclass
from functools import cache


@dataclass(frozen=True)
class Spell:
    name: str
    cost: int
    damage: int
    heal: int
    armor: int
    mana: int
    turns: int

    def tick(self):
        return Spell(self.name, self.cost, self.damage, self.heal, self.armor, self.mana, self.turns - 1)


@dataclass(frozen=True)
class EffectSet:
    active: frozenset[Spell]

    def summarize(self) -> tuple[int, int, int]:
        a, d, m = 0, 0, 0
        for e in self.active:
            a += e.armor
            d += e.damage
            m += e.mana
        return a, d, m
    
    def tick(self):
        tmp = []
        for e in self.active:
            if e.turns > 1:
                tmp.append(e.tick())
        return EffectSet(frozenset(tmp))
    
    def add_effect(self, spell: Spell):
        tmp = list(self.active)
        tmp.append(spell)
        return EffectSet(frozenset(tmp))
    
    def contains(self, spell: Spell):
        return any(x.name == spell.name for x in self.active)


@dataclass(frozen=True)
class Player:
    health: int
    armor: int
    mana: int

    def is_dead(self):
        return self.health <= 0
    
    def add_armor_mana(self, a, m):
        return Player(self.health, a, self.mana + m)
    
    def take_mana(self, spell: Spell):
        return Player(self.health, self.armor, self.mana - spell.cost)
    
    def apply_spell(self, spell: Spell):
        return Player(self.health + spell.heal, self.armor, self.mana - spell.cost)
    
    def hit(self, d: int):
        return Player(self.health - max(d - self.armor, 1), self.armor, self.mana)


@dataclass(frozen=True)
class Boss:
    health: int
    damage: int

    def is_dead(self):
        return self.health <= 0
    
    def hit(self, d):
        return Boss(self.health - d, self.damage)
    
    def apply_spell(self, spell: Spell):
        if spell.damage:
            return Boss(self.health - spell.damage, self.damage)
        return self


@dataclass(frozen=True)
class State:
    player: Player
    boss: Boss
    effects: EffectSet


SPELLS = [
    Spell('Magic Missile', 53, 4, 0, 0, 0, 0),
    Spell('Drain', 73, 2, 2, 0, 0, 0),
    Spell('Shield', 113, 0, 0, 7, 0, 6),
    Spell('Poison', 173, 3, 0, 0, 0, 6),
    Spell('Recharge', 229, 0, 0, 0, 101, 5)
]


def execute_effects(state: State) -> State:
    a, d, m = state.effects.summarize()
    return State(state.player.add_armor_mana(a, m), state.boss.hit(d), state.effects.tick())


def possible_spells(state: State) -> list[Spell]:
    tmp = []
    for spell in SPELLS:
        if spell.cost <= state.player.mana and (not spell.turns or not state.effects.contains(spell)):
            tmp.append(spell)
    return tmp


def apply_spell(spell: Spell, state: State) -> State:
    if spell.turns:
        return State(state.player.take_mana(spell), state.boss, state.effects.add_effect(spell))
    return State(state.player.apply_spell(spell), state.boss.apply_spell(spell), state.effects)


def do_penalty(state: State, penalty: int) -> State:
    if penalty:
        return State(state.player.hit(penalty), state.boss, state.effects)
    return state


def boss_turn(state: State, penalty: int) -> State:
    state = execute_effects(state)
    if state.boss.is_dead():
        return state
    return State(state.player.hit(state.boss.damage), state.boss, state.effects)


def game_loop_with_spell(spell: Spell, state: State, penalty: int) -> int:
    state = apply_spell(spell, state)
    if state.boss.is_dead():
        return spell.cost

    state = boss_turn(state, penalty)
    if state.player.is_dead():
        return None
    if state.boss.is_dead():
        return spell.cost
    
    cost = game_loop(state, penalty)
    return None if cost is None else cost + spell.cost


@cache
def game_loop(state: State, penalty: int) -> int:
    state = do_penalty(state, penalty)
    if state.player.is_dead():
        return None
    state = execute_effects(state)
    if state.boss.is_dead():
        return 0
    
    next_spells = possible_spells(state)
    if not next_spells:
        return None
    
    return min(filter(None, (game_loop_with_spell(spell, state, penalty) for spell in next_spells)), default=None)


def read_boss():
    boss = dict()
    for line in open('22_input.txt'):
        n, v = line.split(': ')
        boss[n] = int(v)
    return Boss(boss['Hit Points'], boss['Damage'])


print('Star 1:', game_loop(State(Player(50, 0, 500), read_boss(), EffectSet(frozenset())), 0))
print('Star 2:', game_loop(State(Player(50, 0, 500), read_boss(), EffectSet(frozenset())), 1))