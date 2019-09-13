def locator(distance):
    (x,y) = (0,0)
    d = distance(x,y)
    while d > 1:
        x_new = x - (distance(x+1,y) - d)*d
        y_new = y - (distance(x,y+1) - d)*d
        if x_new == x and y_new == y:
            x_new = x + 1
        (x,y) = (x_new,y_new)
        d = distance(x,y)
    while(d > 0):
        increment = 0.5
        if(distance(x - 1000.5, y) > 1000):
            x += increment
        else:
            x -= increment
        if(distance(x, y - 1000.5) > 1000):
            y += increment
        else:
            y -= increment
        d = distance(x,y)
    x1 = x + 1
    x2 = x - 1
    xPrime = x
    xPrime2 = x
    yPrime = y
    while (abs(xPrime - x1) >= 0.01): 
  
        # Find middle point 
        c = (xPrime+x1)/2

        check = distance(c,y)
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            xPrime = c 
        else: 
            x1 = c 
    while(abs(xPrime2 - x2) >= 0.01):
        # Find middle point 
        c = (xPrime2+x2)/2

        check = distance(c,y)
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            xPrime2 = c 
        else: 
            x2 = c 
    if(distance(xPrime2,y+0.1) == 0):
        y1 = y + 1
    else:
        y1 = y - 1
    while (abs(yPrime - y1) >= 0.01): 
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

    print((BobX, BobY))  
    return((round(BobX,2),round(BobY,2)),0.01)