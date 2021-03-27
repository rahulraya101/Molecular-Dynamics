# system parameters
k = 2.
m = 3.
x0 = 1.
dt = 0.001  #integration time step

#initial conditions

x = 2.      # initial position   
v = 0.      # intial velocity
a = 0.      # initial accleration
t = 0.      #initial time

for i in range(10000):
    f = -k*(x - x0)   # force acting on x-coordnate (Restoring force)
    a = f/m           # classical mechanics Newton's Law
    v = v + a*dt      # a = dv/dt,  dv = a*dt
    x = x + v*dt      # v = dx/dt,  dx = v*dt
    t = i*dt          # itirating over time

    print(t, x)
