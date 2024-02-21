<h3>Exercise 00</h3>
The main protocol used for interspace communication was called 'Protobuf 2.0'. The entries were
being sent over the transport called 'gRPC'.

As gRPC is a client-server communication framework, two components had to be implemented - 
'reporting_server.py' and 'reporting_client.py'. The server should provide a response-streaming
endpoint, where it receives a set of coordinates
and responds with a stream of Spaceship entries.

As this is currently a test environment, even though every Spaceship should still have all the 
parameters mentioned, they could be random.
 - Alignment is an enum
 - Name is a string
 - Length is a float
 - Class is an enum
 - Size is an integer
 - Armed status is a bool
 - Each officer on board should have first name, last name and rank as strings

The number of officers on board is a random number from 0 (for enemy ships only) to 10.

The workflow should go like this:
1) the server is started
2) the client is started given a set of coordinates in some chosen form, e.g.:
    
`~$ ./reporting_client.py 17 45 40.0409 −29 00 28.118`

An example given is galactic coordinates for [Sagittarius A\*](https://en.wikipedia.org/wiki/Sagittarius_A*)
3) these coordinates are sent to the server, and server responds with a random (1-10) number
  of Spaceships in a gRPC stream to the client
4) the client prints to standard output all the received ships as a set of serialized JSON
  strings, like:

  ```
  {
    "alignment": "Ally",
    "name": "Normandy",
    "class": "Corvette",
    "length": 216.3,
    "crew_size": 8,
    "armed": true,
    "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
  }
  {
    "alignment": "Enemy",
    "name": "Executor",
    "class": "Dreadnought",
    "length": 19000.0,
    "crew_size": 450,
    "armed": true,
    "officers": []
  }
  ```


<h3>Exercise 01</h3>

| Class       | Length     | Crew    | Can be armed? | Can be hostile? |
|-------------|------------|---------|---------------|-----------------|
| Corvette    | 80-250     | 4-10    | Yes           | Yes             |
| Frigate     | 300-600    | 10-15   | Yes           | No              |
| Cruiser     | 500-1000   | 15-30   | Yes           | Yes             |
| Destroyer   | 800-2000   | 50-80   | Yes           | No              |
| Carrier     | 1000-4000  | 120-250 | No            | Yes             |
| Dreadnought | 5000-20000 | 300-500 | Yes           | Yes             |

I decided to represent these limitations as Pydantic data types (see Reading section).

That way it will not just be easier to validate incoming data, but also serialization to JSON
becomes a lot easier. I decided to make another version of the client ('reporting_client_v2.py'),
which will work with the same server. But this time it should validate the stream of Spaceships 
using Pydantic and filter out those which have some parameters out of bounds, according to the 
table above. The rest should be printed exactly as in EX00.

<h3>Exercise 02</h3>
Now Ender's project will have to include 'reporting_client_v3.py' script which is responsible
for mapping incoming objects to a database via ORM.
So, the scan interface in version 3 should look like this:

`~$ ./reporting_client.py scan 17 45 40.0409 −29 00 28.118`

And listing of traitors would be

`~$ ./reporting_client.py list_traitors`

which should print a list of JSON strings with "traitors'" names:

```
{"first_name": "Lando", "last_name": "Calrissian", "rank": "Entrepreneur"}
{"first_name": "Red", "last_name": "Guy", "rank": "Impostor"}
```

<h2 id="chapter-vii" >Chapter VII</h2>
<h3 id="reading">Reading</h3>

[Protocol Buffers using Python](https://developers.google.com/protocol-buffers/docs/pythontutorial)
[gRPC using Python](https://grpc.io/docs/languages/python/basics/)
[Pydantic Models](https://pydantic-docs.helpmanual.io/usage/models/)
[SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
[Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

