
import math

def exponential_model(t, y, r, K=None):
    return r * y

def logistic_model(t, y, r, K):
    return r * y * (1 - y / K)

def gompertz_model(t, y, r, K):
    return r * y * math.log(K / y)
