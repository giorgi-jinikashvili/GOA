# დავალება: დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ შორის უდიდესს.

def number (number1,number2): 
    if number1 > number2:
        number1
    elif number1 == number2:
        return "ertmanetis tolia"
    else:
        return number2
print(number(10,20))


# დავალება: დაწერე ფუნქცია, რომელიც იღებს ტექსტს (სტრიქონს) და აბრუნებს მის სიგრძეს (სიმბოლოების რაოდენობას).
def text(txt):
    len_txt = len(txt)
    return(len_txt)
print(text("hello world"))
# დავალება: დაწერე ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს True-ს თუ ის ლუწია, სხვა შემთხვევაში — False-ს.
def boolean(number):
    if number % 2 == 0:
        return "true"
    else:
        return "false"
print(boolean(10))
# დავალება: დაწერე ფუნქცია, რომელიც იღებს ორ სტრიქონს (ტექსტს), აერთიანებს მათ და აბრუნებს ერთიან ტექსტს.
def text(text1 ,text2):
    return text1 + " " + text2
print(text("hello", "everyone"))
# დავალება: დაწერე ფუნქცია, რომელიც იღებს მართკუთხედის სიგრძესა და სიგანეს და აბრუნებს მის ფართობს.
def fartobi(sigrdze, sigane):
    return f"martkutxedis fartobia {sigrdze * sigane}"
print(fartobi(10 , 20))
# დავალება: დაწერე ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის მოდულს (აბსოლუტურ მნიშვნელობას) abs() ფუნქციის გარეშე.
def modul(number):
    if number < 0:
        return -number
    else:
        return number
print(modul(-19))
# დავალება: დაწერე ფუნქცია, რომელიც იღებს პროდუქტის ფასს და ფასდაკლების პროცენტს, ხოლო აბრუნებს საბოლოო გადასახდელ თანხას.
def sale_price(price, procent):
    sale = price * 20/100 
    new_price = 100 - sale
    return new_price
print(sale_price(100, 20))
# დავალება: დაწერე ფუნქცია, რომელიც იღებს წელს და აბრუნებს True-ს თუ ის ნაკიანია (გაიყოფა 4-ზე), სხვა შემთხვევაში — False-ს.
def nakiani(year):
    if year % 4 == 0:
        return "true"
    else:
        return "false"
print(nakiani(19))
# დავალება: დაწერე ფუნქცია, რომელიც იღებს ტექსტს და აბრუნებს მას დიდ ასოებად (UPPERCASE) გადაყვანილს.
def upper(txt):
    return txt.upper()
print(upper("giorgi"))
# დავალება: დაწერე ფუნქცია, რომელიც იღებს ადამიანის დაბადების წელს და აბრუნებს მის მიმდინარე ასაკს (მიმდინარე წლად ჩათვალე 2026).
def age(year):
    age = 2026 - year
    return age
print(age(1990))