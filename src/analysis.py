import numpy as np

def sampling_rate(t):
    dt = t[1] - t[0]
    fs = 1 / dt
    return fs


def basic_stats(x):
    stats = {
        "mean": np.mean(x),
        "std": np.std(x),
        "rms": np.sqrt(np.mean(x**2)),
        "min": np.min(x),
        "max": np.max(x)
    }
    return stats

