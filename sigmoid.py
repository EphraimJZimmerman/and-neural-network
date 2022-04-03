

import math
# F(x) = 1/(1 + e^(-x))


def stable_sigmoid(x):

    if x >= 0:
        z = math.exp(-x)
        sig = 1 / (1 + z)
        return sig
    else:
        z = math.exp(x)
        sig = z / (1 + z)
        return sig

print(stable_sigmoid(0))

#0.5 is the value when x is = 0.
