import turtle as tp

tp.speed(0)
tp.hideturtle()


def turtle_moves (element, angle):
    if element == "F":
        tp.forward(d)
    elif element == "-":
        tp.left(-angle)
    elif element == "+":
        tp.left(angle)


def koch(axiom, generator, n):
    if n == 0:
        return axiom
    else:
        return koch(axiom, generator, n-1).replace("F", generator)


d = 50
axiom = "F-F-F-F"
generator = "F-F-F+F-F"
angle = 90
n = 5

for element in koch(axiom, generator, n):
    turtle_moves(element, angle)
tp.done()


#Instruções Para uso do Professor: O valor de "d" representa o tamanho da figura, Axiom e generator o Alfabeto regular
# angle é o angulo de construção da figura e "n" a figura através da biblioteca java 3.8 turtle generator
#Caso veja isso eu tinha cansado de fazer na mão e usei Libraries My bad :(
#Não Rodar o programa com Mais que 10 no valor de "n" motivo: travo meu processador :(