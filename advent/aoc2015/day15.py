from functools import reduce
from typing import Iterable, List

RECIPIE_TEASPOONS = 100
CALORIE_REQUIREMENT = 500


class Ingredient:
    def __init__(self, ingredient_str: str):
        self.name, properties_str = ingredient_str.split(": ")
        properties: List[str] = properties_str.split(", ")
        self.properties = {name: int(value) for name, value in map(
            lambda p: p.split(), properties)}

    def __repr__(self):
        return f"{self.name} ({self.properties})"


def product(iterable: Iterable):
    """Return the product of a non-empty iterable."""
    return reduce(lambda a, b: a * b, iterable)


def recipie_generator(ingredient_count: int, teasponns: int):
    """
    https://www.reddit.com/r/adventofcode/comments/3wwj84/day_15_solutions/cxzk44a?utm_source=share&utm_medium=web2x
    """
    start = (teasponns if ingredient_count == 1 else 0)
    for i in range(start, teasponns+1):
        remaining = teasponns - i
        if ingredient_count-1:
            for y in recipie_generator(ingredient_count-1, remaining):
                yield [i] + y
        else:
            yield [i]


def score_cookie(ingredients, recipie):
    property_names = {p for p in ingredients[0].properties if p != "calories"}
    return product(calculate_property_score(ingredients, recipie, property_name) for property_name in property_names)


def count_calories(ingredients, recipie):
    return calculate_property_score(ingredients, recipie, "calories")


def calculate_property_score(ingredients, recipie, property_name):
    return max(0, sum(recipie[i] * ingredient.properties[property_name] for i, ingredient in enumerate(ingredients)))


def parta(txt):
    ingredients = [Ingredient(line) for line in txt.splitlines()]
    return max(score_cookie(ingredients, recipie) for recipie in recipie_generator(len(ingredients), RECIPIE_TEASPOONS))


def partb(txt):
    ingredients = [Ingredient(line) for line in txt.splitlines()]
    return max(
        score_cookie(ingredients, recipie)
        for recipie in recipie_generator(len(ingredients), RECIPIE_TEASPOONS)
        if count_calories(ingredients, recipie) == CALORIE_REQUIREMENT
    )


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
