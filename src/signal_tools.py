def moving_average(x, window_size):
    y = []

    for i in range(len(x)):
        start = max(0, i - window_size + 1)
        window = x[start:i+1]
        y.append(sum(window) / len(window))

    return y
