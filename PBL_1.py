import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the model
def model(y, t, M1):
    M2 = 0.6*(1-(y[3]/50)/1300)*M1 # assuming no active transport
    M3 = M1 - M2
    M4 = 0.01*(M2+y[3]) # change rate from 0.01 to f(y[3]/50) (BLL/50)
    M6 = M2 - M4
    M5 = 0.1*M6 # assuming 90% of the lead in the blood entering bone accumulates in the bone

    dydt = [M2, M3, M4, M5, M6]
    return dydt

# Initial conditions
M1 = 11.53  # intake of lead (in ug/day)
M20, M30, M40, M50, M60 = 0, 0, 0, 0, 0 
y0 = [M20, M30, M40, M50, M60]

# Time conditions
t = np.linspace(0, 700, 700)  # Define the time points for integration

# Solving the ODEs
y = odeint(model, y0, t, args = (M1, ))

# Plotting results
plt.figure(figsize=(10, 6))
plt.plot(t, y[:, 3]/50, 'b-', linewidth=2, label='Blood Lead Levels')
plt.title('Change in Blood Lead Levels Over Time')
plt.xlabel('Time (days)')
plt.ylabel('Lead Concentration')
plt.legend(loc='best')
plt.grid(True)
plt.show()

end_state = y[699]
W_final = end_state[3]/50


print('final mass fraction: ' , W_final)