
import random
from comparison import calculate_mse


def calculate_model_error(ts_input, ys_input, model, solver, r, K):
    ts_model, ys_model = solver(
        ts_input, ys_input, model, r, K
    )

    mse = calculate_mse(ys_input, ys_model)

    return mse


def monte_carlo_simulation(ts_input, ys_input, model, solver, model_name, num_simulations):
    results = []

    for i in range(num_simulations):

        # Kies willekeurige waarden voor de parameters
        r = random.uniform(0.001, 0.1)

        if model_name == "Exponentieel":
            K = None
        else:
            K = random.uniform(4000, 10000)

        # Bereken de MSE
        mse = calculate_model_error(
            ts_input, ys_input, model, solver, r, K
        )

        results.append((r, K, mse))

    return results
