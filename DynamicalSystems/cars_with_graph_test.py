import plotly.graph_objects as go
from math import sqrt

class car():
    def __init__(self,prev_car,d0,v0,carnum,a0=0):
        self.car_ahead = prev_car
        self.distance = d0
        self.velocity = v0
        self.accel = a0
        self.carnum = carnum
        
        self.follow_distance = 3
        self.min_follow_distance = 0.5
        self.max_accel = 2 # meters/sec^2
        self.max_decel = -10 # meters/sec^2; panic stop
        self.max_velocity = 40 # meters/sec, 90 mph

        self.desired_velocity = 30
        self.k1fast = 1/16
        self.k1slow = 1/26.25
        self.k2fast = 7/13
        self.k2slow = 5
        self.b1 = 1/350
        self.b2 = 1/350
        self.collision = False

    # Inputs delta-t, updates acceleration, velocity, position
    def update(self,dt):
        if self.car_ahead == 'Null':
            # For the lead car, life is easy
            self.distance += self.velocity * dt + (.5 * self.accel * dt**2)
        else:
            # Compute how far away we expect to be:
            future_distance = self.car_ahead.distance - (self.distance + self.velocity*dt + (.5 * self.accel * dt**2))
            # '2' below should be a parameter
            if future_distance > self.follow_distance:
                if self.car_ahead.accel < 0:
                    self.accel = min(self.max_accel,(future_distance-self.follow_distance) * self.k1slow + (self.velocity - self.desired_velocity) * self.b1)
                else:
                    self.accel = min(self.max_accel,(future_distance-self.follow_distance) * self.k1fast + (self.velocity - self.desired_velocity) * self.b1)
            elif future_distance > self.min_follow_distance:
                if self.car_ahead.accel < 0:
                    #self.accel = (future_distance-self.follow_distance) * 4
                    self.accel = max(self.max_decel,(future_distance-self.follow_distance) * self.k2slow + (self.velocity - self.desired_velocity) * self.b2)
                else:
                    #self.accel = (future_distance-self.follow_distance)/2
                    self.accel = max(self.max_decel,(future_distance-self.follow_distance)*self.k2fast + (self.velocity - self.desired_velocity) * self.b2)
            else:
                if self.car_ahead.accel > self.accel:
                    #self.accel = self.max_decel / 8
                    self.accel = max(self.max_decel,(future_distance-self.follow_distance) * self.k2slow + (self.velocity - self.desired_velocity) * self.b2)
                else:
                    self.accel = self.max_decel
            if self.accel == self.max_decel:
                print(self.carnum)    
            
            self.velocity += self.accel * dt
            # Speed limit check
            self.velocity = min(self.max_velocity,self.velocity)

            self.distance += self.velocity * dt
            # Distance check: see if we ran the other car over
            if self.distance > self.car_ahead.distance:
                # For now, just set the gap at 0
                print('collision')
                self.collision = True
                self.distance = self.car_ahead.distance

# Initialize the first car
cars = [car('Null',30,100/3.6, 0)]

for i in range(8):
    cars.append(car(cars[-1],27 - 7*i,100/3.6, i + 1))

distances = [ [car.car_ahead.distance - car.distance for car in cars[1:]] ]

fail = False
count = 0
while(fail != True and count < 200):
    for car in cars:
        car.update(.5)
        if(car.collision is True):
            fail = True
    count += 1
    #print([car.car_ahead.velocity - car.velocity for car in cars[1:]])    
    distances.append([car.car_ahead.distance - car.distance for car in cars[1:]])

def accumulate(distance):
    for i in range(1,len(distance)):
        distance[i] += distance[i-1]
    return(distance)

for i in range(len(distances)):
    distances[i] = accumulate(distances[i])

zeros = [0 for car in cars[1:]]

# Create figure
fig = go.Figure(
    data=[go.Scatter(x=distances[0],
                     y=zeros,
                     mode="markers",
                     line=dict(width=2, color="blue"))],
    layout=go.Layout(
        xaxis=dict(range=[-2, 100], autorange=False, zeroline=False),
        yaxis=dict(range=[-10, 10], autorange=False, zeroline=False),
        title_text="Car following distances", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    
    frames=[go.Frame(
        data=[go.Scatter(
            x=distances[k],
            y=zeros,
            mode="markers",
            marker=dict(size=10))])

        for k in range(1,len(distances))]
)

fig.show()
