import matplotlib.pyplot as plt
import os

def plot_conversion(cr):
    # Ensure output directory exists
    os.makedirs("outputs/charts", exist_ok=True)

    cr.plot(kind='bar')
    plt.title("Conversion Rate by Variant")
    plt.ylabel("Conversion Rate")
    plt.tight_layout()
    plt.savefig("outputs/charts/conversion_comparison.png")
    plt.close()
