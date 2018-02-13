import requests
from bs4 import BeautifulSoup as bs


def get_urls():
    page = 1
    result = []
    base = 'http://www.influenster.com'
    while True:

        url = 'http://www.influenster.com/reviews/beauty'
        params = {
            'page': page,
        }
        response = requests.get(url=url, params=params)
        soup = bs(response.text, 'lxml')
        raw_a_list = soup.findAll('a', class_='category-product')
        for i in raw_a_list:
            result.append(base + i.get('href'))
            print(base + i.get('href'))
        if page == 10:
            break
        page += 1

    # print(result)


if __name__ == '__main__':
    get_urls()
