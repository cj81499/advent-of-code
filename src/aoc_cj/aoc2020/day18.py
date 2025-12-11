import collections
import functools
import operator


def tokenize(s: str):
    tokens = []
    words = s.strip().split()
    for word in words:
        if word.startswith("("):
            tokens.append(word[0])
            tokens.extend(tokenize(word[1:]))
        elif word.endswith(")"):
            tokens.extend(tokenize(word[:-1]))
            tokens.append(word[-1])
        elif word in "+*":
            tokens.append(word)
        else:
            tokens.append(int(word))
    return tokens


def weird_math_1_helper(tokens):
    ans = None
    op = None
    while len(tokens) > 0:
        token = tokens.popleft()
        if token == ")":
            break
        if token in ("*", "+"):
            op = token
        else:
            n = weird_math_1_helper(tokens) if token == "(" else token
            if ans is None:
                ans = n
            elif op == "+":
                ans += n
            elif op == "*":
                ans *= n
    return ans


def weird_math_1(problem):
    return weird_math_1_helper(collections.deque(tokenize(problem)))


def weird_math_2_helper(tokens):
    sums = []
    ans = None
    op = None
    while len(tokens) > 0:
        token = tokens.popleft()
        if token == ")":
            break
        if token == "*":
            sums.append(ans)
            ans = None
            op = None
        elif token == "+":
            op = token
        else:
            n = weird_math_2_helper(tokens) if token == "(" else token
            if ans is None:
                ans = n
            elif op == "+":
                ans += n
    sums.append(ans)
    return functools.reduce(operator.mul, sums, 1)


def weird_math_2(problem):
    return weird_math_2_helper(collections.deque(tokenize(problem)))


def part_1(txt: str) -> int:
    return sum(weird_math_1(line) for line in txt.splitlines())


def part_2(txt: str) -> int:
    return sum(weird_math_2(line) for line in txt.splitlines())


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
