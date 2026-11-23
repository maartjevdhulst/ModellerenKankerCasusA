import math

# Exponentieel groeimodel
def exponential_model(t, y, r):
    return r * y


# Logistisch groeimodel
def logistic_model(t, y, r, K):
    return r * y * (1 - y / K)


# Gompertz groeimodel
def gompertz_model(t, y, r, K):
    return r * y * math.log(K / y)