"""Loading Programs — package management with pip and Poetry."""

import importlib
import sys

REQUIRED_PACKAGES: list[tuple[str, str]] = [
    ("pandas", "Data manipulation"),
    ("numpy", "Numerical computation"),
    ("matplotlib", "Visualization"),
]


def check_dependency(name: str) -> tuple[bool, str]:
    """Return (available, version) for a third-party package."""
    try:
        module = importlib.import_module(name)
    except ImportError:
        return False, ""
    version: str = getattr(module, "__version__", "unknown")
    return True, version


def print_dependency_check() -> bool:
    """Print the dependency checklist; return True iff all are present."""
    print("Checking dependencies:")
    all_ok: bool = True
    for pkg_name, description in REQUIRED_PACKAGES:
        ok, version = check_dependency(pkg_name)
        if ok:
            print(f"  [OK] {pkg_name} ({version}) - {description} ready")
        else:
            print(f"  [MISSING] {pkg_name} - {description} unavailable")
            all_ok = False
    return all_ok


def print_install_instructions() -> None:
    """Print install instructions for both pip and Poetry."""
    print()
    print("Install dependencies with one of:")
    print()
    print("  # Using pip:")
    print("  pip install -r requirements.txt")
    print()
    print("  # Using Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def compare_package_managers() -> None:
    """Print a side-by-side comparison of pip vs Poetry."""
    print()
    print("=" * 64)
    print("pip vs Poetry — side by side")
    print("=" * 64)
    rows: list[tuple[str, str, str]] = [
        ("Manifest file", "requirements.txt", "pyproject.toml"),
        ("Lockfile", "manual (pip freeze)", "poetry.lock (auto)"),
        ("Resolver", "pip resolver", "Poetry resolver"),
        ("Dev dep groups", "no", "yes"),
        ("Auto venv", "no", "yes"),
        ("Build/publish", "no", "yes"),
    ]
    print(f"{'Feature':<18} {'pip':<22} {'Poetry':<22}")
    print(f"{'-' * 18} {'-' * 22} {'-' * 22}")
    for feature, pip_v, poetry_v in rows:
        print(f"{feature:<18} {pip_v:<22} {poetry_v:<22}")


def run_analysis() -> None:
    """Run the Matrix data analysis and produce the visualization."""
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print()
    print("Analyzing Matrix data...")
    n: int = 1000
    print(f"Processing {n} data points...")

    rng = np.random.default_rng(42)
    raw = rng.normal(loc=0.0, scale=1.0, size=n).cumsum()
    df = pd.DataFrame({"signal": raw})
    df["rolling_mean"] = df["signal"].rolling(window=20).mean()
    df["rolling_std"] = df["signal"].rolling(window=20).std()

    print("Generating visualization...")
    output_path: str = "matrix_analysis.png"
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df["signal"], label="signal", alpha=0.4)
        ax.plot(
            df.index,
            df["rolling_mean"],
            label="rolling mean (window=20)",
            color="red",
        )
        ax.set_title("Matrix data — simulated random walk")
        ax.set_xlabel("step")
        ax.set_ylabel("value")
        ax.legend()
        fig.tight_layout()
        fig.savefig(output_path)
        plt.close(fig)
    except OSError as err:
        print(f"ERROR: failed to write '{output_path}': {err}")
        raise

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_path}")
    print()
    print("Summary:")
    print(f"  mean = {df['signal'].mean():.4f}")
    print(f"  std  = {df['signal'].std():.4f}")
    print(f"  min  = {df['signal'].min():.4f}")
    print(f"  max  = {df['signal'].max():.4f}")


def main() -> int:
    """Entry point."""
    print("LOADING STATUS: Loading programs...")
    print()
    available: bool = print_dependency_check()
    compare_package_managers()
    if not available:
        print_install_instructions()
        return 1
    run_analysis()
    return 0


if __name__ == "__main__":
    sys.exit(main())
