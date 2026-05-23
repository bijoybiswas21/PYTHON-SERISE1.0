import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

if "df" in globals() and isinstance(df, pd.DataFrame) and not df.empty:
    numeric = df.select_dtypes(include="number")

    if numeric.empty:
        raise ValueError("df has no numeric columns to plot.")

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    numeric.iloc[:, 0].plot(ax=axes[0], color="steelblue", marker="o")
    axes[0].set_title(f"Line Plot: {numeric.columns[0]}")
    axes[0].set_xlabel("Index")
    axes[0].set_ylabel("Value")
    axes[0].grid(True, alpha=0.3)

    numeric.hist(ax=axes[1], bins=20, color="orange", edgecolor="black")
    axes[1].set_title("Histogram of Numeric Columns")

    plt.tight_layout()
    plt.show()
else:
    x = np.arange(1, 11)
    y = np.array([2, 4, 3, 5, 7, 8, 6, 9, 11, 10])

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, marker="o", linewidth=2, color="steelblue", label="Sample Data")
    ax.bar(x, y, alpha=0.2, color="orange")

    ax.set_title("Sample Data Visualization")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    plt.show()