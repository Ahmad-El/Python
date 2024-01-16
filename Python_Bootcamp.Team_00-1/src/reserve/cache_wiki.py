from bs4 import BeautifulSoup, SoupStrainer
import json
import requests
# import networkx as nx
# import nx_altair as nxa


DEFAULT = "https://en.wikipedia.org/wiki/Erd%C5%91s_number"
MAIN_URL = "https://en.wikipedia.org"


class WikiParser:
    def __init__(self, depth=3, max_size=1000, url=None):
        self.total_link = max_size
        self.max_link = 3
        self.depth = depth
        self.cnt = 0
        if url is None:
            self.url = "https://en.wikipedia.org/wiki/Erd%C5%91s_number"
        else:
            self.url = url
        self.main_dict = {self.url: {}}

    def parse_wiki_page(self, link):
        link_cnt = 0
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
                link_cnt += 1
                self.cnt += 1
            if link_cnt == self.max_link:
                break
        return temp_dict

    def go_to_depth(self, current_depth=0, temp_dict=None):
        if temp_dict is None:
            temp_dict: dict = self.main_dict

        if current_depth >= self.depth or self.cnt >= self.total_link:
            return

        repeat_dict = []
        for link in temp_dict:
            if self.cnt >= self.total_link:
                break
            if link in repeat_dict:
                temp_dict[link] = {}
            else:
                temp_dict[link] = self.parse_wiki_page(link)
                repeat_dict.append(link)
            self.go_to_depth(current_depth+1, temp_dict[link])

    def write_to_json(self):
        with open("output.json", "w") as file:
            json.dump(self.main_dict, file, indent=4)
            # self.json_data = json.dumps(self.main_dict)


    def load_json(self):
        with open("output.json", "r") as file:
            json_data = json.load(file)
        return json_data

    def get_data(self, json_data):
        for key in json_data:
            node = key
            values = list(json_data[key])
            print(node)
            print(values)
            self.get_data(json_data[key])

def main():
    parser = WikiParser(depth=3, max_size=30)
    parser.go_to_depth()
    parser.write_to_json()
    # json_data = parser.load_json()
    # print(json_data)
    # parser.get_data(json_data)

if __name__ == "__main__":
    main()


temp1 
     temp2 
        temp1 
            temp2
            temp3
            temp4
     temp3 
     temp4 