import random
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

palindrome()
