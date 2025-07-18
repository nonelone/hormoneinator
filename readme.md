# Hormoneinator

This is a simple Python script `(Python v3.13.5)`, used to graph users hormone levels against AFAB norms.

<img width="75%" height="75%" alt="a graph with mock data" src="https://github.com/user-attachments/assets/10b6c704-4fa9-4a5d-a2cf-724259aba74b" />


### This is not a medical software!
The author does not claim to be a medical professional, and is not liable for any medical issues arising from using this software. Always consult your hormone levels with your doctor. This software is to be used **only** to graph the levels to show change in time. Furthermore, the "normal" hormone levels are simplified, as hormone levels in AFAB individuals may vary depending on multiple factors.


## Usage

In order to run the script, run `python3 app.py`.

You need to have `numpy` and `matplotlib.pyplot` libraries downloaded - either from pip or your distribiution package manager


The software uses a `data.csv` file that contains all the data used to graph. You need to input the values for each hormone as a floating point number: "X.X", and date as: "DD/MM/YYYY" (the only sane way to write dates), so for example:

> "30.0","20.0","50.0","15.0","5.01.2025"

Would mean that on fifth of January 2025, the user had 30.0 pg/ml of estrogen, 20.0 ng/ml of prolactin, 50.0 ng/dl of testosterone and 15.0 ng/ml of progesterone.

## Configuration

The software by default shows reference level based on a simplified AFAB hormone level. It can also show reference based on a simplified AMAB hormone level or no reference at all. To do so, the user must change the app.py file, in the folowing way:

>    \# Change this variable to change whether you want a reference for AFAB or AMAB individuals
>
>    target_norm = 0
>
>    \# Target norms:
>
>    \# 0 = AFAB (for transfemme)
>
>    \# 1 = AMAB (for transmasc)
>
>    \# 2 = no reference
