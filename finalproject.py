import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt,find_peaks
from scipy.fft import fft,fftfreq

df = pd.read_csv("ptbdb_abnormal.csv")
x=len(df)
while True:
    try:
        row_index = int(input(f"Enter the row you want to work with (0 to {x-1}): "))
        if 0 <= row_index < x:
            break
        else:
            print("Invalid row number. Please enter a value within the specified range.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

signal1=df.iloc[row_index].values
signal1=signal1-np.mean(signal1)

def plot_signal(signal, title="ECG Signal", xlabel="Time", ylabel="Amplitude"):
    plt.plot(signal)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

def plot_filtered(filteredsignal,title="FilteredECG",xlabel="time",ylabel="amplitude"):
    plt.plot(filteredsignal)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

def highpass_filter(signal,order=4,cutoff=0.5):
    b,a=butter(order,cutoff/(fs/2),btype="high")
    filtered_signal=filtfilt(b,a,signal)
    return filtered_signal

def lowpass_filter(signal,order=4,cutoff=40):
    b,a=butter(order,cutoff/(fs/2),btype="low")
    filtered_signal=filtfilt(b,a,signal)
    return filtered_signal

def bandstop_filter(signal,lowcut,highcut,order=4):
    b,a=butter(order,[lowcut,highcut],btype="bandstop",fs=fs)
    filtered_signal=filtfilt(b,a,signal)
    return filtered_signal

plot_signal(signal1)
fs=125
n=len(signal1)
t=np.linspace(0,n/fs,n,endpoint=False)
y=fft(signal1)
frq=fftfreq(n,1/fs)
positive=frq>0
freq=frq[positive]
y=np.abs(y[positive])

plt.plot(freq, y)
plt.title("FFT of ECG Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

peaks,dict=find_peaks(y,height=0)
peak_freq=freq[peaks]

if any(fq<0.5 for fq in peak_freq):
    signal1=highpass_filter(signal1)
if any(fq>40 for fq in peak_freq):
    signal1=lowpass_filter(signal1)
if any(48<fq<52 for fq in peak_freq):
    signal1=bandstop_filter(signal1,48,52)
if any(58<fq<62 for fq in peak_freq):
    signal1=bandstop_filter(signal1,58,62)

plot_filtered(signal1)

R_peaks,dict1=find_peaks(signal1,height=0.5*np.max(signal1),distance=int(fs*0.4))

signal_duration=len(signal1)/fs
bpm=(len(R_peaks)/signal_duration)*60
print("Normal heart rate is 60 to 100 beats per minute")
if len(R_peaks) > 0:
    signal_duration = len(signal1) / fs
    bpm = (len(R_peaks) / signal_duration) * 60
    print("Heart beat rate per minute: ", bpm)
    if(bpm<60):
        print("Might be a case of Bradycardia,Visit a doctor")
    elif(bpm>100):
        print("Might be a case of Tachycardia,Visit a doctor")
    else:
        print("Normal heart rate")
else:
    print("No R-peaks detected.")
    bpm = 0 
