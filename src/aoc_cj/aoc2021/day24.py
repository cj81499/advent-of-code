# https://github.com/dphilipson/advent-of-code-2021/blob/master/src/days/day24.rs
z = 0

w = input()
z *= 26  # push
z += w + 6

w = input()
z *= 26  # push
z += w + 12

w = input()
z *= 26  # push
z += w + 5

w = input()
z *= 26  # push
z += w + 10

w = input()
x = 0 if (z % 26) - 16 == w else 1
z //= 26  # pop
z *= (25 * x) + 1  # push if x == 1
z += (w + 7) * x

w = input()
z *= 26  # push
z += w + 0

w = input()
z *= 26  # push
z += w + 4

w = input()
x = 0 if (z % 26) - 4 == w else 1
z //= 26  # pop
z *= (25 * x) + 1  # push if x == 1
z += (w + 12) * x

w = input()
z *= 26  # push
z += w + 14

w = input()
x = 0 if (z % 26) - 7 == w else 1
z //= 26  # pop
z *= (25 * x) + 1  # push if x == 1
z += (w + 13) * x

w = input()
x = 0 if (z % 26) - 8 == w else 1
z //= 26  # pop
z *= (25 * x) + 1  # push if x == 1
z += (w + 10) * x

w = input()
x = 0 if (z % 26) - 4 == w else 1
z //= 26  # pop
z *= (25 * x) + 1  # push if x == 1
z += (w + 11) * x

w = input()
x = 0 if (z % 26) - 15 == w else 1
z //= 26  # pop
z *= (25 * x) + 1  # push if x == 1
z += (w + 9) * x

w = input()
x = 0 if (z % 26) - 8 == w else 1
z //= 26  # pop
z *= (25 * x) + 1  # push if x == 1
z += (w + 9) * x
