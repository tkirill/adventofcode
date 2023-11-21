from __future__ import annotations
from aoc import *
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

    def near(self, minutes) -> Iterable[State]:
        if self.minute == minutes:
            return

        built = False
        if self.robots.ore < self.blueprint.max_required_robots.ore and self.blueprint.ore_robot in self.resources:
            yield replace(
                self,
                minute=self.minute + 1,
                resources=self.resources - self.blueprint.ore_robot + self.robots,
                robots=self.robots + ResourceVector(ore=1),
            )
            built = True
        if self.robots.clay < self.blueprint.max_required_robots.clay and self.blueprint.clay_robot in self.resources:
            yield replace(
                self,
                minute=self.minute + 1,
                resources=self.resources - self.blueprint.clay_robot + self.robots,
                robots=self.robots + ResourceVector(clay=1),
            )
            built = True
        if self.robots.obsidian < self.blueprint.max_required_robots.obsidian and self.blueprint.obsidian_robot in self.resources:
            yield replace(
                self,
                minute=self.minute + 1,
                resources=self.resources - self.blueprint.obsidian_robot + self.robots,
                robots=self.robots + ResourceVector(obsidian=1),
            )
            built = True
        if self.blueprint.geode_robot in self.resources:
            yield replace(
                self,
                minute=self.minute + 1,
                resources=self.resources - self.blueprint.geode_robot + self.robots,
                robots=self.robots + ResourceVector(geode=1),
            )
            built = self.blueprint.geode_robot
        if not built:
            yield replace(
                self,
                minute=self.minute + 1,
                resources=self.resources + self.robots,
            )


def get_max_geodes(bp: Bluepint, minutes: int) -> int:
    max_geodes = 0
    for s, minute in bfs(State(blueprint=bp), lambda x: x.near(minutes)):
        if s.minute == minutes and s.resources.geode > max_geodes:
            max_geodes = s.resources.geode
            print(bp.id, max_geodes)
    return max_geodes


def get_bluepint_score(bp: Bluepint) -> int:
    return bp.id * get_max_geodes(bp, 24)


blueprints = [parse_blueprint(s) for s in readlines()]

print('Star 1:', sum(get_bluepint_score(x) for x in blueprints))
print('Star 2:', get_max_geodes(blueprints[0], 32) * get_max_geodes(blueprints[1], 32) * get_max_geodes(blueprints[2], 32))