import time
from tqdm import tqdm, trange
from . import parser

beer_datas = []

def get_beer_data(style_num, start_num):
    beer_datas = []
    beer_list = get_beer_list(style_num, start_num)    # 카테고리 번호 수정해서 실행

    for i, beers in tqdm(enumerate(beer_list)):
        b = get_beer_content(beers)
        beer_datas.append(b)

    return beer_datas

get_beer_data(32, 0)

print(beer_datas)








