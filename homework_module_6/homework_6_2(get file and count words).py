import requests
import re
import wget

url = 'https://en.wikipedia.org/robots.txt'

print('Requests method')
response = requests.get(url)

if response.status_code == 200:
    word_count_bot = len(re.findall(r'\bbot\b', response.text.lower()))
    word_count_bots = len(re.findall(r'\bbots\b', response.text.lower()))
    print(f'Number of words bot: {word_count_bot}\n'
          f'Number of words bots: {word_count_bots}\n'
          f'Total: {word_count_bot + word_count_bots}\n')
else:
    print('Error when receiving the file')


print('Wget method')
wget.download(url, out='robots.txt')

word_count_bot = 0
word_count_bots = 0

with open('robots.txt', 'r') as file:
    for line in file:
        word_count_bot += len(re.findall(r'\bbot\b', line.lower()))
        word_count_bots += len(re.findall(r'\bbots\b', line.lower()))

print(f'Number of words bot: {word_count_bot}\n'
      f'Number of words bots: {word_count_bots}\n'
      f'Total: {word_count_bot + word_count_bots}')
