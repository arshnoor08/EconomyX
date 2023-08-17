import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.font_manager import FontProperties

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
    plt.yticks(color='w')
    plt.xticks(color='w')

    plt.xlabel("GDP (Output)", fontname="Georgia")
    plt.ylabel("Price Level", fontname="Georgia")
    plt.title("Fiscal Policy Impact", fontname="Georgia")

    plt.grid(False)
    ax.set_facecolor("#F5EFEA")

    plt.title("Contractionary Fiscal Policy", fontname="Georgia")


    def add(val):
        fig, ax = plt.subplots(figsize=(12, 6))

        # Set axis limits (not necessary, but you can adjust these if you want)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        # Remove axis ticks and labels
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # Add text to the center of the plot
        paragraph = " Contractionary fiscal policy refers to deliberate government actions aimed at reducing aggregate demand within an economy. \n This policy is typically implemented during periods of high inflation or when the economy is considered to be overheating. \n The primary goal of a contractionary fiscal policy is to slow down economic growth, decrease inflationary pressures, and stabilize \n the economy. This causes a downward shift in the AD. \n \n The user chose a high future tax rate and low future government spending, it signifies a contractionary fiscal policy. \n Here's how this policy works: \n High Future Tax Rate: Increasing taxes reduces disposable income for households and available funds for businesses. \n This leads to decreased consumption and investment spending, which in turn reduces aggregate demand. \n \n Low Future Government Spending: Decreasing government spending reduces the overall demand for goods and services \n in the economy. \n When the government spends less, it directly reduces the demand for goods and services, which can contribute to lower \n overall economic activity.\n Together, the combination of higher taxes and reduced government spending reduces the overall spending capacity of consumers \n and businesses, leading to a decrease in aggregate demand. \n As a result, this policy aims to slow down economic growth, potentially leading to lower output and decreasing inflationary \n pressures."

        lines = paragraph.strip().split('\n')
        line_height = 0.05  # Adjust this to control the spacing between lines
        y_position = 0.9  # Starting y-position for the first line

        for line in lines:
            ax.text(0.01, y_position, line, fontsize=10, ha='left', va='top')
            y_position -= line_height

        # Display the plot
        plt.show()
    axes = plt.axes([0.81, 0.000001, 0.15, 0.075])
    custom_font = FontProperties(family='Georgia')
    bnext = Button(axes, 'Explanation', color="#EA5E27")
    bnext.label.set_fontproperties(custom_font)
    bnext.on_clicked(add)
    plt.tight_layout()
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
    plt.yticks(color='w')
    plt.xticks(color='w')

    plt.xlabel("GDP (Output)", fontname="Georgia")
    plt.ylabel("Price Level", fontname="Georgia")
    plt.title("Fiscal Policy Impact", fontname="Georgia")
    plt.title("EconomyX", fontname="Georgia", weight='bold')
    plt.grid(False)
    ax.set_facecolor("#F5EFEA")

    plt.title("Expansionary Fiscal Policy", fontname="Georgia")

    def add(val):
        fig, ax = plt.subplots(figsize=(12, 6))

        # Set axis limits (not necessary, but you can adjust these if you want)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        # Remove axis ticks and labels
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # Add text to the center of the plot
        paragraph = " Expansionary fiscal policy is used to stimulate economic activity and boost growth during periods of recession or low economic \n activity. The focus of expansionary fiscal policy is to increase aggregate demand, encourage spending, and promote \n economic recovery. This leads to an upward shift in AD.\n The user chose a low future tax rate and high future government spending, it signifies an expansionary fiscal policy. \n Here's how this policy works: \n \n Low Future Tax Rate: Lowering taxes increases disposable income for households and available funds for \n businesses. This encourages higher consumption and investment spending, leading to increased aggregate demand. \n \n High Future Government Spending: Increasing government spending injects additional funds into the economy, which creates \n demand for goods and services. This spending can lead to increased economic activity and job creation. \n \n The combined effect of lower taxes and increased government spending leads to an overall increase in aggregate demand. \n \n As a result, this policy aims to stimulate economic growth, increase output, and reduce unemployment."

        lines = paragraph.strip().split('\n')
        line_height = 0.05  # Adjust this to control the spacing between lines
        y_position = 0.9  # Starting y-position for the first line

        for line in lines:
            ax.text(0.01, y_position, line, fontsize=10, ha='left', va='top')
            y_position -= line_height

        # Display the plot
        plt.show()
    axes = plt.axes([0.81, 0.000001, 0.15, 0.075])
    custom_font = FontProperties(family='Georgia')
    bnext = Button(axes, 'Explanation', color="#EA5E27")
    bnext.label.set_fontproperties(custom_font)
    bnext.on_clicked(add)
    plt.tight_layout()
    plt.show()

else:
    print("Please enter values that show a shift in the graph.")
    exit()
