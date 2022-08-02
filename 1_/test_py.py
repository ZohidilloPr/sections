import datetime
# for i in range(10-1):
#     print(i)
sinf = []
b_year = int(input("Kirgan yili: "))
j_year = datetime.datetime.now().year

if b_year < j_year:
    for i in range((j_year - b_year) - 1):
        sinf.append(1)
    print(sinf)
else:
    print(sinf)
