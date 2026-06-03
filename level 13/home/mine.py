# დავალება:
# დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს მის კვადრატს.
num = 5
print(num ** 2)

# დავალება:
# დაწერე ფუნქცია, რომელიც იღებს სამ რიცხვს და აბრუნებს მათ საშუალოს.
num1 = 10
num2 = 20
num3 = 100
sashvalo = num1 + num2 + num3 / 3
print(sashvalo)

# დავალება:
# დაწერე ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს True - ს თუ რიცხვი დადებითია, სხვა შემთხვევაში False - ს.
num = 1
if num >= 0:
    print("True")
else:
    print("False")

# დავალება:
# დაწერე ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის გაორმაგებულ მნიშვნელობას.
num = 5
print(num * 2)

# დავალება:
# დაწერე ფუნქცია, რომელიც აბრუნებს ორი რიცხვის ჯამს.
# თუ მომხმარებელი არ შემოიტანს მეორე რიცხვს, მაშინ მისი მნიშვნელობა იყოს 10
def num(num1 , num2 = 10):
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    print(num1 + num2)
num()

# დავალება:
# დაწერე ფუნქცია, რომელიც ბეჭდავს მისალმებას.
# თუ სახელი არ გადაეცემა, დაიბეჭდოს "Guest".
def hello (name = "guest"):
    print(f"hello {name}")
hello()


# დავალება:
# დაწერე ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ორ რიცხვს და დაბეჭდავს მათ ჯამს.
x = int(input("enter first num: "))
x2 = int(input("enter second num: "))
print(x + x2)

# დავალება:
# დაწერე ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ასაკს და დაბეჭდავს თუ 10 წლის შემდეგ რამდენი წლის იქნება.
age = int(input(" enter age: "))
age1 = age + 10
print(f"10 wlis shemdeg shen iqnebi{age1}wlis")

# დავალება:
# დაწერე ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს სახელს და დაბეჭდავს მისალმებას.
name = input("enter ypur name: ")
print(f"hello {name}")

# დავალება:
# დაწერე ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს 3 რიცხვს და დაბეჭდავს მათ ნამრავლს.
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
print(num1 * num2 * num3)

# დავალება:
# დაწერე ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ტემპერატურას ცელსიუსში და დაბეჭდავს ფარენჰეიტში გადაყვანილ მნიშვნელობას.
def celsius_to_fahrenheit():
    celsius = float(input("enter temperature iin celsius: "))
    fahernheit = celsius * 9/5 + 32
    print(fahernheit)
celsius_to_fahrenheit()

# ეს ფორმულა გამოიყენეთ კონვერტაციისთვის
# ფორმულა:
# F = C * 9/5 + 32




# დავალება:
# დაწერე ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს საათებს და დაბეჭდავს:

# რამდენი წუთია

# რამდენი წამია
def hour_conversion():
    hour = float(input("enter hours: "))
    min = hour * 60
    second = hour * 3600
    print(min)
    print(second)
hour_conversion()

# დავალება:
# დაწერე ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს 4  სხვადასხვა ქულას და დაბეჭდავს მათ საშუალოს.
def avg():
    score1 = float(input("enter score1: "))
    score2 = float(input("enter score2: "))
    score3 = float(input("enter score3: "))
    score4 = float(input("enter score4: "))
    avg_score = score1 + score2 + score3 +score4 / 4
    print(avg_score)
avg()

