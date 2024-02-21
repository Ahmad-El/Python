from bs4 import BeautifulSoup, SoupStrainer
import json
import requests
import logging
import argparse
import urllib.parse

DEFAULT = "https://en.wikipedia.org/wiki/Erd%C5%91s_number"
MAIN_URL = "https://en.wikipedia.org"
logging.basicConfig(level=logging.INFO)


class WikiParser:
    def __init__(self, url, depth=3, max_size=1000):
        self.max_link_per_page = 20
        self.total_link = max_size
        self.depth = depth
        self.url = url
        self.main_dict = {self.url: {}}
        self.data_base = []

    def parse_wiki_page(self, link):
        logging.info(urllib.parse.unquote(link))
        with requests.Session() as session:
            response = session.get(link)
        parse_only = SoupStrainer("div", id="bodyContent")
        soup = BeautifulSoup(response.content, features="lxml", parse_only=parse_only)
        links = soup.find_all("a", href=True)
        links = [
            link
            for link in links
            if not link["href"]
            .lower()
            .endswith((".svg", ".png", ".jpg", ".jpeg", ".css"))
            and link["href"].find(":") == -1
        ]
        for link in links:
            relative_link = str(link.get("href"))
            if relative_link.startswith("/wiki/"):
                yield MAIN_URL + relative_link

    def dict_to_json(self, data_dict):
        with open("wiki.json", "w") as file:
            json.dump(data_dict, file, indent=4)

    def go_to_depth(self, parse_link, current_depth=0, temp_dict={}):
        current_depth += 1
        if self.total_link <= 0 or current_depth > self.depth:
            return
        generator = self.parse_wiki_page(parse_link)
        for link in generator:
            if self.total_link <= 0:
                generator.close()
                break
            if link in temp_dict:
                continue
            temp_dict[link] = {}
            self.total_link -= 1
            if link not in self.data_base:
                self.go_to_depth(link, current_depth, temp_dict=temp_dict[link])
                if current_depth < self.depth:
                    self.data_base.append(link)
            if len(temp_dict) >= self.max_link_per_page:
                generator.close()

    def print_result(self):
        print(self.main_dict)

    def write_to_json(self):
        with open("wiki.json", "w") as file:
            json.dump(self.main_dict, file, indent=4)


def valid_number(value):
    ivalue = int(value)
    if 3 <= ivalue <= 20:
        return ivalue
    else:
        return None


def parse_arguments():
    parser = argparse.ArgumentParser(description="Wikipedia article")
    parser.add_argument("--article_link", "-p", help="wikipedia relative page link")
    parser.add_argument("--max_depth", "-d", type=valid_number, help="max depth number")
    args = parser.parse_args()
    if args.max_depth is None:
        args.max_depth = 3
    if args.article_link is None:
        args.article_link = DEFAULT
    else:
        link = MAIN_URL + "/wiki/" + args.article_link
        responce = requests.get(link)
        if responce.status_code == 200:
            args.article_link = link
        else:
            args.article_link = DEFAULT
    return args


def main():
    args = parse_arguments()
    print(args)
    parse = WikiParser(url=args.article_link, depth=int(args.max_depth))
    parse.go_to_depth(args.article_link, temp_dict=parse.main_dict[args.article_link])
    parse.write_to_json()


if __name__ == "__main__":
    main()
