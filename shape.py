import turtle

bob = turtle.Turtle()

#画四方形
def square(t,length):


    for i in range(4):
        t.lt(90)
        t.fd(length)

square(bob,200)

#画多边形
def polygon(t,length,n):


    for i in range(n):

        t.lt(360/n)
        t.fd(length)


polygon(bob,50,30)


#画圆形
def circle(t,r):

    for i in range(1000):
        t.lt(360 / 1000)
        t.fd(3.14*2*r/1000)

circle(bob,100)

#画圆形二
def arc(t,r,angle):

    if angle ==0:
        x = 0
    elif angle ==360:
        x = 360
        for i in range(int(x)):
            t.fd(3.14 * 2 * r / x)
            t.lt(1)
    else:
        x = 360/angle
        for i in range(int(x)):
            t.fd(3.14 * 2 * r / x)
            t.lt(angle)

arc(bob,50,360)