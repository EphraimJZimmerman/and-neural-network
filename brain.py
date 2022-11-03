import math
import numpy
import time

def sigmoid(x):
    return 1 /(1 + 1 / numpy.exp(x))


# Giving us our cost of
b_fixed = 1
b, w_1, w_2 = 1, 50, 50
x_1, x_2, x_3 = [0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 1]
k = 10

for i in range(100000):
    z_3_1 = b + w_1 * x_1[0] + w_2 * x_2[0]
    output_1 = 1 / (1+math.exp(-z_3_1))
    cost_1 = pow((x_3[0]-output_1), 2)

    z_3_2 = b + w_1 * x_1[1] + w_2 * x_2[1]
    output_2 = 1 / (1+math.exp(-z_3_2))
    cost_2 = pow((x_3[1]-output_2), 2)

    z_3_3 = b + w_1 * x_1[2] + w_2 * x_2[2]
    output_3 = 1 / (1+math.exp(-z_3_3))
    cost_3 = pow((x_3[2]-output_3), 2)

    z_3_4 = b + w_1 * x_1[3] + w_2 * x_2[3]
    output_4 = 1 / (1+math.exp(-z_3_4))
    cost_4 = pow((x_3[3]-output_4), 2)

    delta_cost_1 = (2 * (output_1 - x_3[0]))
    delta_cost_2 = (2 * (output_2 - x_3[1]))
    delta_cost_3 = (2 * (output_3 - x_3[2]))
    delta_cost_4 = (2 * (output_4 - x_3[3]))

    delta_output_1 = (math.exp(z_3_1) / pow(1 + math.exp(z_3_1), 2))
    delta_output_2 = (math.exp(z_3_2) / pow(1 + math.exp(z_3_2), 2))
    delta_output_3 = (math.exp(z_3_3) / pow(1 + math.exp(z_3_3), 2))
    delta_output_4 = (math.exp(z_3_4) / pow(1 + math.exp(z_3_4), 2))

    delta_bias = b_fixed

    delta_w_1_1 = x_1[0]
    delta_w_1_2 = x_1[1]
    delta_w_1_3 = x_1[2]
    delta_w_1_4 = x_1[3]

    delta_w_2_1 = x_2[0]
    delta_w_2_2 = x_2[1]
    delta_w_2_3 = x_2[2]
    delta_w_2_4 = x_2[3]

    delta_b_1 = (delta_cost_1) * (delta_output_1) * (delta_bias)
    delta_b_2 = delta_cost_2 * delta_output_2 * delta_bias
    delta_b_3 = delta_cost_3 * delta_output_3 * delta_bias
    delta_b_4 = (delta_cost_4) * (delta_output_4) * (delta_bias)

    delta_c_w_1_1 = (delta_output_1 * delta_cost_1 * delta_w_1_1)
    delta_c_w_1_2 = (delta_output_2 * delta_cost_2 * delta_w_1_2)
    delta_c_w_1_3 = (delta_output_3 * delta_cost_3 * delta_w_1_3)
    delta_c_w_1_4 = (delta_output_4 * delta_cost_4 * delta_w_1_4)

    delta_c_w_2_1 = (delta_output_1 * delta_cost_1 * delta_w_2_1)
    delta_c_w_2_2 = (delta_output_2 * delta_cost_2 * delta_w_2_2)
    delta_c_w_2_3 = (delta_output_3 * delta_cost_3 * delta_w_2_3)
    delta_c_w_2_4 = (delta_output_4 * delta_cost_4 * delta_w_2_4)

    average_change_in_bias = (
        (delta_b_1 + delta_b_2 + delta_b_3 + delta_b_4) / 4)
    average_change_in_w_1 = (
        (delta_c_w_1_1 + delta_c_w_1_2 + delta_c_w_1_3 + delta_c_w_1_4) / 4)
    average_change_in_w_2 = (
        (delta_c_w_2_1 + delta_c_w_2_2 + delta_c_w_2_3 + delta_c_w_2_4) / 4)

    # print("Change in bias", average_change_in_bias)
    # print("Change in w_1 ", average_change_in_w_1)
    # print("Change in w_2 ", average_change_in_w_2)

    b_new = b - k * average_change_in_bias
    w_1_new = w_1 - k * average_change_in_w_1
    w_2_new = w_2 - k * average_change_in_w_2

    b, w_1, w_2 = b_new, w_1_new, w_2_new
    print(sigmoid(b), sigmoid(w_1), sigmoid(w_2))
    # print(b, w_1, w_2)
    # time.sleep(0.5)
