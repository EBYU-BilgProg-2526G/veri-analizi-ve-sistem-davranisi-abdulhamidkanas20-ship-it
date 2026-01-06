from io_utils import load_signal_csv
from analysis import sampling_rate, basic_stats
from signal_tools import moving_average
from plotting import plot_time

def main():
    t, x = load_signal_csv("../data/sample_signal.csv")

    fs = sampling_rate(t)
    print("Sampling rate (Hz):", fs)

    stats = basic_stats(x)
    for k, v in stats.items():
        print(f"{k}: {v}")

    x_filt = moving_average(x, window_size=5)

    plot_time(t, x, x_filt, "signal_plot.png")


if __name__ == "__main__":
    main()
