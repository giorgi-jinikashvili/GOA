# დავალება 1 : მომხმარებელს უნდა შევაყვანინოთ რიცხვი და უნდა დავითვალოთ რამდენია დადებითი და რანდენი უარყოფითი

a = int(input("enter number: "))
if a > 0:
    print("positive")
else:
    print("negative")

b = int(input("enter number: "))

if b > 0:
    print("positive")
else:
    print("negative")

c = int(input("enter number: "))

if c > 0:
    print("positive")
else:
    print("negative")

d = int(input("enter number: "))

if d > 0:
    print("positive")
else:
    print("negative")

e = int(input("enter number: "))
  
if e > 0:
    print("positive")
else:
    print("negative")

 # დავალება 2 : მომხმარებელს ვაყვანინებთ n რიცხვს და 1 დან n ამდე ვითვლით ლუწი რიცხვების ჯამს

n = int(input("enter n: "))
count = 0
for i in range(0, n):
    if i % 2 == 0: 
        count += i
print(count)

# დავალება 3 : მომხმარებელმა უნდა გამოიცნოს რიცხვი და უნდა გამოვიყენოთ if else

x = int(input("enter x: "))
if x > 5 and x < 7:
    print("correct")
else:
    print("inccorect----try egein")

# დავალება 4 : უნდა შევიყვანოთ 3 რიცხვი და თუ საშვალო > 50 დავბეჭდო passed სხვა შემთხვევაში failed

x = int(input("enter number 1: "))
y = int(input("enter number 2: "))
a = int(input("enter number 3: "))
average = (x + y + a) / 3
if average > 50 :
    print("passed")
else:
    print("failed")
# დავალება 5 : დაპრინტე 1 დან 20 ამდე რიცხვები და რომელი რიცხვებიც 3 ის ჯერადი იქნება დავპრინტოთ fizz

for i in range(0, 20,):
    print(i)
    if i % 3 == 0:
        print("fizz")

# დავალება 6 : მომხმარებელმა უნდა შეიყვანოს დადებითი რიცხვი თუ უარყოფითს შეიყვანს უნდა სცადოს ახლიდან

x = int(input("enter x: "))
if x > 0:
    print("succes")  
else:
    print("try egein")
    x = int(input("enter x: "))

# დავალება 7 : მომხმარებელს უნდა შევაყვანინო 6 რიცხვი უნდა დავითვალო რამდენი კენტი და რამდენი ლუწია და ბოლოს ყველაფერი ერთად უნდა გამოვიტანოთ 

luwi = 0
kenti = 0
count1 = int(input("enter number: "))
count2 = int(input("enter number: "))
count3 = int(input("enter number: "))
count4 = int(input("enter number: "))
count5 = int(input("enter number: "))
count6 = int(input("enter number: "))

if count1 % 2 == 0:
    luwi += 1
else:
    kenti += 1

if count2 % 2 == 0:
    luwi += 1
else: 
    kenti += 1

if count3 % 2 == 0:
    luwi += 1
else: 
    kenti += 1
    
if count4 % 2 == 0:
    luwi += 1
else: 
    kenti += 1

if count5 % 2 == 0:
    luwi += 1
else: 
    kenti += 1

if count6 % 2 == 0:
    luwi += 1
else: 
    kenti += 1

print(f"luwi:  {luwi}")
print(f"kenti: {kenti}")

# დავალება 8

highest = int(input("enter num: "))
b = int(input("enter num: "))
if b > highest:
    highest = b
c = int(input("enter num: "))
if c > highest:
    highest = c
d = int(input("enter num: "))
if d > highest:
    highest = d
e = int(input("enter num: "))
if e > highest:
    highest = e

print(f"highest: {highest}")