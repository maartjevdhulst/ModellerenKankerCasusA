# Bereken de Mean Squared Error
def calculate_mse(ys_input, ys_model):
    total = 0

    for i in range(len(ys_input)):
        difference = ys_input[i] - ys_model[i]
        total = total + difference ** 2

    mse = total / len(ys_input)

    return mse


# Vergelijk alle modellen en solvers
def compare_results(ys_input, results):
    for name, result in results.items():
        ts_model, ys_model = result

        mse = calculate_mse(ys_input, ys_model)

        print(name, "MSE:", mse)