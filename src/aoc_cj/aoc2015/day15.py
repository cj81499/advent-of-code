import math
from typing import Generator, override

RECIPE_TEASPOONS = 100
CALORIE_REQUIREMENT = 500


class Ingredient:
    def __init__(self, ingredient_str: str) -> None:
        self.name, properties_str = ingredient_str.split(": ")
        properties: list[str] = properties_str.split(", ")
        self.properties = {name: int(value) for name, value in map(lambda p: p.split(), properties)}

    @override
    def __repr__(self) -> str:
        return f"{self.name} ({self.properties})"


def recipe_generator(ingredient_count: int, teaspoons: int) -> Generator[list[int], None, None]:
    """
    https://www.reddit.com/r/adventofcode/comments/3wwj84/day_15_solutions/cxzk44a?utm_source=share&utm_medium=web2x
    """
    start = teaspoons if ingredient_count == 1 else 0
    for i in range(start, teaspoons + 1):
        remaining = teaspoons - i
        if ingredient_count - 1:
            for y in recipe_generator(ingredient_count - 1, remaining):
                yield [i, *y]
        else:
            yield [i]


def score_cookie(ingredients: list[Ingredient], recipe: list[int]) -> int:
    property_names = {p for p in ingredients[0].properties if p != "calories"}
    return math.prod(calculate_property_score(ingredients, recipe, property_name) for property_name in property_names)


def count_calories(ingredients: list[Ingredient], recipe: list[int]) -> int:
    return calculate_property_score(ingredients, recipe, "calories")


def calculate_property_score(ingredients: list[Ingredient], recipe: list[int], property_name: str) -> int:
    return max(0, sum(recipe[i] * ingredient.properties[property_name] for i, ingredient in enumerate(ingredients)))


def part_1(txt: str) -> int:
    ingredients = [Ingredient(line) for line in txt.splitlines()]
    return max(score_cookie(ingredients, recipe) for recipe in recipe_generator(len(ingredients), RECIPE_TEASPOONS))


def part_2(txt: str) -> int:
    ingredients = [Ingredient(line) for line in txt.splitlines()]
    return max(
        score_cookie(ingredients, recipe)
        for recipe in recipe_generator(len(ingredients), RECIPE_TEASPOONS)
        if count_calories(ingredients, recipe) == CALORIE_REQUIREMENT
    )


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
