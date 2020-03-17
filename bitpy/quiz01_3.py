def quiz03():
    students = [
        {
            "name": "Kim",
            "kor": 80,
            "eng": 90,
            "math": 80
        },
        {
            "name": "Lee",
            "kor": 90,
            "eng": 85,
            "math": 85
        }
    ]
    for stu in students :
        stu['total'] = stu["kor"] + stu["eng"] + stu["math"]
        stu['average'] = round((stu['total'] / 3),2)
        print("students:", stu)

    print(students)

if __name__ == "__main__":
    quiz03()