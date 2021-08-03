from pathlib import Path

path = Path("hello.txt")
# print(path.exists())
# path.rename("hello.cpp")
# path.unlink()
# print(path.read_text())

# with open("hello.txt", "r") as file:
#     # do something
path.write_text("Hemlo")
print(path.read_text())
