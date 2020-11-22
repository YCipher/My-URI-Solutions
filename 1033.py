from tkinter import Tk , Button , Canvas
class Rects(Canvas):

    width , height , point1 , point2 = 0,0,0,0
    color = ""
    def creat_Rects(self , width , height , point1 , point2 , color):
                self.color = color
                self.width = width
                self.height = height
                self.point1 = point1
                self.point2 = point2
                myCanvas.create_rectangle(self.height , self.width  , self.point1 , self.point2 , fill = self.color )



###----------Main-----------

root = Tk()

myCanvas = Canvas(root ,width = 1800 , height = 800 , bg = "orange")
myCanvas.pack()
rect1 = myCanvas.create_rectangle(10 , 10 , 40 , 40 ,fill = 'red' ,  tags = ('rect1'))
rect2 = myCanvas.create_rectangle(10 , 10 , 40 , 40 ,fill = 'green' ,  tags = ('rect2'))
#rect3 = myCanvas.create_rectangle(10 , 10 , 40 , 40 ,fill = 'pink' ,  tags = ('rect3'))
#rect4 = myCanvas.create_rectangle(10 , 10 , 40 , 40 ,fill = 'green' ,  tags = ('rect4'))
def right():
    i =  0
    while (i <= 10):
        i = i + 20
        myCanvas.move('rect1', i , 0)
        myCanvas.move('rect2', 0 , i)

def left():
    i =  10
    while (i >= 10):
        i = i - 20
        myCanvas.move('rect1', i , 0)
        myCanvas.move('rect2', 0 , i)

def up():
    i =  10
    while (i >= 10):
        i = i -20
        myCanvas.move('rect1', 0 , i)
        myCanvas.move('rect2', i , 0)
def down():
    i =  0
    while (i <= 10):
        i = i + 20
        myCanvas.move('rect1', 0 , i)
        myCanvas.move('rect2', i , 0)
b1 = Button(root , text = "move right" , command = right)
b1.place(x = 1400 , y = 500)
b2 = Button(root , text = "move left" , command = left)
b2.place(x = 1400 , y = 550)
b3 = Button(root , text = "move up" , command = up)
b3.place(x = 1400 , y = 600 )
b4 = Button(root , text = "move down" , command = down)
b4.place(x = 1400 , y = 650)
root.mainloop()
