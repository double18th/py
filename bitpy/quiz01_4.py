def quiz04():
    lst_date = ['2018.01.02', '2018.01.03', '2018.01.04', '2018.01.05']
    lst_dow = ["화", "수", "목", "금"]
    lst_price = [2479.65, 2486.35, 2466.46, 2497.52]

    # kospi_price라는 이름의 빈 사전을 만들어 봅니다.
    kospi_price = dict()

    # dow, price 키값을 보유한 사전을 만들어 kospi_price 사전에 date를 키값으로 추가해 봅시다.
    # 예  {"dow": "화", "price": 2479.65}

    # 2018.01.02를 제외한 나머지 날짜에 price_diff 키를 추가하고 전날의 price와 현재 날짜의 price의 가격 차를 값으로 담아 봅시다.

    #2018.01.05일의 price_diff는 얼마입니까?
    # 코스피 프라이스의 price diff 를 구해야함...
    print("2018.01.05일의 price_diff:", kospi_price.get('2018.01.05'))

    # 이 기간 중 최고가와 최저가는 각각 얼마입니까?
    # 코스피 프라이스의 프라이스를 구해야함...
    print("최고가:", max(price))
    print("최저가:", min(price))





if __name__ == "__main__":
    quiz04()