import pandas as pd
import matplotlib.pyplot as plt
import os

def main():

    if not os.path.isfile("data.csv"):
        with open("data.csv", "w") as f:
            f.write('"Estrogen (pg/ml)","Prolactin (ng/ml)","Testosterone (ng/dl)","Progesterone (ng/ml)","Date"')

    df = pd.read_csv("data.csv")

    plt.subplot(2,2,1)
    plt.axhspan(30, 400, 0, 1, color="#00ff0030") # Estrogen reference
    plt.plot(df['Date'], df['Estrogen (pg/ml)'], color="g", label="Estrogen (pg/ml)")

    #plt.xlabel("Time")
    plt.grid()
    plt.legend()
    plt.title("Estrogen vs Reference")

    plt.subplot(2,2,2)
    plt.axhspan(4, 40, 0, 1, color="#0000ff30") # Prolactin reference
    plt.plot(df['Date'], df['Prolactin (ng/ml)'], color="b", label="Prolactin (ng/ml)")

    plt.grid()
    plt.legend()
    plt.title("Prolactin vs Reference")

    plt.subplot(2,2,3)
    plt.axhspan(15, 70, 0, 1, color="#ff000030") # Testosterone
    plt.plot(df['Date'], df['Testosterone (ng/dl)'], color="r", label="Testosterone (ng/dl)")

    plt.grid()
    plt.legend()
    plt.title("Testosterone vs Reference")

    plt.subplot(2,2,4)
    plt.axhspan(2, 25, 0, 1, color="#ff00ff30") # Testosterone
    plt.plot(df['Date'], df['Progesterone (ng/ml)'], color="#ff00ff", label="Progesterone (ng/ml)")

    plt.grid()
    plt.legend()
    plt.title("Progesterone vs Reference")


    plt.gcf().set_size_inches(12,9)
    plt.savefig("img.png",dpi=200)

    plt.show()


if __name__ == "__main__":
    main()
