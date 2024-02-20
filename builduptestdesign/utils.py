import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np


def horner_method(p, t):
    """
    Horner plot method for pressure buildup test analysis.
    
    Parameters:
        p (numpy array): Measured pressure values [psi]
        t (numpy array): Corresponding time values [s]
        
    Returns:
        m (float): Slope of the straight line fit
        b (float): Intercept of the straight line fit
    """
    
    log_p = np.log10(p)
    log_t = np.log10(t)
    m, b = np.polyfit(log_t, log_p, 1)
    
    return m, b

def design_buildup_test(Q, k, h, mu, ct):
    """
    Design a buildup test for pressure transient analysis.
    
    Parameters:
        Q (float): Flow rate [m^3/s]
        k (float): Reservoir permeability [mD]
        h (float): Reservoir thickness [m]
        mu (float): Fluid viscosity [cP]
        ct (float): Total compressibility [1/psi]
        
    Returns:
        t (numpy array): Time values for the test [s]
        p_true (numpy array): True pressure values for the test [psi]
        p_measured (numpy array): Measured pressure values for the test [psi]
    """
    
    r = 0.14 * np.sqrt((k * h) / (mu * ct * Q))  # Effective radius [m]
    t = np.logspace(0, 4, 100)  # Time values for the test [s]
    print(t)
    p_true = 0.394 * Q * mu / (k * h) * (np.log10(0.25 * (k * t) / (mu * ct * r**2)) + 0.80907)  # True pressure values [psi]
    p_measured = p_true + np.random.normal(0, 5, len(t))  # Simulated measured pressure values with noise
    
    return t, p_true, p_measured



# Plotting the Horner plot
def get_plot(t, p_measured, m,b):
    plt.switch_backend('AGG')   
    log_t = np.log(t)
    log_p_measured = np.log(p_measured)
    log_p_fit = m * log_t + b
    plt.plot(log_t, log_p_measured,  label='Measured Data')
    plt.plot(log_t, log_p_fit, label='Horner Fit')
    plt.xlabel('log(Time) [s]')
    plt.ylabel('log(Pressure) [psi]')
    plt.legend()    
    graph = get_graph()
    return graph


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph