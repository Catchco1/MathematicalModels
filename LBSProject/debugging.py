from math import sqrt



def dist(a,b):
    return(lambda x,y : round(sqrt((x-a)**2+(y-b)**2)))


def locator(distance):
    (x,y) = (0,0)
    d = distance(x,y)
    count = 0
    count += 1
    print('count for gradient:{}'.format(count))
    while d > 1:
        x_new = x - (distance(x+1,y) - d)*d/1
        count += 1
        print('count for gradient:{}'.format(count))
        y_new = y - (distance(x,y+1) - d)*d/1
        count += 1
        print('count for gradient:{}'.format(count))
        if x_new == x and y_new == y:
            x_new = x + 1
        (x,y) = (x_new,y_new)
        #print(x,y)
        d = distance(x,y)
        count += 1
        print('count for gradient:{}'.format(count))
    #return
    while(d > 0):
        count += 1
        print('count for fix:{}'.format(count))
        if(distance(x - 1000.5, y) > 1000):
            count += 1
            print('count for fix:{}'.format(count))
            x += 0.25
        else:
            count += 1
            print('count for fix:{}'.format(count))
            x -= 0.25
        if(distance(x, y - 1000.5) > 1000):
            y += 0.25
        else:
            y -= 0.25
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
        count += 1
        print('count for x1:{}'.format(count))
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            xPrime = c 
        else: 
            x1 = c 
    while(abs(xPrime2 - x2) >= 0.01):
        # Find middle point 
        c = (xPrime2+x2)/2

        check = distance(c,y)
        count += 1
        print('count for x2:{}'.format(count))
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            xPrime2 = c 
        else: 
            x2 = c 
    if(distance(xPrime2,y+0.1) == 0):
        count += 1
        print('count for yStart:{}'.format(count))
        y1 = y + 1
    else:
        count += 1
        print('count for yStart:{}'.format(count))
        y1 = y - 1
    while (abs(yPrime - y1) >= 0.01): 
        # Find middle point 
        c = (yPrime+y1)/2

        check = distance(xPrime, c)
        count += 1
        print('count for y1:{}'.format(count))
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            yPrime = c 
        else: 
            y1 = c
    BobX = (xPrime + xPrime2) / 2
    BobY = (yPrime + y) / 2

    print((BobX, BobY))  
    return((round(BobX,2),round(BobY,2)),0.01)
    

# To test:

locator(dist(210.3124, 342.3248))
locator(dist(210,-340))
locator(dist(-20.5463,34.46372))
locator(dist(-270.68,301.76))
locator(dist(10,10))
locator(dist(0.25,0.25))