from bs4 import BeautifulSoup
import requests

def main():
    page = requests.get(f'https://en.wikipedia.org/wiki/Computer_science')
    soup = BeautifulSoup(page.text, "html.parser")
    elements = soup.findAll('p')
    for element in elements:
        print(element)

if __name__  == '__main__':
    main()
