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

def common_el():
    alist = [1, 2, 3, 4]
    blist = [3, 4, 5]
    clist = []
    for x in alist:
        if x in blist:
            clist.append(x)
    print(clist)

def longest_word():
    sent = input("")
    slist = sent.rsplit(" ")
    llist = []
    n = 0
    for x in slist:
        llist.append(len(x))
    for x in llist:
        if x > n:
            n = x
    print(slist[llist.index(n)])

def rotate():
    nums = [1, 2, 3, 4, 5]
    lnums = []
    k = int(input(""))
    n = len(nums) - 1
    for x in nums:
        if k > 0:
            id = nums[n]
            lnums.append(id)
            n = n - 1
            k = k - 1
            print(lnums)
    lnums.reverse()
    lnums.extend(nums)
    print(lnums)

def first_unique():
    word = list(input(""))
    for x in word:
        n = word.count(x)
        if n == 1:
            print(x)
            break

def mis_num():
    nums = [0, 1, 3, 4]
    n = 0
    for x in nums:
        if not x == n:
            print("NO " + str(x) + " should be: " + str(n))
            break
        else:
            print(str(x) + " = " + str(n))
        n = n + 1
        
mis_num()
