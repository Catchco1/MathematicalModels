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
    x1 = x + 2
    print(x1)
    while (sqrt((x - x1)**2) >= 0.001): 
  
        # Find middle point 
        c = (x+x1)/2
        print('c:{}'.format(c))

        check = distance(c,y)
        print('check:{}'.format(check))
        # Check if middle point is on the circle 
        if (check == 0): 
            print(x,y)
            break
   
        # Decide the side to repeat the steps 
        if (check*d < 0): 
            x = c 
        else: 
            x1 = c 
        print(x,y)

# To test:

locator(dist(210.3124,342.3248))
#locator(dist(-270.68,301.76))




