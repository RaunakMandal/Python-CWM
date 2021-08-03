from pathlib import Path

path = Path(r"9 - Python Standard Library\test")
print(path.iterdir())
for p in path.iterdir():
    print(p)
