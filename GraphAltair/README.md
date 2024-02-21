When it is run like this:

`~$ python cache_wiki.py -p 'Erdős number'`

it should start parsing from [this page](https://en.wikipedia.org/wiki/Erd%C5%91s_number).

The goal is to keep following links (only those leading to other Wikipedia pages, NOT to the
outside internet) going *at least three pages deep* down every link. This parameter should be
configurable using `-d`, so default value will be `3`. But if the result is too large (>1000 pages)
your code should stop processing links. If it is too small (<20 pages) then please choose some
other default starting page. Don't forget to keep track of the links leading to the pages you've
already visited. If page A links to page B and page B links to page A - it is two directed graph
edges, not one.

Every page visits logged to stdout using `logging` Python module with log 
level setted  to 'INFO'. 

`~$ python shortest_path.py --from 'Welsh Corgi' --to 'Solomon'`

3

`~$ python shortest_path.py --from 'Solomon' --to 'Welsh Corgi' --non-directed`

3
```

Mind the `--non-directed` flag. It means we treat all links as "non-directed" or "bidirected", so
every edge is treated equally in both directions. In this case, a path exists betweeh *any* two
nodes in your serialized graph.

By default (when `--non-directed` is not specified) we are only following the directed edges of 
the graph. This means, not all pages in the database can be reachable from other pages, especially 
if they  have a small amount of inbound links. If the path doesn't exist, your script should print
'Path not found'.
```
~$ python shortest_path.py -v --from 'Welsh Corgi' --to 'Solomon'

'Welsh Corgi' -> 'Dog training' -> 'King Solomon's Ring (book)' -> 'Solomon'

3
```

Used library [Altair](https://altair-viz.github.io/) 
to generate graph in `.png` and `.html`.

