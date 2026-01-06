import matplotlib.pyplot as plt

def plot_time(t, x_raw, x_filt, save_path):
    plt.figure()
    plt.plot(t, x_raw, label="Raw Signal")
    plt.plot(t, x_filt, label="Filtered Signal")

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Time Domain Signal")
    plt.legend()
    plt.grid()

    plt.savefig(save_path)
    plt.close()
