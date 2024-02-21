import json
from urllib.parse import unquote
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

FILE = os.environ.get("WIKI_FILE")


def read_file():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        print(f"The file {FILE} does not exist.")
        return {}


class Algorithm:
    path_start = [""] * 20

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.answer = []
        self.start_exists = False
        self.end_exists = False

    def check_for_endpoint(self, data):
        if self.start_exists and self.end_exists:
            return True
        for key in data:
            link = key.split("/")[-1]
            link = unquote(link)
            if link == self.start:
                self.start_exists = 1

            if link == self.end:
                self.end_exists = 1
            if self.check_for_endpoint(data[key]):
                return True
        return False

    def pass_throw_data(self, data, search_link, found_links=[]):
        for key in data:
            link = key.split("/")[-1]
            link = unquote(link)
            if link == search_link:
                found_links += self.get_links(data[key])
            self.pass_throw_data(data[key], search_link, found_links)
        return found_links

    def get_links(self, data):
        temp = []
        for link in data:
            link = link.split("/")[-1]
            link = unquote(link)
            temp.append(link)
        return temp

    def recursively_search(self, data, start):
        if start in self.answer:
            return -1
        temp = self.pass_throw_data(data, start, [])
        self.answer.append(start)
        if start == self.end:
            return 1

        for key in temp:
            code = self.recursively_search(data, key)
            if code == -1:
                continue
            elif code == 0:
                self.answer.pop()
            elif code == 1:
                return 1
        return 0


def parse_arguments():
    parser = argparse.ArgumentParser(description="Wikipedia find path")
    parser.add_argument("--from_path", "--from", help="from wiki page")
    parser.add_argument("--to_path", "--to", help="to wiki page")
    parser.add_argument("--non_directed", action="store_true", help="reverse looking")
    parser.add_argument("--graph", "-v", action="store_true")
    args = parser.parse_args()
    return args


def print_answer(links: list):
    print(f"'{links[0]}'", end="")
    for link in links[1:]:
        print(f" -> '{link}'", end="")
    print()


def main():
    args = parse_arguments()
    start = args.from_path
    end = args.to_path
    print(start)
    print(end)
    bidirect = args.non_directed
    graph = args.graph
    json_data = read_file()
    if len(json_data) == 0:
        return

    answer = []
    algorithm = Algorithm(start, end)

    if algorithm.check_for_endpoint(json_data) is False:
        print("Endpoints doesn't exist!")
        return

    algorithm.recursively_search(json_data, start)
    answer = algorithm.answer

    if len(answer) < 2 and bidirect:
        algorithm = Algorithm(end, start)
        algorithm.recursively_search(json_data, end)
        answer = algorithm.answer

    if len(answer) < 2:
        print("They don't connect with each other!")
    else:
        if graph:
            print_answer(answer)
        print(len(answer) - 1)


if __name__ == "__main__":
    main()


# Some useful clues for start code
# start = "link3"
# end = "link7"
# start = "Welsh_Corgi"
# end = "Pembrokeshire"
# end = 'Carmarthenshire'
# to Carmarthenshire

# python ex01/shortest_path.py --from 'Erdős_number' --to 'Hungarian_language' -v
