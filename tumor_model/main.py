
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

from comparison import compare_results, calculate_BIC_AIC_AICc
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
def optimize_models(ts_input, ys_input, solver_results):

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

            # Zoek het resultaat met de laagste MSE
            best_result = results[0]

            for result in results:
                if result[2] < best_result[2]:
                    best_result = result

            # Bepaal de BIC, AIC en AICc
            name = model_name + " + " + solver_name

        bic_aic = calculate_BIC_AIC_AICc(ys_input, best_result, solver_results)

        # Print de beste parameters en MSE
        print(name)
        print("Beste r:", best_result[0])

        if name != "Exponentieel":
            print("Beste K:", best_result[1])

        print("Laagste MSE:", best_result[2])
        print("Modelvergelijking:\n", bic_aic)


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

    optimize_models(ts_input, ys_input, results)


if __name__ == "__main__":
    main()
