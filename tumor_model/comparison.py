import math



# Bereken de Mean Squared Error
def calculate_mse(ys_input, ys_model):
    total = 0

    for i in range(len(ys_input)):
        difference = ys_input[i] - ys_model[i]
        total = total + difference ** 2

    mse = total / len(ys_input)

    return mse


# berekenen BIC, AIC & AICc
def calculate_BIC_AIC_AICc(ys_input, best_result, solver_results):

    for name, result in solver_results.items():
        ts_model, ys_model = result


    r, K, mse = best_result
    n, k = len(ys_model), len(best_result)-1 #mse erafhalen om aantal parameters te krijgen
    
    BIC  = n * math.log(mse) + k * math.log(n)
    AIC  = n * math.log(mse) + k * 2.0
    AICc = n * math.log(mse) + k * 2.0 * n/(n-k-1) 
   
   
    return f"{BIC  = :.1f},\n {AIC  = :.1f},\n {AICc = :.1f}"

# Vergelijk alle modellen en solvers
def compare_results(ys_input, results):
    for name, result in results.items():
        ts_model, ys_model = result

        mse = calculate_mse(ys_input, ys_model)

        print(name, "MSE:", mse)