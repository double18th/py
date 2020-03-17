def quiz02():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #리스트로부터 [4, 5, 6, 7]을 추출하여 slice 에 담아 봅시다.
    slice = lst[3:7]
    #slice의 순서를 뒤집어 봅시다.
    slice.reverse()
    # lst의 적절한 부분에 slice를 끼워 넣어 봅시다.
    lst[3:7] = slice
    print(lst)



if __name__ == "__main__":
    quiz02()
