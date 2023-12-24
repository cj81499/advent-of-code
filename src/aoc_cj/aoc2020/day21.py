class Food:
    def __init__(self, food_str):
        self.ingredients, self.allergens = food_str.strip(")").split(" (contains ")
        self.ingredients = set(self.ingredients.split())
        self.allergens = set(self.allergens.split(", "))


def get_alergens_to_ingredients(foods):
    alerg_to_ingrs = {}
    for f in foods:
        for a in f.allergens:
            if a in alerg_to_ingrs:
                alerg_to_ingrs[a] = alerg_to_ingrs[a].intersection(f.ingredients)
            else:
                alerg_to_ingrs[a] = f.ingredients

    while not all(len(ingrs) == 1 for ingrs in alerg_to_ingrs.values()):
        solved = {ingr for ingrs in alerg_to_ingrs.values() for ingr in ingrs if len(ingrs) == 1}
        for a in alerg_to_ingrs:
            if len(alerg_to_ingrs[a]) != 1:
                alerg_to_ingrs[a] = alerg_to_ingrs[a].difference(solved)

    # dict[str, set[str]] -> dict[str, str]
    a_to_i = {alerg: ingrs.pop() for alerg, ingrs in alerg_to_ingrs.items()}

    return a_to_i


def part_1(txt):
    foods = [Food(f) for f in txt.splitlines()]
    a_to_i = get_alergens_to_ingredients(foods)

    all_ingredients = {i for f in foods for i in f.ingredients}
    safe_ingredients = all_ingredients.difference(i for i in a_to_i.values())

    return sum(i in f.ingredients for i in safe_ingredients for f in foods)


def part_2(txt):
    foods = [Food(f) for f in txt.splitlines()]
    a_to_i = get_alergens_to_ingredients(foods)
    return ",".join(a_to_i[a] for a in sorted(a_to_i))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
