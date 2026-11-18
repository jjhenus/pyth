import random
import math
def OK():
    word = input("Type a word ")


    if "ok" in word.lower():
        print("WOW")
        print(word[2:6])
    else:
        print("no")
        print("The answer is", len(word))

def AGE():
    
    age = int(input("Whats your age? "))
    newage = age * 2
    print(f"Your age is {newage}")
    
def guys():
    names = ["Peter", "Johannes", "Urs"]
    search = input("Letter youre searching for? ")
    newlist = [x for x in names if search in x] 
    newlist.sort()
    print(newlist)

def tdic():
    tsdic = {
        "Hoodie": "Balenciaga",
        "Pants": "Acne",
        "Shoes": "Jordans",
        "Value": 3000
    }
    print(tsdic)

def rndmnum():
    i = 0
    while i < 10:
        rndmlst = [x for x in str(random.randrange(0, 100, 1))]
        print(rndmlst)
        i = i + 1


def lop():
    i = 0
    amn = int(input("How many times? "))
    while i < amn:
        i = i + 1
        print(i)

def count_vowels():
    word = input("")
    print(word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u"))

def crosssum():
    number = list(input(""))
    i = 0
    x = 0
    print(len(number))
    while i < len(number):
        x = x + int(number[i])
        i = i + 1
    print(x)

def max():
    numbers = list(input(""))
    numbers.sort(reverse = True)
    print(numbers[0])

def palindrome():
    word = list(input(""))
    rword = word.copy()
    rword.reverse()
    if word == rword:
        print("YES")
    else:
        print("No")

def fizzbuzz():
    numbers = [100, 50, 65, 82, 23, 45]
    newlist = []
    for x in numbers:
        if x % 5 == 0 and x % 3 == 0:
            print("Yes")
            newlist.append("FizzBuzz")
        elif x % 5 == 0:
            print("No")
            newlist.append("Buzz")
        elif x % 3 == 0:
            newlist.append("Fizz")
        else:
            newlist.append(x)
    print(newlist)

def nodup():
    numbers = [1, 2, 2, 3, 1]
    nodupnum = []
    for x in numbers:
        if numbers.count(x) > 0:
            print("DUP")
        else:
            print("NODUP")
            nodupnum.append(x)
        print(nodupnum)

def sec():
    numbers = [100, 50, 65, 82, 23, 45, 65]
    nodupnum = []
    for x in numbers:
        if x in nodupnum:
            pass
        else:
            nodupnum.append(x)
    nodupnum.sort(reverse = True)
    print(nodupnum[1])

def indexsum():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    num = int(input(""))
    for x in range(len(numbers)):
        print(x)

def isprime():
    n = int(input(""))
    if n <= 1:
        print("No Prime")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print("No Prime")
                break
            print("Prime")
            break

def primesto():
    n = int(input(""))
    primelist = []
    for i in range(n):
        if i <= 1:
            prime = False
        if i == 2 or i == 3:
            prime = True
        else:
            prime = True
            for x in range(2, int(i*0.5) + 1):
                if i % x == 0:
                    prime = False
                    break

        if prime == True:
            primelist.append(i)

    print(primelist)

def nfib():
    n = int(input(""))
    print("")
    i = 1
    x = 1
    fiblist = []
    while n > 0:
        y = i + x 
        n = n - 1
        print(y)
        i = x + y 
        n = n - 1
        print(i)
        x = y + i 
        n = n - 1
        print(x)
        

def test():
    i = 1
    x = 1
    y = i + x
    print(y)


def compress():
    word = list(input(""))
    nodupl = []
    for x in word:
        if  x + str(word.count(x)) in nodupl:
            print("DUP")
        else:
            nodupl.append(x + str(word.count(x)))

    print(str("".join(nodupl)))

def valid_parentheses():
    check = list(input(""))
    olist = []
    for x in check:
        if x == "(":
            olist.append(1)
        if x == ")":
            olist.append(-1)
    print(olist)

    print(check)

valid_parentheses()
