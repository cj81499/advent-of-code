def is_valid_a(passport):
    lines = passport.splitlines()
    missing = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    for line in lines:
        pairs = line.split(" ")
        for pair in pairs:
            key, val = pair.split(":")
            if key in missing:
                missing.remove(key)
    return len(missing) == 0


def is_valid_b(passport):   # noqa: C901
    lines = passport.splitlines()
    missing = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    for line in lines:
        pairs = line.split(" ")
        for pair in pairs:
            key, val = pair.split(":")
            if key in missing:
                missing.remove(key)
                if key == "byr":
                    if len(val) != 4:
                        return False
                    if not (1920 <= int(val) <= 2002):
                        return False
                elif key == "iyr":
                    if len(val) != 4:
                        return False
                    if not (2010 <= int(val) <= 2020):
                        return False
                elif key == "eyr":
                    if len(val) != 4:
                        return False
                    if not (2020 <= int(val) <= 2030):
                        return False
                elif key == "hgt":
                    if val.endswith("cm"):
                        if not (150 <= int(val[:-2]) <= 193):
                            return False
                    elif val.endswith("in"):
                        if not (59 <= int(val[:-2]) <= 76):
                            return False
                    else:
                        return False
                elif key == "hcl":
                    if not val.startswith("#") or not len(val) == 7:
                        return False
                    for c in val[1:]:
                        if c not in "0123456789abcdef":
                            return False
                elif key == "ecl":
                    if val not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                        return False
                elif key == "pid":
                    if len(val) != 9 or not val.isnumeric():
                        return False
    return len(missing) == 0


def parta(txt):
    passports = txt.split("\n\n")
    return sum(is_valid_a(p) for p in passports)


def partb(txt):
    passports = txt.split("\n\n")
    return sum(is_valid_b(p) for p in passports)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
