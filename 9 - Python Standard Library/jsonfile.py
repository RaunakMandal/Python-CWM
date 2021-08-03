import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Test", "year": 2000},
#     {"id": 2, "title": "Test2", "year": 20001},
# ]

# data = json.dumps(movies)
# print(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
