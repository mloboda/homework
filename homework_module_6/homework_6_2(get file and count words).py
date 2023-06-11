import requests
import re
import wget


def get_file_by_requests(file_url):
    response = requests.get(file_url)

    if response.status_code == 200:
        word_count_bot = len(re.findall(r'\bbot\b', response.text.lower()))
        word_count_bots = len(re.findall(r'\bbots\b', response.text.lower()))
        return f'Number of words bot: {word_count_bot}\n' \
               f'Number of words bots: {word_count_bots}\n' \
               f'Total: {word_count_bot + word_count_bots}\n'
    else:
        return 'Error when receiving the file'


def get_file_by_wget(file_url):
    wget.download(file_url, out='robots.txt')

    word_count_bot = 0
    word_count_bots = 0

    with open('robots.txt', 'r') as file:
        for line in file:
            word_count_bot += len(re.findall(r'\bbot\b', line.lower()))
            word_count_bots += len(re.findall(r'\bbots\b', line.lower()))

    return f'Number of words bot: {word_count_bot}\n' \
           f'Number of words bots: {word_count_bots}\n' \
           f'Total: {word_count_bot + word_count_bots}'


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/robots.txt'

    print(f'Requests method: \n{get_file_by_requests(url)}')
    print(f'Wget method: \n{get_file_by_wget(url)}')
