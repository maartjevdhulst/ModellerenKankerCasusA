
# ODE-solver met Euler
def euler_solver(ts_input, ys_input, model, r, K):
    # Initialisatie
    t, y = ts_input[0], ys_input[0]
    ts_euler, ys_euler = [t], [y]

    # ODE-solver
    for i in range(len(ts_input) - 1):
        dt = ts_input[i + 1] - ts_input[i]

        # Pakt de afgeleide van het model
        dydt1 = model(t, y, r, K)

        # Update van Euler
        t = t + dt
        y = y + dydt1 * dt

        # Bewaar tussenresultaten
        ts_euler.append(t)
        ys_euler.append(y)

    # Return de resultaten
    return ts_euler, ys_euler


# ODE-solver met Heun
def heun_solver(ts_input, ys_input, model, r, K):
    # Initialisatie
    t, y = ts_input[0], ys_input[0]
    ts_heun, ys_heun = [t], [y]

    # ODE-solver
    for i in range(len(ts_input) - 1):
        dt = ts_input[i + 1] - ts_input[i]

        # Eerste update volgens Heun
        dydt1 = model(t, y, r, K)
        t1 = t + dt
        y1 = y + dydt1 * dt

        # Tweede update volgens Heun
        dydt2 = model(t1, y1, r, K)

        t = t + dt
        y = y + (dydt1 + dydt2) / 2.0 * dt

        # Bewaar tussenresultaten
        ts_heun.append(t)
        ys_heun.append(y)

    # Return de resultaten
    return ts_heun, ys_heun


# ODE-solver met Runge-Kutta 4
def rk4_solver(ts_input, ys_input, model, r, K):
    # Initialisatie
    t, y = ts_input[0], ys_input[0]
    ts_rk4, ys_rk4 = [t], [y]

    # Loop door de tijdstappen en voer RK4 uit
    for i in range(len(ts_input) - 1):
        dt = ts_input[i + 1] - ts_input[i]

        # Bereken de vier k-waarden voor RK4
        k1 = model(t, y, r, K)
        k2 = model(t + dt / 2, y + k1 * dt / 2, r, K)
        k3 = model(t + dt / 2, y + k2 * dt / 2, r, K)
        k4 = model(t + dt, y + k3 * dt, r, K)

        # Update van y en t volgens RK4
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6 * dt
        t = t + dt

        # Bewaar de resultaten
        ts_rk4.append(t)
        ys_rk4.append(y)

    # Return de resultaten
    return ts_rk4, ys_rk4
