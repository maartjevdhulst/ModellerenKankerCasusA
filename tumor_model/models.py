from math import exp
from matplotlib import pyplot as plt

Nsteps = 5
dt = 1.0 / Nsteps

# Voorbeeld differentiaalvergelijking: dy/dt = y + 1
def ODE(t, y):
    return y + 1.0

# Heeft met beginwaarde y(0)=0 als wiskundige oplossing: y(t) = e^t - 1
def solution(t):
    return exp(t) - 1.0

ts_exact = [i * dt for i in range(Nsteps+1)]
ys_exact = [solution(t) for t in ts_exact]

plt.plot(ts_exact, ys_exact, '-k', label='Exact')
plt.plot(ts_exact[-1], ys_exact[-1], 'ok')
plt.axhline(0.0, lw=0.5, color='k'); plt.axvline(0.0, lw=0.5, color='k')
plt.grid(True); plt.legend()
plt.xlabel('$t$'); plt.ylabel('$y(t)$')
plt.title(f'$y(t=1)$ = {ys_exact[-1]:8.6f}')
plt.show()

# Initialisatie
t, y = 0.0, 0.0
ts_euler, ys_euler = [t], [y]

# ODE-solver
for _ in range(Nsteps):
    # Update volgens Euler
    dydt1 = ODE(t, y)
    t = t + dt
    y = y + dydt1 * dt
    # Bewaar tussenresultaten
    ts_euler.append(t)
    ys_euler.append(y)

plt.plot(ts_exact, ys_exact, '-k', label='Exact')
plt.plot(ts_exact[-1], ys_exact[-1], 'ok')
plt.plot(ts_euler, ys_euler, '.:r', label='Euler')
plt.axhline(0.0, lw=0.5, color='k'); plt.axvline(0.0, lw=0.5, color='k')
plt.grid(True); plt.legend()
plt.xlabel('$t$'); plt.ylabel('$y(t)$')
plt.title(f'error$(t=1)$ = {ys_exact[-1] - ys_euler[-1]:8.6f}')
plt.show()