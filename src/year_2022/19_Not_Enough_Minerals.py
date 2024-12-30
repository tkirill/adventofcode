from __future__ import annotations
from aoc.io import *
from aoc.algo import bfs
from collections.abc import Iterable
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class ResourceVector:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __add__(self, other: ResourceVector) -> ResourceVector:
        return replace(
            self,
            ore=self.ore + other.ore,
            clay=self.clay + other.clay,
            obsidian=self.obsidian + other.obsidian,
            geode=self.geode + other.geode,
        )

    def __sub__(self, other: ResourceVector) -> ResourceVector:
        return replace(
            self,
            ore=self.ore - other.ore,
            clay=self.clay - other.clay,
            obsidian=self.obsidian - other.obsidian,
            geode=self.geode - other.geode,
        )
    
    def __mul__(self, other: int) -> ResourceVector:
        return replace(
            self,
            ore=self.ore * other,
            clay=self.clay * other,
            obsidian=self.obsidian * other,
            geode=self.geode * other
        )

    def __contains__(self, item: ResourceVector) -> bool:
        return (
            self.ore >= item.ore
            and self.clay >= item.clay
            and self.obsidian >= item.obsidian
            and self.geode >= item.geode
        )


@dataclass(frozen=True)
class Bluepint:
    id: int
    ore_robot: ResourceVector
    clay_robot: ResourceVector
    obsidian_robot: ResourceVector
    geode_robot: ResourceVector
    max_required_robots: ResourceVector


def parse_blueprint(s):
    (
        id,
        ore_robot_cost,
        clay_robot_cost,
        obsidian_robot_cost_ore,
        obsidian_robot_cost_clay,
        geode_robot_cost_ore,
        geode_robot_cost_obsidian,
    ) = allints(s)
    max_required_robots = ResourceVector(
        ore=max(
            ore_robot_cost,
            clay_robot_cost,
            obsidian_robot_cost_ore,
            geode_robot_cost_ore,
        ),
        clay=obsidian_robot_cost_clay,
        obsidian=geode_robot_cost_obsidian,
    )
    return Bluepint(
        id,
        ResourceVector(ore=ore_robot_cost),
        ResourceVector(ore=clay_robot_cost),
        ResourceVector(ore=obsidian_robot_cost_ore, clay=obsidian_robot_cost_clay),
        ResourceVector(ore=geode_robot_cost_ore, obsidian=geode_robot_cost_obsidian),
        max_required_robots,
    )


@dataclass(frozen=True)
class State:
    blueprint: Bluepint
    minute: int = 0
    resources: ResourceVector = ResourceVector()
    robots: ResourceVector = ResourceVector(ore=1)

    def minutes_until_next(self, bp: ResourceVector):
        d = bp - self.resources
        result = 0
        if d.ore > 0:
            if not self.robots.ore:
                return None
            result = max(result, d.ore // self.robots.ore + ((d.ore % self.robots.ore) > 0))
        if d.clay > 0:
            if not self.robots.clay:
                return None
            result = max(result, d.clay // self.robots.clay + ((d.clay % self.robots.clay) > 0))
        if d.obsidian > 0:
            if not self.robots.obsidian:
                return None
            result = max(result, d.obsidian // self.robots.obsidian + ((d.obsidian % self.robots.obsidian) > 0))
        return result


    def near(self, minutes) -> Iterable[State]:
        if self.minute == minutes:
            return

        if self.robots.ore < self.blueprint.max_required_robots.ore:
            nadd = self.minutes_until_next(self.blueprint.ore_robot)
            if self.minute + nadd + 1 <= minutes:
                yield replace(
                    self,
                    minute=self.minute + nadd + 1,
                    resources=self.resources + self.robots * (nadd + 1) - self.blueprint.ore_robot,
                    robots=self.robots + ResourceVector(ore=1),
                )
        if self.robots.clay < self.blueprint.max_required_robots.clay:
            nadd = self.minutes_until_next(self.blueprint.clay_robot)
            if self.minute + nadd + 1 <= minutes:
                yield replace(
                    self,
                    minute=self.minute + nadd + 1,
                    resources=self.resources + self.robots * (nadd + 1) - self.blueprint.clay_robot,
                    robots=self.robots + ResourceVector(clay=1),
                )
        if self.robots.obsidian < self.blueprint.max_required_robots.obsidian and self.robots.clay:
            nadd = self.minutes_until_next(self.blueprint.obsidian_robot)
            if self.minute + nadd + 1 <= minutes:
                yield replace(
                    self,
                    minute=self.minute + nadd + 1,
                    resources=self.resources + self.robots * (nadd + 1) - self.blueprint.obsidian_robot,
                    robots=self.robots + ResourceVector(obsidian=1),
                )
        if self.robots.obsidian:
            nadd = self.minutes_until_next(self.blueprint.geode_robot)
            if self.minute + nadd + 1 <= minutes:
                yield replace(
                    self,
                    minute=self.minute + nadd + 1,
                    resources=self.resources + self.robots * (nadd + 1) - self.blueprint.geode_robot,
                    robots=self.robots + ResourceVector(geode=1),
                )


def get_max_geodes(bp: Bluepint, minutes: int) -> int:
    max_geodes = 0
    for s, minute in bfs(State(blueprint=bp), lambda x: x.near(minutes)):
        if s.minute == minutes and s.resources.geode > max_geodes:
            max_geodes = s.resources.geode
    # print(bp.id, max_geodes)
    return max_geodes


def get_bluepint_score(bp: Bluepint) -> int:
    return bp.id * get_max_geodes(bp, 24)


blueprints = [parse_blueprint(s) for s in readlines()]

import datetime
print(datetime.datetime.now())
print('Star 1:', sum(get_bluepint_score(x) for x in blueprints))
print(datetime.datetime.now())
print('Star 2:', get_max_geodes(blueprints[0], 32) * get_max_geodes(blueprints[1], 32) * get_max_geodes(blueprints[2], 32))
print(datetime.datetime.now())


# 2024-12-30 20:10:58.468635
# Star 1: 1550
# 2024-12-30 20:11:26.625220
# Star 2: 18630
# 2024-12-30 20:21:28.482330