import csv

with open("data/big-data-1_comments.csv","r",encoding="utf-8") as csvfile:
    #读取csv文件，返回的是迭代类型
    read = csv.reader(csvfile)
    alist = [];
    bdict = [];
    for i in read:
        alist.append(i[0])
    for a in alist[1:]:
        print(a)

