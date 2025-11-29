import random
import time

import rich
import rich.spinner
import rich.text
from rich.live import Live
from rich.table import Table


def rng_value() -> tuple[rich.text.Text, rich.text.Text]:
    value = random.random() * 100
    return rich.text.Text(f"{value:3.2f}"), rich.text.Text(
        "ERROR" if value < 50 else "SUCCESS",
        style="red" if value < 50 else "green",
    )


state = {i: (rich.spinner.Spinner("dots"), rng_value()) for i in range(20)}

table = Table(
    collapse_padding=True,
    pad_edge=False,
    show_header=False,
    box=None,
)
table.add_column("ID")
table.add_column("Spinner")
table.add_column("Value")
table.add_column("Status")
for i, s in state.items():
    table.add_row(str(i), s[0], *s[1])


with Live(table, refresh_per_second=60) as live:
    for _ in range(20):
        row = random.choice(state)
        new_values = rng_value()
        for i, v in enumerate(new_values):
            row[1][i].plain = v.plain
            row[1][i].style = "yellow"
        time.sleep(1)
