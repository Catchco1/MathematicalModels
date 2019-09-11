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
        x_new = x - (distance(x+1,y) - d)*d
        count += 1
        print('count for gradient:{}'.format(count))
        y_new = y - (distance(x,y+1) - d)*d
        count += 1
        print('count for gradient:{}'.format(count))
        if x_new == x and y_new == y:
            x_new = x + 1
        (x,y) = (x_new,y_new)
        #print(x,y)
        d = distance(x,y)
        count += 1
        print('count for gradient:{}'.format(count))
        #print('d:{}'.format(d))
    while(d > 0):
        if(d < 2):
            x += 0.5
            d = distance(x,y)
            count += 1
            print('count for fix:{}'.format(count))
        else:
            x -= 0.5
            d = distance(x,y)
            count += 1
            print('count for fix:{}'.format(count))
        count += 1
        print('d:{}'.format(d))
    x1 = x + 1
    x2 = x - 1
    xPrime = x
    xPrime2 = x
    yPrime = y
    yPrime2 = y
    y1 = y + 1
    y2 = y - 1
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
    while(abs(yPrime2 - y2) >= 0.01):
        # Find middle point 
        c = (yPrime2+y2)/2

        check = distance(xPrime, c)
        count += 1
        print('count for y2:{}'.format(count))
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            yPrime2 = c 
        else: 
            y2 = c
    BobX = (xPrime + xPrime2) / 2
    BobY = (yPrime + yPrime2) / 2

    print((BobX, BobY))  
    return((round(BobX,2),round(BobY,2)),1)
    

# To test:

locator(dist(210.3124, 342.3248))
locator(dist(210,-340))
locator(dist(-20.5463,34.46372))
locator(dist(-270.68,301.76))