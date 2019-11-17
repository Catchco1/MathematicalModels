import numpy as np
from numpy.random import exponential
import matplotlib.pyplot as plt

def arrival_rate(t): # minutes between customers, on average
    if 0 <= t < 4*60:
        return(1)
    if 4*60 <= t < 11*60:
        return(2)
    if 11*60 <= t < 16*60:
        return(3)

def counter_rate(t): # minutes to place an order, on average
    if 0 <= t < 4*60:
        return(1/2)
    if 4*60 <= t < 11*60:
        return(1)
    if 11*60 <= t < 16*60:
        return(2/3)

def preparation_rate(t): # minutes to make a drink, on average
    if 0 <= t < 4*60:
        return(0.75)
    if 4*60 <= t < 11*60:
        return(1.2)
    if 11*60 <= t < 16*60:
        return(1.5)


class Customer():
    def __init__(self, time, prev_customer):
        self.arrival_time = time
        self.counter_time = exponential(counter_rate(time))
        self.prep_time = exponential(preparation_rate(time))
        if prev_customer == 'NULL':
            self.done_order_time = time + self.counter_time
            self.done_time = self.done_order_time + self.prep_time
        else:          
            self.done_order_time = max(time,prev_customer.done_order_time)+\
                                   self.counter_time
            self.done_time = max(self.done_order_time,prev_customer.done_time)+\
                             self.prep_time
        self.in_line_time = self.done_order_time - self.arrival_time
        self.wait_time = self.done_time - self.done_order_time
        
def simulate(num=10):
    simulation = []
    for i in range(num):
        time = exponential(arrival_rate(0))
        customers = [Customer(time,'NULL')]
        
        while time < 16*60:
            time += exponential(arrival_rate(time))
            if time < 16*60:
                customers.append(Customer(time,customers[-1]))
            # otherwise, we are closed
        
        simulation.append(customers)
    return(simulation)

# dt is the time increment, width of a bin
dt = 10

in_line_times = []
wait_times = []

for i in range(int(16*60/dt)):
    in_line_times.append([])
    wait_times.append([])

simulation = simulate(1000)

for record in simulation:    
    for customer in record:
        in_line_times[int(customer.arrival_time/dt)].append(customer.in_line_time)
        wait_times[int(customer.arrival_time/dt)].append(customer.wait_time)
    
plt.plot([np.average(time) for time in in_line_times])
plt.plot([np.std(time) for time in in_line_times])
plt.show()


#t = np.linspace(0,16*60,num=16*6)
#
#plt.plot([customer.arrival_time for customer in customers],\
#         [customer.wait_time for customer in customers])
##plt.plot(t,t**2)
##plt.plot(t,[arrival_rate(i) for i in t])
#
#plt.show()
#


    
