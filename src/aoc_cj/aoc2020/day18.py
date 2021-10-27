import collections
import functools
from operator import mul


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


def weird_math_a_helper(tokens):
    ans = None
    op = None
    while len(tokens) > 0:
        token = tokens.popleft()
        if token == ")":
            break
        elif token in ("*", "+"):
            op = token
        else:
            n = weird_math_a_helper(tokens) if token == "(" else token
            if ans is None:
                ans = n
            elif op == "+":
                ans += n
            elif op == "*":
                ans *= n
    return ans


def weird_math_a(problem):
    return weird_math_a_helper(collections.deque(tokenize(problem)))


def weird_math_b_helper(tokens):
    sums = []
    ans = None
    op = None
    while len(tokens) > 0:
        token = tokens.popleft()
        if token == ")":
            break
        elif token == "*":
            sums.append(ans)
            ans = None
            op = None
        elif token == "+":
            op = token
        else:
            n = weird_math_b_helper(tokens) if token == "(" else token
            if ans is None:
                ans = n
            elif op == "+":
                ans += n
    sums.append(ans)
    return functools.reduce(mul, sums, 1)


def weird_math_b(problem):
    return weird_math_b_helper(collections.deque(tokenize(problem)))


def parta(txt):
    return sum(weird_math_a(line) for line in txt.splitlines())


def partb(txt):
    return sum(weird_math_b(line) for line in txt.splitlines())


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
