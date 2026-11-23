from matplotlib import pyplot as plt

# Visualiseer alle groeimodellen en solvers
def plot_results(ts_input, ys_input, results):
    plt.figure(figsize=(12, 7))

    plt.plot(ts_input, ys_input, 'ok', label='Meetgegevens')

    for name, result in results.items():
        ts_model, ys_model = result

        plt.plot(ts_model, ys_model, label=name)

    plt.grid(True)
    plt.legend()
    plt.xlabel('Tijd (dagen)')
    plt.ylabel('Tumorvolume (mm³)')
    plt.title('Vergelijking tumorgroeimodellen en ODE-solvers')
    plt.show()

# Visualiseer na optimalisatie van de parameters
def plot_optimized_results(ts_input, ys_input, results, models, solvers):
    plt.figure(figsize=(12, 7))

    plt.plot(ts_input, ys_input, 'ok', label='Meetgegevens')

    for model_name, model in models.items():

        for solver_name, solver in solvers.items():

            name = model_name + " + " + solver_name

            # Zoek de beste parameters
            simulations = results[name]
            best_result = simulations[0]

            for result in simulations:
                if result[2] < best_result[2]:
                    best_result = result

            # Bereken de tumorgroei met de beste parameters
            ts_model, ys_model = solver(
                ts_input, ys_input, model,
                best_result[0], best_result[1]
            )

            plt.plot(ts_model, ys_model, label=name)

    plt.grid(True)
    plt.legend()
    plt.xlabel('Tijd (dagen)')
    plt.ylabel('Tumorvolume (mm³)')
    plt.title('Tumorgroei met geoptimaliseerde parameters')
    plt.show()