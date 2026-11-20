def count_words():
    sent = input("")
    lsent = sent.rsplit(" ")
    print(len(lsent))

def factorial():
    num = int(input(""))
    x = 0
    n = 0
    while n < num:
        x = x + n
        n = n + 1
    print(x)

def count_even():
    numbs = [1, 2, 4, 7]
    for x in numbs:
        if x % 2 == 0:
            print("Yes")
        else:
            print("No")

def cap_words():
    words = input("")
    lwords = words.rsplit(" ")
    bwords = []
    for x in lwords:
        bwords.append(x.capitalize())
    print(" ".join(bwords))

cap_words()
