# ECG BPM Detector 🫀

This project is a beginner-friendly Python implementation that processes ECG signals to estimate Beats Per Minute (BPM) using filtering and peak detection. It reads ECG data from a publicly available Kaggle dataset and visualizes key aspects like the raw signal, FFT spectrum, and filtered signal, finally calculating the heart rate.

## 📌 Project Highlights

- 🧠 **Signal Filtering**: Butterworth high-pass and low-pass filters are applied to remove noise.
- 📉 **Frequency Analysis**: FFT helps inspect noise and dominant frequencies.
- 🔺 **R-Peak Detection**: Peaks in the ECG waveform are detected to estimate BPM.
- ⚠️ **Medical Insight**: The analyzed ECG signal frequently displayed a heart rate around **39 BPM**, suggesting **bradycardia** — a condition characterized by an abnormally slow heart rate (typically < 60 BPM).

> ⚠️ *Disclaimer: This project is for educational purposes and should not be used for real medical diagnosis.*

## 🗃️ Dataset

- Source: [PTB Diagnostic ECG Dataset on Kaggle](https://www.kaggle.com/datasets/shayanfazeli/heartbeat)
- Sample used: `ptdb_abnormal.csv`

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/afreen-nesha/ECG-BPM-detector.git
   cd ECG-BPM-detector
   ```

2. Install dependencies:
   ```bash
   pip install numpy pandas matplotlib scipy
   ```

3. Run the script:
   ```bash
   python finalproject.py
   ```

## 📊 Output Preview

- Raw ECG signal visualization  
- FFT plot for frequency domain analysis  
- Filtered ECG signal  
- R-peak markers with BPM display

## 🧰 Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- SciPy

## 🙏 Acknowledgements

- PTB Diagnostic Dataset authors
- SciPy documentation & Signal Processing tutorials
- My learning journey through signal filtering & biomedical data
  
> Created with curiosity and a heart for learning 🫀
