from pathlib import Path

# Path(r"C:\Program Files\Microsoft")  # absolute path -> r is raw string to get rid of \\
# Path()  # current path
# Path("file_in_current")  # can be used in current
# Path() / "folder"
path = Path(r"9 - Python Standard Library\test")
path.exists()
path.is_file()
path.is_dir()

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path.absolute())
