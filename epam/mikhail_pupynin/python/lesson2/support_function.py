import random

def random_color():
    rgbl=["red","green","blue"]
    random.shuffle(rgbl)
    return rgbl[0]

def random_mark():
    mark = ["Icarus","Gas","Zil"]
    random.shuffle(mark)
    return mark[0]
