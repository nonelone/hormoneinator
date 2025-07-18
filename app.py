import pandas as pd
import matplotlib.pyplot as plt
import os

def main():

    # Check if data.csv file exists in project directory
    if not os.path.isfile("data.csv"):
        # And if it does not exist, create a new one from the template
        with open("data.csv", "w") as f:
            f.write('"Estrogen (pg/ml)","Prolactin (ng/ml)","Testosterone (ng/dl)","Progesterone (ng/ml)","Date"')

    # Use pandas to parse .csv
    df = pd.read_csv("data.csv")

    # This software creates 4 subplots in one plot, split into 2 rows and 2 columns

    # Estrogen subplot
    plt.subplot(2,2,1)
    plt.axhspan(30, 400, 0, 1, color="#00ff0030") # Estrogen reference
    plt.plot(df['Date'], df['Estrogen (pg/ml)'], color="g", label="Estrogen (pg/ml)")

    # Boilerplate for each subplot: show grid, legend, and appropriate title
    plt.grid()
    plt.legend()
    plt.title("Estrogen vs Reference")

    # Prolactin subplot
    plt.subplot(2,2,2)
    plt.axhspan(4, 40, 0, 1, color="#0000ff30") # Prolactin reference
    plt.plot(df['Date'], df['Prolactin (ng/ml)'], color="b", label="Prolactin (ng/ml)")

    plt.grid()
    plt.legend()
    plt.title("Prolactin vs Reference")

    # Testosterone subplot
    plt.subplot(2,2,3)
    plt.axhspan(15, 70, 0, 1, color="#ff000030") # Testosterone reference
    plt.plot(df['Date'], df['Testosterone (ng/dl)'], color="r", label="Testosterone (ng/dl)")

    plt.grid()
    plt.legend()
    plt.title("Testosterone vs Reference")

    # Progesterone subplot
    plt.subplot(2,2,4)
    plt.axhspan(2, 25, 0, 1, color="#ff00ff30") # Progesterone reference
    plt.plot(df['Date'], df['Progesterone (ng/ml)'], color="#ff00ff", label="Progesterone (ng/ml)")

    plt.grid()
    plt.legend()
    plt.title("Progesterone vs Reference")


    plt.gcf().set_size_inches(12,9)
    # Save the figure before rendering it - otherwise the software would
    # loop the .show() part and the figure wouldn't be saved properly
    plt.savefig("img.png",dpi=200)

    plt.show()

if __name__ == "__main__":
    main()
