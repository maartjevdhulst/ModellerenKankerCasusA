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