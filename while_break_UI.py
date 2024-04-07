import random
import turtle

ventana = turtle.Screen()
ventana.title('Carrea de Tortugas')
ventana.bgcolor('lightblue')
ventana.setup(width=800,height=310)

tortuga1 = turtle.Turtle()
tortuga1.shape('turtle')
tortuga1.color('red')
tortuga1.penup()
tortuga1.goto(-300,100)
tortuga1.speed(1.3)

tortuga2 = turtle.Turtle()
tortuga2.shape('turtle')
tortuga2.color('blue')
tortuga2.penup()
tortuga2.goto(-300,0)
tortuga2.speed(1.3)


meta = 300

linea_meta =turtle.Turtle()
linea_meta.penup()
linea_meta.goto(meta,150)
linea_meta.pendown()
linea_meta.goto(meta, -150)
linea_meta.hideturtle()



"""while True:#ejemplo con break
    avance_tortuga1 = random.randint(1,20)
    avance_tortuga2 = random.randint(1,20)
    
    tortuga1.forward(avance_tortuga1)
    tortuga2.forward(avance_tortuga2)
    
    print(f'El caracol 1 avanza {avance_tortuga1}, para un total de: {tortuga1.xcor()}')
    print(f'El caracol 2 avanza {avance_tortuga2}, para un total de: {tortuga2.xcor()}\n')
    
    if (tortuga1.xcor() >= meta or tortuga2.xcor() >= meta):
        break
"""

while True:
    
    avance_tortuga1 = random.randint(1,20)
    avance_tortuga2 = random.randint(1,20)
    
    if avance_tortuga1 % 2 == 0 or avance_tortuga2 % 2 == 0:
        continue
    tortuga1.forward(avance_tortuga1)
    tortuga2.forward(avance_tortuga2)
    
    print(f'El caracol 1 avanza {avance_tortuga1}')
    print(f'El caracol 2 avanza {avance_tortuga2}\n')
    
    if (tortuga1.xcor() >= meta or tortuga2.xcor() >= meta):
        break



if (tortuga1.xcor() > tortuga2.xcor()):
    print(f'El caracol 1 ha ganado con un total de {tortuga1.xcor()} puntos!')
elif(tortuga2.xcor() > tortuga1.xcor()):
    print(f'El caracol 2 ha ganado con un total de {tortuga2.xcor()} puntos!')
else:
    print('Empate')

ventana.exitonclick()