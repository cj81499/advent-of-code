from pathlib import Path

cwd = Path()

for file in cwd.glob("test*.py"):
    file: Path = file
    print(file)
    file.rename(f"day{file.name[-5:-3]}_test.py")
