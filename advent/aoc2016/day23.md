# Day 23

| assembunny | translate             | interpret gotos      | simplify |
| ---------- | --------------------- | -------------------- | -------- |
| cpy a b    | b = a                 | b = 7 (or 12)        |
| dec b      | label6: b--           | while (true) {       |
|            |                       | b = 6 (or 11)        |
| cpy a d    | d = a                 | d = 7 (or 12)        |
| cpy 0 a    | a = 0                 | a = 0                |
| cpy b c    | label2: c = b         | while (d != 0) {     |
|            |                       | c = b                |
| inc a      | label1: a++           | while (c != 0) {     |
|            |                       | a++                  |
| dec c      | c--                   | c--                  |
| jnz c -2   | goto label1 if c != 0 | }                    |
| dec d      | d--                   | d--                  |
| jnz d -5   | goto label2 if d != 0 | }                    |
| dec b      | b--                   | b--                  |
| cpy b c    | c = b                 | c = b                |
| cpy c d    | d = c                 | d = c                |
| dec d      | label3: d--           | while (d != 0) {     |
|            |                       | d--                  |
| inc c      | c++                   | c++                  |
| jnz d -2   | goto label3 if d != 0 | }                    |
| tgl c      | tgl c                 | tgl c å              |
| cpy -16 c  | c = -16               | c = -16              |
| jnz 1 c    | goto c                | } // assume c == -16 |
| cpy 96 c   | c = 96                |
| jnz 79 d   | label5: goto d        |
| inc a      | label4: a++           |
| inc d      | d++                   |
| jnz d -2   | goto label4 if d != 0 |
| inc c      | c++                   |
| jnz c -5   | goto label5 if c != 0 |
