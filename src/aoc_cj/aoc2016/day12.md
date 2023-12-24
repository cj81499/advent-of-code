# Day 12

| assembunny | translate             | interpret gotos  | simplify             |
| ---------- | --------------------- | ---------------- | -------------------- |
| cpy 1 a    | a = 1                 | a = 1            | a = 1                |
| cpy 1 b    | b = 1                 | b = 1            | b = 1                |
| cpy 26 d   | d = 26                | d = 26           | d = 26               |
| jnz c 2    | goto label1 if c != 0 | if (c != 0) {    | if (part_2) {        |
| jnz 1 5    | goto label2           |                  |                      |
| cpy 7 c    | label1: c = 7         | c = 7            |                      |
| inc d      | label3: d++           | while (c != 0) { |                      |
|            |                       | d++              | d += 7               |
| dec c      | c--                   | c--              |                      |
| jnz c -2   | goto label3 if c != 0 | }                |                      |
|            |                       | }                | }                    |
| cpy a c    | label2: c = a         | while (d != 0) { | for \_ in range(d) { |
|            |                       | c = a            | c = a                |
| inc a      | label4: a++           | while (b != 0) { |                      |
|            |                       | a++              | a += b               |
| dec b      | b--                   | b--              |                      |
| jnz b -2   | goto label4 if b != 0 | }                |                      |
| cpy c b    | b = c                 | b = c            | b = c                |
| dec d      | d--                   | d--              |                      |
| jnz d -6   | goto label2 if d != 0 | }                | }                    |
| cpy 19 c   | c = 19                | c = 19           | a += 14 \* 19        |
| cpy 14 d   | label6: d = 14        | while (c != 0) { |                      |
|            |                       | d = 14           |                      |
| inc a      | label5: a++           | while (d != 0) { |                      |
|            |                       | a++              |                      |
| dec d      | d--                   | d--              |                      |
| jnz d -2   | goto label5 if d != 0 | }                |                      |
| dec c      | c--                   | c--              |                      |
| jnz c -5   | goto label6 if c != 0 | }                |                      |
