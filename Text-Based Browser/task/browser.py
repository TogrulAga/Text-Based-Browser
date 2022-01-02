from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore
import colorama
import argparse
import os


class WebBrowser:
    def __init__(self, directory):
        self.directory = os.path.join(os.getcwd(), directory)
        self.page_stack = deque()
        self.make_dir()
        self.run()

    def make_dir(self):
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)

    def run(self):
        while True:
            url = input()
            if url == "exit":
                break
            elif url == "back":
                url = self.get_back()
                with open(os.path.join(self.directory, ".".join(url.split(".")[:-1])), "r", encoding="utf-8") as page:
                    print(page.read())
                continue
            elif url in os.listdir(self.directory):
                print(self.load_page(url))
                continue
            elif "." not in url:
                print("Error: Incorrect URL")
                continue

            if "https://" in url:
                response = requests.get(url)
            else:
                response = requests.get("https://" + url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                colorized = self.color_refs(response.content, soup)

                self.save_page(url, colorized)
                content = self.load_page(url)
                self.page_stack.append(content)
                print(content)

            else:
                print("Error: Incorrect URL")

    def save_page(self, url, page):
        with open(os.path.join(self.directory, url.split(".")[0]), "w", encoding="utf-8") as file:
            file.write(page)

    def load_page(self, url):
        with open(os.path.join(self.directory, url.split(".")[0]), "r", encoding="utf-8") as page:
            content = ""
            for line in page.readlines():
                if line != "\n":
                    content += line
        return content

    def get_back(self):
        # _ = self.page_stack.pop()
        return self.page_stack.pop()

    def color_refs(self, content, soup):
        content = ""
        all_tags = soup.find_all(["div", "p", "a", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li"])
        for tag in all_tags:
            if tag.string:
                if tag.name == "a":
                    content += Fore.BLUE + tag.string + "\n"

        return content


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")
    args = parser.parse_args()
    colorama.init(autoreset=True)
    _ = WebBrowser(args.dir)
