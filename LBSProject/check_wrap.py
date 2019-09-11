from math import sqrt
from multiprocessing import Pool
from time import time

"""
Your goal is to write the function locator() that inputs the distance
function r from (x,y) to Bob and outputs Bob's location. It is assumed that
r(x,y) is only an approximate distance, but no additional masking is done
(e.g., no random numbers are added to the actual distance, only rounding to
the nearest integer is performed).

The function locator() should output the approximate coordinates of Bob
together with an indication of a possible error.

The function will be issued 10 challenges: it will be called with 10 different
distance functions; Bob's the location will vary in those distance functions.

5 best results will be used for grading.

Grading guidelines:

D: the function produces a correct result within 5 seconds on one of the
attempts, with the error at most +/-0.01 in both x and y coordinates

C: the function produces a correct result within 5 seconds on three of the
attempts, with the error at most +/-0.01 in both x and y coordinates

B: the function produces a correct result on three of the attempts, with
the error at most +/-0.01 in both x and y coordinates, calling the distance
function no more than 40 times.

A: the function produces a correct result on five of the attempts, with
the error at most +/-0.01 in both x and y coordinates, calling the distance
function no more than 25 times.

"""


def locator(distance):
    (x,y) = (0,0)
    d = distance(x,y)
    while d > 0:
        x_new = x - (distance(x+1,y) - d)*d
        y_new = y - (distance(x,y+1) - d)*d
        if x_new == x and y_new == y:
            x_new = x + 1
        (x,y) = (x_new,y_new)
        print(x,y)
        d = distance(x,y)
    return((x,y),1)

### The code below will be used for grading the assignment.
def locator_check(a,b):
    global count
    count = 0
    def r(x,y):
        global count
        count += 1
        return(round(sqrt((x-a)**2+(y-b)**2)))
    start_time = time()
    point,error = locator(r)
    run_time = time()-start_time
    actual_error = max(abs(point[0]-a),abs(point[1]-b))
    if actual_error <= error:
        return('Success: found Bob at {}, with max error {}, called distance \
{} times, took {} seconds'.format(point,error,count,run_time))
    else:
        return('Unsuccessful for point {}, actual error {} exceeds max error \
{}, called distance {} times, took {} seconds'.format((a,b),actual_error,\
                                                      error,count,run_time))

def main():
    points = [[210,-340],[-20.5463,34.46372],[10,10],[0.25,0.25]]
    check = Pool()
    for point in points:
        result = check.apply_async(locator_check,point)
        result.wait(timeout=5)
        if result.ready():
            print(result.get())
        else:
            print('Attempt with point {} unsuccessful, timed out'.format(point))
    check.terminate()

if __name__ == "__main__":
    main()



