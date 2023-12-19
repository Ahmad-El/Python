from bs4 import BeautifulSoup, SoupStrainer
import json
import requests

DEFAULT = "https://en.wikipedia.org/wiki/Erd%C5%91s_number"
MAIN_URL = "https://en.wikipedia.org"


def parse_wiki_page(link, max_link=10):
    with requests.Session() as session:
        response = session.get(link)
    parse_only = SoupStrainer("div", id="bodyContent")
    soup = BeautifulSoup(response.content, features="lxml", parse_only=parse_only)
    links = soup.find_all("a", href=True)
    temp_dict = {}
    for link in links:
        relative_link = str(link.get("href"))
        if relative_link.startswith("/wiki/"):
            temp_dict[MAIN_URL + relative_link] = {}
            max_link -= 1
        if max_link <= 0:
            break
    return temp_dict


def go_to_depth(main_dict, depth=3, repeat_dict=None):
    if repeat_dict is None:
        repeat_dict = []
    if depth <= 0 or len(repeat_dict) >= 1000:
        return
    for link in main_dict:
        if link in repeat_dict:
            main_dict[link] = {}
        else:
            main_dict[link] = parse_wiki_page(link)
            repeat_dict.append(link)
        go_to_depth(main_dict[link], depth - 1)


def write_to_json(input_dict: dict):
    with open("output.json", "w") as file:
        json.dump(input_dict, file, indent=4)


def main():
    main_dict = {DEFAULT: {}}
    go_to_depth(main_dict, 4)
    write_to_json(main_dict)


if __name__ == "__main__":
    main()
