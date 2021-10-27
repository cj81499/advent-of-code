class Group:
    def __init__(
        self,
        unit_count: int,
        unit_hp: int,
        unit_dmg: int,
        initiative: int,
        attack_type: str,
        weaknesses: list,
        immunities: list,
        army_name: str,
        group_num: int,
    ):
        self.unit_count = unit_count
        self.unit_hp = unit_hp
        self.unit_dmg = unit_dmg
        self.initiative = initiative
        self.attack_type = attack_type
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.army_name = army_name
        self.group_num = group_num

        self.alive_unit_count = unit_count

    def effective_power(self):
        return max(0, self.alive_unit_count) * self.unit_dmg

    def __str__(self):
        return self.army_name + " group " + str(self.group_num)

    def __repr__(self):
        return str(
            (
                self.unit_count,
                self.unit_hp,
                self.unit_dmg,
                self.initiative,
                self.attack_type,
                self.weaknesses,
                self.immunities,
            )
        )

    @classmethod
    def parseGroup(cls, group_str: str, army_name: str, number: int, immune_boost=0):
        words = group_str.split()
        nums = [int(s) for s in words if s.isdigit()]
        attack_type = words[words.index("damage") - 1]
        weaknesses = None
        immunities = None
        open_paren = group_str.find("(")
        if open_paren != -1:
            close_paren = group_str.find(")")
            modifiers = group_str[open_paren + 1 : close_paren].split("; ")
            for modifier in modifiers:
                if modifier[0] == "w":
                    modifier = modifier[8:]
                    weaknesses = modifier.split(", ")
                elif modifier[0] == "i":
                    modifier = modifier[10:]
                    immunities = modifier.split(", ")
        if army_name == "Immune System":
            nums[2] += immune_boost
        return cls(nums[0], nums[1], nums[2], nums[3], attack_type, weaknesses, immunities, army_name, number)

    def calculate_dmg(self, defender):
        dmg_dealt = self.effective_power()
        if defender.immunities is not None and self.attack_type in defender.immunities:
            dmg_dealt = 0
        elif defender.weaknesses is not None and self.attack_type in defender.weaknesses:
            dmg_dealt *= 2
        return dmg_dealt

    def take_dmg_from(self, attacker):
        dmg = attacker.calculate_dmg(self)
        kill_count = dmg // self.unit_hp
        if kill_count > self.alive_unit_count:
            kill_count = self.alive_unit_count
        self.alive_unit_count -= kill_count
        return kill_count


class Army:
    def __init__(self, groups: list, name: str):
        self.groups = groups
        self.name = name

    @classmethod
    def parseArmy(cls, army_str: str, immune_boost=0):
        group_list = []
        group_str_list = army_str.strip().splitlines()
        army_name = group_str_list.pop(0)[:-1]
        group_number = 1
        for group_str in group_str_list:
            group = Group.parseGroup(group_str, army_name, group_number, immune_boost)
            group_list.append(group)
            group_number += 1
        return cls(group_list, army_name)

    def __repr__(self):
        return "Army(name: {}, group count: {})".format(self.name, len(self.groups))


class Battle:
    def __init__(self, armies):
        self.armies = armies

    @classmethod
    def parseBattle(cls, battle_str, immune_boost=0):
        armies = [Army.parseArmy(army_str, immune_boost) for army_str in battle_str.split("\n\n")]
        return cls(armies)

    def fight(self):
        fighting = True
        while fighting:
            result = self.round()
            if result == "No deaths":
                return ("None", -1)
            for i, army in enumerate(self.armies):
                alive_count = sum([1 if group.alive_unit_count > 0 else 0 for group in army.groups])
                if alive_count == 0:
                    return army.name, sum([x.alive_unit_count for x in self.armies[0 if i == 1 else 1].groups])

    def round(self):
        fighting_groups = self._get_fighting_groups()
        attacks = self._select_targets(fighting_groups)
        return self._attack(fighting_groups, attacks)

    def _get_fighting_groups(self):
        fighting_groups = []
        for army in self.armies:
            for group in army.groups:
                if group.alive_unit_count > 0:
                    fighting_groups.append(group)
        fighting_groups.sort(key=lambda x: x.initiative, reverse=True)
        fighting_groups.sort(key=lambda x: x.effective_power(), reverse=True)
        return fighting_groups

    def _select_targets(self, fighting_groups):
        remaining_targets = set(fighting_groups)
        attacks = {}
        for attacker in fighting_groups:
            best_targets = []
            best_dmg = 0
            for target in remaining_targets:
                if attacker.army_name != target.army_name:
                    dmg = attacker.calculate_dmg(target)
                    if dmg > best_dmg:
                        best_dmg = dmg
                        best_targets = [target]
                    elif dmg == best_dmg and dmg != 0:
                        best_targets.append(target)
            if len(best_targets) > 0:
                best_targets.sort(key=lambda x: x.initiative, reverse=True)
                best_targets.sort(key=lambda x: x.effective_power(), reverse=True)
                best_target = best_targets.pop(0)
                remaining_targets.remove(best_target)
                attacks[attacker.initiative] = (attacker, best_target)
        return attacks

    def _attack(self, fighting_groups, attacks):
        round_death_count = 0
        fighting_groups.sort(key=lambda x: x.initiative, reverse=True)
        for step in sorted(attacks.keys(), reverse=True):
            attack = attacks[step]
            attacker = attack[0]
            defender = attack[1]
            if attacker.alive_unit_count > 0:
                round_death_count += defender.take_dmg_from(attacker)
        if round_death_count == 0:
            return "No deaths"


def parta(txt):
    battle = Battle.parseBattle(txt)
    return battle.fight()[1]


def partb(s: str):
    boost = 1
    immune_wins = False
    while not immune_wins:
        battle = Battle.parseBattle(s, boost)
        loser, remaining = battle.fight()
        if loser == "Infection":
            break
        boost += 1
    return remaining


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
