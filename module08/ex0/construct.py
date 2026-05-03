"""Detect and report on the active Python environment."""

import os
import site
import sys


def is_virtual_env() -> bool:
    """Return True when running inside a venv or virtualenv."""
    if hasattr(sys, "real_prefix"):
        return True
    return sys.prefix != sys.base_prefix


def get_site_packages() -> list[str]:
    """Return the list of site-packages directories for the active env."""
    paths: list[str] = []
    if hasattr(site, "getsitepackages"):
        try:
            paths = list(site.getsitepackages())
        except Exception:
            paths = []
    user_site: str = ""
    if hasattr(site, "getusersitepackages"):
        user_site = site.getusersitepackages()
    if user_site and user_site not in paths:
        paths.append(user_site)
    return paths


def print_inside_construct() -> None:
    """Print the success report for a session inside a virtual environment."""
    env_path: str = sys.prefix
    env_name: str = os.path.basename(env_path.rstrip(os.sep)) or env_path
    site_packages: list[str] = get_site_packages()

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    if site_packages:
        for path in site_packages:
            print(f"  {path}")
    else:
        print("  (none reported by site module)")


def print_outside_construct() -> None:
    """Print the warning and instructions when no venv is active."""
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate    # On Unix")
    print("  matrix_env\\Scripts\\activate     # On Windows")
    print()
    print("Then run this program again.")


def main() -> int:
    """Entry point: dispatch on venv detection."""
    if is_virtual_env():
        print_inside_construct()
    else:
        print_outside_construct()
    return 0


if __name__ == "__main__":
    sys.exit(main())
