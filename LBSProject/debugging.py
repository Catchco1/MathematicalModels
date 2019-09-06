from math import sqrt



def dist(a,b):
    return(lambda x,y : round(sqrt((x-a)**2+(y-b)**2)))


def locator(distance):
    (x,y) = (0,0)
    d = distance(x,y)
    while d > 1:
        x_new = x - (distance(x+1,y) - d)*d
        y_new = y - (distance(x,y+1) - d)*d
        if x_new == x and y_new == y:
            x_new = x + 1
        (x,y) = (x_new,y_new)
        print(x,y)
        d = distance(x,y)
        print('d:{}'.format(d))
    
    x1 = x
    x2 = x
    xPrime = x
    xPrime2 = x
    yPrime = y
    y1 = y
    while(distance(x1,y) < 1):
        x1 += 0.25
    while(distance(x2, y) < 1):
        x2 -= 0.25
    while (abs(xPrime - x1) >= 0.001): 
  
        # Find middle point 
        c = (xPrime+x1)/2

        check = distance(c,y)
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            xPrime = c 
        else: 
            x1 = c 
    while(abs(xPrime2 - x2) >= 0.001):
        # Find middle point 
        c = (xPrime2+x2)/2

        check = distance(c,y)
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            xPrime2 = c 
        else: 
            x2 = c 
    while(distance(xPrime, y1) < 1):
        y1 += 0.25

    while (abs(yPrime - y1) >= 0.001): 
        # Find middle point 
        c = (yPrime+y1)/2

        check = distance(xPrime, c)
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            yPrime = c 
        else: 
            y1 = c
    BobX = (xPrime + xPrime2) / 2
    BobY = (yPrime + y) / 2

    print(BobX, BobY)  
    return((BobX,BobY),1)
    

# To test:

locator(dist(210.3124,342.3248))
#locator(dist(-270.68,301.76))




