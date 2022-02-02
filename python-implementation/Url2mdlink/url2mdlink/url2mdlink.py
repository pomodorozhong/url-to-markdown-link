import requests
from bs4 import BeautifulSoup


def transform(url):
    """Take a url and returns a markdown link of it."""
    description = __extracts_title(url)
    markdown = __markdownlize(description, url)
    return markdown


def __extracts_title(url):
    """Extracts the title from a url."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').text
    return title


def __markdownlize(title, url):
    """Puts everything in a markdown's manner."""
    markdown = f'[{title}]({url})'
    return markdown
