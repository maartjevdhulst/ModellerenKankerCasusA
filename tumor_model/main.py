
from data_reader import read_data
from optimization import monte_carlo_simulation

from models import (
    exponential_model,
    logistic_model,
    gompertz_model
)

from solvers import (
    euler_solver,
    heun_solver,
    rk4_solver
)

from comparison import compare_results
from visualization import plot_results


# Data inladen
def load_data():
    # Lees de gegevens uit het CSV-bestand met data_reader.py
    ts_input, ys_input = read_data("Hassan_2024.csv")

    return ts_input, ys_input


# Modellen en parameters instellen
def setup_models():
    models = {
        "Exponentieel": (exponential_model, 0.02, None),
        "Logistisch": (logistic_model, 0.02, 5000),
        "Gompertz": (gompertz_model, 0.02, 5000)
    }

    return models


# ODE-solvers instellen
def setup_solvers():
    solvers = {
        "Euler": euler_solver,
        "Heun": heun_solver,
        "RK4": rk4_solver
    }

    return solvers


# Alle modellen en solvers uitvoeren
def run_comparisons(ts_input, ys_input, models, solvers):
    results = {}

    for model_name, (model, r, K) in models.items():

        for solver_name, solver in solvers.items():

            name = model_name + " + " + solver_name

            results[name] = solver(
                ts_input,
                ys_input,
                model,
                r,
                K
            )

    return results


# Zoek de beste parameters met Monte Carlo
def optimize_models(ts_input, ys_input):

    models = {
        "Exponentieel": exponential_model,
        "Logistisch": logistic_model,
        "Gompertz": gompertz_model
    }

    solvers = {
        "Euler": euler_solver,
        "Heun": heun_solver,
        "RK4": rk4_solver
    }

    for model_name, model in models.items():

        for solver_name, solver in solvers.items():

            results = monte_carlo_simulation(
                ts_input, ys_input, model, solver,
                model_name, 5000
            )

            best_result = min(results, key=lambda result: result[2])

            print(model_name, "+", solver_name)
            print("Beste r:", best_result[0])

            if model_name != "Exponentieel":
                print("Beste K:", best_result[1])

            print("Laagste MSE:", best_result[2])
            print()


# Main functie waarin elke stap wordt uitgevoerd
def main():
    ts_input, ys_input = load_data()

    models = setup_models()
    solvers = setup_solvers()

    results = run_comparisons(
        ts_input,
        ys_input,
        models,
        solvers
    )

    compare_results(ys_input, results)

    plot_results(ts_input, ys_input, results)

    optimize_models(ts_input, ys_input)


if __name__ == "__main__":
    main()
