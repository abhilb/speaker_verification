import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

def main():
    sample1, fs = librosa.load('abhilash_1.m4a')
    sample2, fs = librosa.load('gurjeet_1.m4a')
    print(sample1.shape)
    print(sample2.shape)

    _, ax = plt.subplots(nrows=2, sharex=True, sharey=True)
    librosa.display.waveshow(sample1, sr=fs, ax=ax[0])
    ax[0].set(title='Sample 1')
    ax[0].label_outer()

    librosa.display.waveshow(sample2, sr=fs, ax=ax[1])
    ax[1].set(title='Sample 2')

    plt.show()

if __name__ == "__main__":
    main()