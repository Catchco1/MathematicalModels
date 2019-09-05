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
    
    x1 = x
    while(distance(x1,y) < 1):
        x1 += 0.25
    print(x1)
    while (sqrt((x - x1)**2) >= 0.5): 
  
        # Find middle point 
        c = (x+x1)/2
        print('c:{}'.format(c))

        check = distance(c,y)
        print('check:{}'.format(check))
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            x = c 
        else: 
            x1 = c 
        print(x,y)
    y1 = y
    while(distance(x,y1) < 1):
        y1 += 0.25
    while (sqrt((y - y1)**2) >= 0.5): 
  
        # Find middle point 
        c = (y+y1)/2
        print('c:{}'.format(c))

        check = distance(x,c)
        print('check:{}'.format(check))
   
        # Decide the side to repeat the steps 
        if (check == 0): 
            y = c 
        else: 
            y1 = c 
        print(x,y)

# To test:

locator(dist(210.3124,342.3248))
#locator(dist(-270.68,301.76))




