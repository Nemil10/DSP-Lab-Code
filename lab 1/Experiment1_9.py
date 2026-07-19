import numpy as np
import matplotlib.pyplot as plt

def simulate_function(time):
    
    y = np.zeros_like(time)
    
    # Apply unit impulses (Delta functions) at specific time indices
    y[time == 0] = 1       
    y[time == 1] += 1      
    y[time == -5] += 3      
    
    return y

# Define the time range from -10 to 10 (inclusive)
time = np.arange(-10, 11)

# Simulate the function to get the discrete-time sequence values
function_values = simulate_function(time)

# Plot and display the function using a stem plot for discrete signals
plt.stem(time, function_values)

# Add titles, labels, and formatting
plt.title('Function y(t) = Delta(t) + delta(t-1) + 3*delta(t+5)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.ylim([-0.5, 4.5])
plt.grid(True)

# Render the visualization
plt.show()
