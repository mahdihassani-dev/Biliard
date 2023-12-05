import tkinter as tk
import math

mass = 0.1
alpha = 1
g = 10
t = 0.08
fraction_k = 0.3


def getVelocity(par, v0, a, t, alpha, mass):
    match par:
        case True:
            if v0 ** 2 - 2 * alpha / mass < 0:
                return 0

            v0 = math.sqrt(v0 ** 2 - 2 * alpha / mass)

        case False:
            v0 = a * t + v0

            if v0 < 0:
                return 0  # error!

    return v0

def updateVelocity(v0):
    return v0 - t*g*fraction_k*8


def rectangle():
    base = tk.Tk()
    base.title("board")
    canvas = tk.Canvas(base, width=820, height=520)
    canvas.pack()

    # Constants

    def aroundTheBorder(newA, a1, a2):
        if newA >= a2:
            return a2

        elif newA <= a1:
            return a1

    def drawO():
        nonlocal x, y, angle, x1, y1, x2, y2, velocity
        canvas.delete("o")
        newX = x - velocity * math.cos(math.radians(angle))
        newY = y - velocity * math.sin(math.radians(angle))

        if x1 < newX < x2 and y1 < newY < y2:
            x = newX
            y = newY

            # velocity = getVelocity(False, velocity, a, t, alpha, mass)
            velocity = updateVelocity(velocity)

        else:
            if not x1 < newX < x2:
                aroundTheBorder(newX, x1, x2)
                angle = 180 - angle

            else:
                aroundTheBorder(newY, y1, y2)
                angle = 360 - angle

            # velocity = getVelocity(True, velocity, a, t, alpha, mass)
            velocity = updateVelocity(velocity)

        print(f'velocity : {velocity}')

        canvas.create_text(x, y, text="o", fill="black", font=("Arial", 20), tags="o")

        if ((x - 35) * (x - 35) + (y - 35) * (y - 35) < 225 or
                (x - 785) * (x - 785) + (y - 35) * (y - 35) < 225 or
                (x - 35) * (x - 35) + (y - 485) * (y - 485) < 225 or
                (x - 785) * (x - 785) + (y - 485) * (y - 485) < 225):
            victory()
        elif velocity > 0:
            base.after(80, drawO)
        else:
            print(f'x = {x}')
            print(f'y = {y}')
            newInputs()

    def newInputs():
        nonlocal velocity, angle
        velocity = int(input("enter velocity : "))
        angle = int(input("enter angle : "))
        newLine()
        drawO()

    def victory():
        Winwindow = tk.Toplevel()
        Winwindow.title("victory")
        label = tk.Label(Winwindow, text="You won!", font=("Arial", 16))
        label.pack()

    def newLine():
        nonlocal angle, line
        canvas.delete("line")
        angleRad = math.radians(angle)
        lineLength = 300
        xLineEnd = x + lineLength * math.cos(angleRad)
        yLineEnd = y + lineLength * math.sin(angleRad)
        line = canvas.create_line(x, y, xLineEnd, yLineEnd, fill="red", tags="line")

    x1, y1 = 20, 20
    x2, y2 = 800, 500
    canvas.create_rectangle(x1, y1, x2, y2, fill="green")

    x = 410
    y = 260

    canvas.create_text(x, y, text="o", fill="black", font=("Arial", 20), tags="o")

    x1hole1, y1hole1 = 20, 20
    x2hole1, y2hole1 = 50, 50
    canvas.create_oval(x1hole1, y1hole1, x2hole1, y2hole1, fill="black")

    x1hole2, y1hole2 = 800, 20
    x2hole2, y2hole2 = 770, 50
    canvas.create_oval(x1hole2, y1hole2, x2hole2, y2hole2, fill="black")

    x1hole3, y1hole3 = 20, 500
    x2hole3, y2hole3 = 50, 470
    canvas.create_oval(x1hole3, y1hole3, x2hole3, y2hole3, fill="black")

    x1hole4, y1hole4 = 800, 500
    x2hole4, y2hole4 = 770, 470
    canvas.create_oval(x1hole4, y1hole4, x2hole4, y2hole4, fill="black")

    velocity = int(input("enter first velocity : "))
    angle = int(input("enter first angle : "))

    angleRad = math.radians(angle)
    lineLength = 300
    xLineEnd = x + lineLength * math.cos(angleRad)
    yLineEnd = y + lineLength * math.sin(angleRad)

    canvas.create_text(x, y, text="o", fill="black", font=("Arial", 20), tags="o")
    line = canvas.create_line(x, y, xLineEnd, yLineEnd, fill="red", tags="line")
    base.after(80, drawO)

    base.mainloop()


rectangle()
