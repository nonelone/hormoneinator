# Hormoneinator

This is a simple Python script `(Python v3.13.5)`, used to graph users hormone levels against AFAB norms.

**This is not a medical software! The author does not claim to be a medical professional. Always consult your hormone levels with your doctor.** This software is used only to graph the levels to show change in time. The norms are simplified, as hormone levels in AFAB individuals usualy vary depending on multiple factors.


## Usage

In order to run the script, run `python3 app.py`.

You need to have `numpy` and `pyplot` libraries downloaded - either from pip or your distribiution package manager


The software requires a `data.csv` file that contains all the data used to graph. You need to input the values for each hormone as a floating point number: "X.X", and date as: "DD/MM/YYYY" (the only sane way to write dates)
