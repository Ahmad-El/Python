# import wikipediaapi
# wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

# page_py = wiki_wiki.page('Python_(programming_language)')
import argparse
import json
import wikipediaapi

def get_links(page):
    """Get links from the main text and 'See also' section of a Wikipedia page."""
    links = set()

    # Extract links from the main text
    for section in page.sections:
        links.update(get_links_from_text(section.text))

    # Extract links from the 'See also' section
    if 'See also' in page.sections_by_title:
        see_also_section = page.sections_by_title['See also']
        links.update(get_links_from_text(see_also_section.text))

    return links

def get_links_from_text(text):
    """Extract links from the text of a Wikipedia section."""
    links = set()

    # Wikipedia links are enclosed in double square brackets, e.g., [[Link]]
    link_start = text.find('[[')
    while link_start != -1:
        link_end = text.find(']]', link_start)
        if link_end != -1:
            link = text[link_start + 2:link_end].split('|')[0]
            links.add(link)
            link_start = text.find('[[', link_end)
        else:
            break

    return links

def create_wiki_graph(start_page, max_depth=1):
    """Create a directed graph representation of Wikipedia links."""
    wiki_wiki = wikipediaapi.Wikipedia('en')
    visited_pages = set()
    graph = {'vertices': set(), 'edges': []}

    def dfs(current_page, depth):
        if depth > max_depth or current_page.title in visited_pages:
            return

        visited_pages.add(current_page.title)
        current_links = get_links(current_page)

        # Add vertices
        graph['vertices'].update([current_page.title] + list(current_links))

        # Add edges
        graph['edges'].extend([(current_page.title, link) for link in current_links])

        # Recursively explore linked pages
        for link in current_links:
            linked_page = wiki_wiki.page(link)
            dfs(linked_page, depth + 1)

    start_page_obj = wiki_wiki.page(start_page)
    dfs(start_page_obj, depth=0)

    return graph

def save_graph_to_json(graph, output_file='wiki.json'):
    """Save the graph to a JSON file."""
    with open(output_file, 'w') as json_file:
        json.dump(graph, json_file, indent=2)

def main():
    parser = argparse.ArgumentParser(description='Cache Wikipedia links as a directed graph.')
    parser.add_argument('-p', '--page', default='Harry_Potter', help='Wikipedia page to start parsing from')
    parser.add_argument('-d', '--depth', type=int, default=1, help='Maximum depth for graph traversal')
    args = parser.parse_args()

    start_page = args.page.replace(' ', '_')  # Handle spaces in page names

    graph = create_wiki_graph(start_page, max_depth=args.depth)
    save_graph_to_json(graph)

if __name__ == '__main__':
    main()
