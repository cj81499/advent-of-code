# Day 23

| assembunny | translate           | interpret gotos     | simplify            |
| ---------- | ------------------- | ------------------- | ------------------- |
|            | a = part_1 ? 7 : 12 | a = part_1 ? 7 : 12 | a = part_1 ? 7 : 12 |
| cpy a b    | b = a               | b = a               |                     |
| dec b      | b -= 1              | b -= 1              | b = a - 1           |
| cpy a d    | d = a               | d = a               | d = a               |
| cpy 0 a    | a = 0               | a = 0               | a = 0               |
|            |                     | while (d != 0) {    |
| cpy b c    | c = b               | c = b               |
|            |                     | while (c != 0) {    |
| inc a      | a += 1              | a += 1              |
| dec c      | c -= 1              | c -= 1              |
| jnz c -2   | goto -2 if c != 0   | }                   |
| dec d      | d -= 1              | d -= 1              |
| jnz d -5   | goto -5 if d != 0   | }                   |
| dec b      | b -= 1              | b -= 1              |
| cpy b c    | c = b               | c = b               |
| cpy c d    | d = c               | d = c               |
|            |                     | while (d != 0) {    |
| dec d      | d -= 1              | d -= 1              |
| inc c      | c += 1              | c += 1              |
| jnz d -2   | goto -2 if d != 0   | }                   |
| tgl c      | toggle c            | toggle c            |
| cpy -16 c  | c = -16             | c = -16             |
| jnz 1 c    | goto c if 1 != 0    | ??????????????????? |
| cpy 96 c   | c = 96              | c= 96               |
|            |                     | while (c != 0) {    |
| jnz 79 d   | goto d if 79 != 0   | ??????????????????? |
|            |                     | while (d != 0) {    |
| inc a      | a += 1              | a += 1              |
| inc d      | d += 1              | d += 1              |
| jnz d -2   | goto -2 if d != 0   | }                   |
| inc c      | c += 1              | c += 1              |
| jnz c -5   | goto -5 if c != 0   | }                   |
