import random
from solvers import rk4_solver
from comparison import calculate_mse


# Bereken de MSE van het groeimodel
def calculate_model_error(ts_input, ys_input, model, r, K):
    ts_model, ys_model = rk4_solver(ts_input, ys_input, model, r, K)
    mse = calculate_mse(ys_input, ys_model)
    return mse


# Voer de Monte Carlo-simulatie uit
def monte_carlo_simulation(ts_input, ys_input, model, num_simulations):
    results = []

    for i in range(num_simulations):
        r = random.uniform(0.001, 0.1)
        K = random.uniform(4000, 10000)

        mse = calculate_model_error(ts_input, ys_input, model, r, K)
        results.append((r, K, mse))

    return results