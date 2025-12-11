import dataclasses
import math
import re
from collections.abc import Generator, Sequence
from typing import ClassVar, Literal, TypeIs, assert_never, cast

XMAS = Literal["x", "m", "a", "s"]
COMPARISON = Literal["<", ">"]


def is_xmas(o: object) -> TypeIs[XMAS]:
    return o in ("x", "m", "a", "s")


def is_comparison(o: object) -> TypeIs[COMPARISON]:
    return o in ("<", ">")


@dataclasses.dataclass(frozen=True)
class Rule:
    lhs: XMAS
    op: COMPARISON
    rhs: int
    result: str

    CONDITION_PATTERN: ClassVar = re.compile(r"^(?P<lhs>[xmas])(?P<op>[<>])(?P<rhs>\d+):(?P<result>[a-zA-Z]+)$")

    @staticmethod
    def parse(s: str) -> "Rule":
        match = Rule.CONDITION_PATTERN.match(s)
        assert match is not None, f"failed to match {s}"
        lhs, op, rhs, result = match.group("lhs", "op", "rhs", "result")
        assert is_xmas(lhs)
        assert is_comparison(op)
        return Rule(lhs=lhs, op=op, rhs=int(rhs), result=result)

    def matches(self, part_rating: dict[str, int]) -> bool:
        lhs_value = part_rating[self.lhs]
        if self.op == "<":
            return lhs_value < self.rhs
        if self.op == ">":
            return lhs_value > self.rhs
        assert_never(self.op)


@dataclasses.dataclass(frozen=True)
class Workflow:
    name: str
    rules: Sequence[Rule]
    fallback: str

    WORKFLOW_PATTERN: ClassVar = re.compile(r"^(?P<name>[a-zA-Z]+){(?P<conditions>.*),(?P<fallback>[a-zA-Z]+)}$")

    @staticmethod
    def parse(s: str) -> "Workflow":
        match = Workflow.WORKFLOW_PATTERN.match(s)
        assert match is not None, f"failed to match {s}"
        return Workflow(
            name=match.group("name"),
            rules=[Rule.parse(c) for c in match.group("conditions").split(",")],
            fallback=match.group("fallback"),
        )

    def apply(self, part_rating: dict[str, int]) -> str:
        for r in self.rules:
            if r.matches(part_rating):
                return r.result
        return self.fallback

    def is_acceptable(self, workflows: dict[str, "Workflow"], part_rating: dict[str, int]) -> bool:
        result = self.apply(part_rating)
        if result == "A":
            return True
        if result == "R":
            return False
        return workflows[result].is_acceptable(workflows, part_rating)


def part_1(txt: str) -> int:
    workflows_str, part_ratings = txt.split("\n\n")
    workflows = {(wf := Workflow.parse(line)).name: wf for line in workflows_str.splitlines()}
    part_ratings = [
        {(p := pair.partition("="))[0]: int(p[2]) for pair in line.removeprefix("{").removesuffix("}").split(",")}
        for line in part_ratings.splitlines()
    ]

    # for part_rating in part_ratings:
    return sum(sum(part.values()) for part in part_ratings if workflows["in"].is_acceptable(workflows, part))


XMASRanges = dict[XMAS, range]


def part_2(txt: str) -> int:
    workflows_str, _ = txt.split("\n\n")
    workflows = {(wf := Workflow.parse(line)).name: wf for line in workflows_str.splitlines()}

    def _acceptable_part_ranges_helper(result: str, ranges: XMASRanges) -> Generator[XMASRanges]:
        if result == "A":
            yield ranges
        elif result != "R":
            yield from acceptable_part_ranges(workflows[result], ranges)

    def acceptable_part_ranges(wf: Workflow, ranges: XMASRanges | None = None) -> Generator[XMASRanges]:
        ranges = {cast("XMAS", k): range(1, 4001) for k in "xmas"} if ranges is None else ranges.copy()
        for rule in wf.rules:
            go_to_result_ranges = ranges.copy()

            # update continue_workflow_ranges and go_to_result_ranges based on rule
            go_to_result_r = go_to_result_ranges[rule.lhs]
            continue_wf_r = ranges[rule.lhs]
            if rule.op == "<":
                go_to_result_ranges[rule.lhs] = range(go_to_result_r.start, min(go_to_result_r.stop, rule.rhs))
                ranges[rule.lhs] = range(max(continue_wf_r.start, rule.rhs), continue_wf_r.stop)
            elif rule.op == ">":
                go_to_result_ranges[rule.lhs] = range(max(go_to_result_r.start, rule.rhs + 1), go_to_result_r.stop)
                ranges[rule.lhs] = range(continue_wf_r.start, min(continue_wf_r.stop, rule.rhs + 1))
            else:
                assert_never(rule.op)

            yield from _acceptable_part_ranges_helper(rule.result, go_to_result_ranges)
        yield from _acceptable_part_ranges_helper(wf.fallback, ranges)

    # count # of parts in each range of acceptable parts
    return sum(math.prod((v.stop - v.start) for v in r.values()) for r in acceptable_part_ranges(workflows["in"]))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
