
def exp_filter(data, alpha):
    for i in range(1, len(data)):
        data[i] = alpha * data[i] + (1 - alpha) * data[i-1]
    return data


data = [1, 2, 3, 4, 5]
alpha = 0.5
filtered_data = exp_filter(data, alpha)
print(filtered_data)


