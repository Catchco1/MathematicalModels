from math import sqrt

## The function inputs three distances d1, d2, d3 to a point
## (x,y) from (a,b), (a-1,b) and (a,b-1), respectively.
## The last two parameters a and b are optional, both 0 by default.

def bob_finder(d1,d2,d3,a,b):
    x = a + (d2**2 - d1**2 - 1)/2
    y = b + (d3**2 - d1**2 - 1)/2

    distance_error = abs(d1 - sqrt((x-a)**2 + (y-b)**2))

    if distance_error < 10**(-20):
        print('Bob is at the point ({0:.3f},{1:.3f})'.format(x,y))
    else:
        print('Mismatch between distances is {0:.6f}'.format(distance_error))
        print('Bob may be at the point ({0:.3f},{1:.3f})'.format(x,y))


## Examples of use (remove comment and compile or copy into console):
#bob_finder(405.3, 404.7, 406.1, 0, 0)
## or
bob_finder(35.2, 35.9, 34.5, -243.5, 324.06)
## or
# bob_finder(sqrt(13),sqrt(20),sqrt(10),b=2,a=1)
