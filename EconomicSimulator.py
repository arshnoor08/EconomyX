import numpy as np
import matplotlib.pyplot as plt

# AD-1
# points:
x_values = [30, 70]
y_values = [50, 25]

slope_ad1 = -2.25

ax = plt.axes()
slope_ad2 = -2.25



# INPUTS
# Take user inputs for base tax and future tax rate
base_tax_rate = float(input("Enter the base tax rate: "))
future_tax_rate = float(input("Enter the future tax rate: "))

# Take user inputs for base govt spending and future govt spending
base_govt_spending = float(input("Enter the base government spending: "))
future_govt_spending = float(input("Enter the future government spending: "))


# DECIDING THE SHIFT
if base_tax_rate<future_tax_rate and base_govt_spending>future_govt_spending:
    # contractionary policy
    # shifts downwards
    x_values_down = [20, 60]
    y_values_down = [40, 15]
    plt.plot(x_values, y_values, label="AD-1", color="black")
    plt.text(39, 46, 'AD-1', fontsize=11, fontname="Georgia")

    plt.plot(x_values_down, y_values_down, label="AD-2",  color="#EA5E27")
    plt.text(28, 37, 'AD-2', fontsize=11, fontname="Georgia")

    plt.xlabel("GDP (Output)", fontname="Georgia")
    plt.ylabel("Price Level", fontname="Georgia")
    plt.title("Fiscal Policy Impact", fontname="Georgia")
    plt.legend()
    plt.grid(False)
    ax.set_facecolor("#F5EFEA")
    plt.show()

elif base_tax_rate>future_tax_rate and base_govt_spending<future_govt_spending:
    # expansionary policy
    # shifts upwards
    x_values_up = [40, 80]
    y_values_up = [60, 35]
    plt.plot(x_values, y_values, label="AD-1", color="black")
    plt.text(40, 45, 'AD-1', fontsize=11, fontname="Georgia")

    plt.plot(x_values_up, y_values_up, label="AD-2", color="#EA5E27")
    plt.text(50, 55, 'AD-2', fontsize=11, fontname="Georgia")


    plt.xlabel("GDP (Output)", fontname="Georgia")
    plt.ylabel("Price Level", fontname="Georgia")
    plt.title("Fiscal Policy Impact", fontname="Georgia")
    plt.title("EconomyX", fontname="Georgia", weight='bold')
    plt.grid(False)
    ax.set_facecolor("#F5EFEA")
    plt.show()

else:
    print("Please enter values that show a shift in the graph.")
    exit()





