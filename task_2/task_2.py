import requests

from bs4 import BeautifulSoup as bs


URL = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'

def get_animals(soup, animals):
    next_url ='https://ru.wikipedia.org' + soup.find('div', id='mw-pages').find_all('a', {'title': 'Категория:Животные по алфавиту'})[1].get('href')

    #get all category group
    all_category_group = soup.find('div', {'class': 'mw-content-ltr'}).find('div', {'class': 'mw-category'}).find_all('div', {'class': 'mw-category-group'})

    for category in all_category_group:
        key = category.find('h3').text

        if key == 'A':
            return 0

        if animals.get(key) == None:
            animals[key] = []
            
        li = category.find('ul').find_all('li')

        for e in li:
            animals[key].append(e.find('a').get('title'))

    return next_url

animals = {}

if __name__ == '__main__':
    print('wait...')
    while URL:
        
        r = requests.get(URL)
        soup = bs(r.text, 'lxml')

        URL = get_animals(soup, animals)

    for k, v in animals.items():
        print(f'{k}: {len(v)}')
