from bs4 import BeautifulSoup as bs
from crawler import crawl
import random
import time
import lxml.html

beer_list = []
beer_data = []


# 2
def get_beer_list(style_num, start_num):
    base_url = f"https://www.beeradvocate.com/beer/styles/{style_num}/?sort=revsD&start={start_num}"
    page_string = crawl(base_url)

    soup = bs(page_string, 'lxml')
    tds = soup.find('table').findAll('td', {'class': 'hr_bottom_light'})[:-3:2]

    if not tds:
        return beer_list

    else:
        for td in tds:
            link = td.find('a')
            if link:
                beer_list.append(link['href'])
            else:
                pass
    start_num += 50
    time.sleep(random.randint(1, 2))
    get_beer_list(start_num)

    return beer_list


def get_beer_content(url):
    base_url = f"http://beeradvocate.com{url}"
    page_string = crawl(base_url)
    soup = bs(page_string, 'lxml')

    titles = soup.find("div", {'class': 'titleBar'}).contents[1]
    title_span = titles.find('span').text
    title = titles.text.replace(title_span, "")

    stats = soup.findAll("dd", {'class': 'beerstats'})
    note = soup.select("#ba-content > div:nth-child(8) > div:nth-child(3)")[0].text
    note2 = note.split(":")[-1].strip()

    beer_data = {"beerName": title, "type": stats[0].select('b')[0].text,
                "country": stats[7].text.split(', ')[-1], "company": stats[6].text,
                "ABV": stats[1].text.split('%')[0], "ratingBA": stats[3].text.split(' ')[0]}

    time.sleep(random.randint(1, 2))

    return beer_data



if __name__ == "__main__":
    get_beer_list()