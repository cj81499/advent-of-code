# This code looks like garbage so I'm explaining it here

```python
step_size = int(.085 * (g.size()**(.5)))
if step_size < 50:
    step_size = 1
```

I wanted to speed up the program by making points move by many steps (seconds) at a time, rather than iterating the 10274 times required for solving my sample input. This line of code allows me to DRAMATICALLY lower that to 36 (I think? My brain hurts and I may have counted wrong). There is probably a better equation for this, but this runs so much faster than my original solution, so I'm happy with it.

To try out my idea, I used code similar to this:

``` python
if g.size() > 100000000:
    step_size = 100
elif g.size() > 1000000:
    step_size = 10
else:
    step_size = 1
```

This worked, proving to me that my idea of moving by many seconds at a time would work. Using trial and error, I refined my idea by deleting zeros until it broke (very scientific, I know).

```python
if g.size() > 1000000:
    step_size = 100
elif g.size() > 10000:
    step_size = 10
else:
    step_size = 1
```

I graphed the points (1000000, 100) and (10000, 10) on desmos, and noticed they both roughly fell on the line ![equation](https://latex.codecogs.com/gif.latex?.1%5Csqrt%7B%5Cleft%28x%5Cright%29%7D). That equation would translate to:

```python
.1 * (g.size()**(.5))
```

In practice, .1 was too much, so I lowered it (using trial and error) and found that .085 worked for my input. 0.085 is probably increasable for more performance, but idk if it would work for all inputs. idk if 0.085 works for all inputs tbh.

The if statement makes the loop step by one second when it is close so that it doesn't overshoot the correct answer.
