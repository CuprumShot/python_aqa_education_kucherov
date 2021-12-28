"""Text browser task"""

import requests

from os import mkdir
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore


class TextBrowser:
    def __init__(self, directory):
        self.directory = directory
        self.tabs = {}
        self.cached_page = deque()
        try:
            mkdir(self.directory)
        except FileExistsError:
            pass

    def open_url(self, url):
        with open(self.tabs[url]) as tab:
            return tab.read()

    def cache_site(self, name, content):
        # create cache file
        namesList = name.split('.')
        if len(namesList) > 1 and not self.tabs.get(namesList[1]):
            with open(f'{self.directory}/{namesList[0]}.txt', 'w') as tab:
                tab.write(content)
            self.tabs[namesList[0]] = f'{self.directory}/{namesList[0]}.txt'
            self.cached_page.append(self.tabs[namesList[0]])

    @staticmethod
    def get_tags_content(content):
        # parsing page without html tags
        tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        soup = BeautifulSoup(content, 'html.parser').body.descendants
        page = ''
        for objects in soup:
            if objects.name in tags:
                if objects.name == 'a':
                    page += Fore.BLUE + objects.get_text().strip() + '\n'
                else:
                    page += Fore.RESET + objects.get_text().strip() + '\n'
        return page + Fore.RESET

    def check_url(self, url):
        # check for the http inputting
        try:
            if url.startswith('http'):
                return self.request(url)
            return self.request(f'https://{url}')
        except requests.exceptions.RequestException:
            return 'Lost the connection or request is wrong.\n'

    def request(self, url):
        # request the page
        request = requests.get(url)
        final_page = self.get_tags_content(request.content)
        self.cache_site(url.lstrip('https://'), final_page)
        return final_page

    def back_menu(self):
        # functional for the input the 'back' request
        if len(self.cached_page) == 1:
            return 'The history is empty.\n'
        try:
            with open(self.cached_page.pop()) as cached:
                return cached.read()
        except FileNotFoundError:
            return 'File with history not found, sorry.\n'
        except IndexError:
            return 'There are no any requests in your history.\n'


def main_menu(folder='history'):
    # main menu functional
    browser = TextBrowser(folder)
    while True:
        url = input('''Please, input URL for the site parsing,
\'back\' for the open previous page,
\'exit\' for exit the program:\n> ''')
        if '.' in url:
            print(browser.check_url(url))
        elif url in browser.tabs:
            print(browser.open_url(url))
        elif url == 'back':
            print(browser.back_menu())
        elif url == 'exit':
            break
        else:
            print('Oops! Something went wrong! Probably, you should input correctly request.')


if __name__ == '__main__':
    main_menu()
