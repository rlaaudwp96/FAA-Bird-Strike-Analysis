"""Python version of the FAA bird-strike analysis; the original R files remain unchanged."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "birds.csv"


def main():
    birds = pd.read_csv(DATA, low_memory=False)
    clean = birds.dropna(subset=["phase_of_flt", "time_of_day", "state"]).copy()
    clean["region"] = clean["state"].eq("CA").map({True: "California", False: "Other states"})
    phase = clean.groupby(["region", "phase_of_flt"]).size().reset_index(name="collisions")
    time = clean.groupby(["region", "time_of_day"]).size().reset_index(name="collisions")

    print(f"Rows analyzed: {len(clean):,}")
    print("\nCollisions by region and flight phase:")
    print(phase.sort_values("collisions", ascending=False).to_string(index=False))
    print("\nCollisions by region and time of day:")
    print(time.sort_values("collisions", ascending=False).to_string(index=False))

    pivot = phase.pivot(index="phase_of_flt", columns="region", values="collisions").fillna(0)
    pivot.plot(kind="bar", figsize=(9, 5), color=["#2f6690", "#f28e2b"])
    plt.title("FAA Bird Strikes by Flight Phase")
    plt.xlabel("Flight phase")
    plt.ylabel("Collisions")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(ROOT / "bird_strike_python_plot.png", dpi=180)
    plt.close()
    print(f"Saved plot: {ROOT / 'bird_strike_python_plot.png'}")


if __name__ == "__main__":
    main()
