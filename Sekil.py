import turtle
import time

def kare():
    turtle.speed(1)  
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150) 
    turtle.left(90)
    turtle.forward(150) 
    turtle.left(90)
    turtle.forward(150) 
    turtle.left(90)
    time.sleep(2)
    turtle.clear()

def daire():
    turtle.pensize(5)
    turtle.speed(1)
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.fillcolor("red")
    turtle.end_fill()
    time.sleep(2)
    turtle.clear()

def ucgen():
    turtle.pensize(2)
    turtle.speed(1)
    turtle.color("blue")
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    time.sleep(2)
    turtle.clear()

while True:
    sekil = input("Sekil Giriniz(kare,üçgen,daire):")
    if(sekil == "kare" or sekil == "KARE" or sekil == "Kare"):
        kare()
    elif(sekil == "daire" or sekil == "DAİRE" or sekil == "Daire"):
        daire()
    elif(sekil == "üçgen" or sekil == "ÜÇGEN" or sekil == "Üçgen"):
        ucgen()
        continue
    else:
        print("Hatalı Tuşlama")