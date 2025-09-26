import json
from pathlib import Path

movies = [
    {"id":1, "title":"Titamic", "year": 1999},
    {"id":2, "title":"Terminator", "year": 2000}
]

data = json.dumps(movies)
Path("movies.json").write_text(data)


#Read
Path("movies.json").read_text()
movies = json.loads(data)
print(movies)