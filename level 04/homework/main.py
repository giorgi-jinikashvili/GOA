# logical operator - შედგება ორი ოპერატორისგან or - and
print(False and False)
print(False and True)
print(True and True)                           # and operator - უპირატელობას ანიჭებს False - ს
print(False and False and True and False)
print(True and True and False)

print(" ")

print(False or False)
print(True or False)
print(True or True or False or False)          # or operator - უპირატელობას ანიჭებს True - ს
print(False or False or False or True)
print(True or True)

print(" ")

print(20 < 15 and 20 > 15)
print(10 <= 11 and 19 == 19)
print(99 > 100 and 11 > 19)                    # and operator - უპირატელობას ანიჭებს False - ს
print(1 >= 1 and 13 <= 78)
print(89 == 89 and 1 != 2)

print(" ")

print(11 > 12 or 11 < 10)
print(99 >= 10 or 12 == 111)                   
print(15 >= 15 or 19 <= 112)                   # or operator - უპირატელობას ანიჭებს True - ს
print(77 <= 78 or 99 != 89)
print(55 > 15 or 10 < 11)

# რა არის input? input - ი არის ინფორმაცია რომელიც შედის კომპიუტერში ხოლო output არის ინფორმაცია რომელიც გამოდის კომპიუტერიდან.
print(" ")

x = int(input("enter X: "))
y = int(input("enter Y: "))
c = int(input("enter C: "))
a = int(input("enter A: "))

print(x <= y and c > a)
print(a <= x and a <= y)
print(y >= x and c == x)

print(" ")
x = int(input("enter X: "))
y = int(input("enter Y: "))
c = int(input("enter C: "))
a = int(input("enter A: "))

print(a == c or x != y)
print(c >= y or x >= a)
print(y < a or x > c)