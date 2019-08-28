from math import sqrt

d1 = sqrt(65)
d2 = sqrt(74)
d3 = sqrt(52)

# Formulas for x, y assuming the points are 
# (0,0), (-1,0), (0,-1)
x = (d2**2 - d1**2 - 1) / 2
y = (d3**2 - d1**2 - 1) / 2

disatnce_error = abs(x**2 + y**2 - d1**2)

# Perfrom the check to ensure the point is valid
if distance_error < 10**(-8):
    print('Success; Bob is at ({0:.2f},{1:.2f})'.format(x, y))
else:
    print('The distances are wrong.')
