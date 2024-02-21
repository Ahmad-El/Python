from wsgiref.simple_server import make_server
from urllib.parse import unquote
import json

species = {
    "Cyberman": "John Lumic",
    "Dalek": "Davros",
    "Judoon": "Shadow Proclamation Convention 15 Enforcer",
    "Human": "Leonardo da Vinci",
    "Ood": "Klineman Halpen",
    "Silence": "Tasha Lem",
    "Slitheen": "Coca-Cola salesman",
    "Sontaran": "General Staal",
    "Time Lord": "Rassilon",
    "Weeping Angel": "The Division Representative",
    "Zygon": "Broton",
}


def simple_app(environ, start_response):
    status = "404 Not Found"
    response = {"credentials": "Unknown"}
    try:
        query = unquote(environ["QUERY_STRING"]).strip().split("=")
        if query[0] == "species" and query[1] in species:
            response = {"credentials": species[query[1]]}
            status = "200 OK"
    except:
        pass
    headers = [("Content-type", "application/json; charset=utf-8")]
    start_response(status, headers)
    return [json.dumps(response, ensure_ascii=False).encode("utf-8")]


with make_server("127.0.0.1", 8888, simple_app) as httpd:
    print("Listening on port 8888....")
    httpd.serve_forever()
