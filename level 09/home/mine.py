# შექმენით სია, სადაც არის შეტანილი სტუდენტების ქულები. გადაუარე სიას და დაბეჭდე თითოეული ქულის შესაბამისი სტატუსი:
# 51-მდე "ჩაიჭრა", 51-90 "ჩააბარა", 90-ზე მეტი "ფრიადი". ბოლოს გამოთვალე საშუალო არითმეტიკული.

qulebi = [20, 50, 68, 44, 12, 43, 100]
for qula in qulebi:
    if qula < 51:
        print("chaichra")
    elif qula > 51 and qula < 90:
        print("chaabara")
    elif qula > 90:
        print("friadosani")

#2 შექმენით რიცხვების სია. დათვალე მათი ჯამი for ციკლის გამოყენებით.

numbers = [2,3,4,23,55,66,5,44,67,556,7]   
jami = 0
for num in numbers:
    jami += num
print(jami)

# დავალება 3 შეამოწმეთ არის თუ არა რიცხვი 7 სიაში

numbers = [2,3,34,5,6,77,8,7,66,4]
for num in numbers:
    if num == 7:
        print("რიცხვი 7 სიაშია")

# დავალება 4 შექმენით სია და დათვალეთ რამდენი მნიშვნელობაა სიაში

sia = [1,2,1,1,11,2,1,23,3,"gio"]
x = len(sia)
print(x)

# დავალება 5 იპოვე ყველაზე მაღალი რიცხვი სიაში

numbers = [33,4,54,55,34,2,]
highest = 0
for high in numbers:
    if high > highest:
        highest = high
print(highest)

# დავალება 6 შექმენით სია გადაეცით სახელები და  ყველას მიესალმეთ

names = ["gio", "nika", "nodari", "nino", "lika"]
for name in names:
    print(name + " " + "hello")

# დავალება 7 მოცემულია სია [1, 2, 3, 2, 4, 2, 5]. დათვალე, რამდენჯერ მეორდება რიცხვი 2 ამ სიაში ციკლის 

numbers = [1, 2, 3, 2, 4, 2, 5]
number2 = 0
for num in numbers:
    if 2 == num:
        number2 += 1
print(number2)

# დავალება 8 მოცემულია რიცხვების სია [15, 3, 8, 42, 1]. იპოვე და დაბეჭდე ყველაზე პატარა (მინიმალური) ელემენტი

numbers = [15, 3, 8, 42, 1]
small = 100
for num in numbers:
    if num < small:
        small = num
print(small)