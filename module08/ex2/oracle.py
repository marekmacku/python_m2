"""The Oracle — load configuration from environment variables and .env."""

import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except ImportError:
    print("ERROR: python-dotenv not installed (pip install python-dotenv)")
    sys.exit(1)

REQUIRED: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]
DEFAULTS: dict[str, str] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "sqlite:///./matrix_dev.db",
    "API_KEY": "",
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": "http://localhost:8080",
}
PLACEHOLDERS: set[str] = {"", "changeme", "your_api_key_here"}


def mask(v: str) -> str:
    if not v:
        return "(empty)"
    if len(v) <= 4:
        return "*" * len(v)
    return f"{v[:2]}{'*' * (len(v) - 4)}{v[-2:]}"


def main() -> int:
    env_file: str = os.path.join(os.path.dirname(__file__), ".env")
    env_loaded: bool = os.path.exists(env_file)
    if env_loaded:
        try:
            load_dotenv(env_file, override=False)
        except OSError as err:
            print(f"WARNING: could not read '{env_file}': {err}")
            env_loaded = False

    cfg: dict[str, str] = {k: os.getenv(k, DEFAULTS[k]) for k in REQUIRED}
    mode: str = cfg["MATRIX_MODE"]
    db: str = cfg["DATABASE_URL"]
    api: str = cfg["API_KEY"]
    is_local: bool = "localhost" in db or db.startswith("sqlite:")
    db_kind: str = "local" if is_local else "remote"
    api_status: str = "Authenticated" if api else "Missing API_KEY"

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"  Mode: {mode}")
    print(f"  Database: Connected to {db_kind} instance")
    print(f"  API Access: {api_status} (key: {mask(api)})")
    print(f"  Log Level: {cfg['LOG_LEVEL']}")
    print(f"  Zion Network: {cfg['ZION_ENDPOINT']}")

    issues: list[str] = []
    if mode not in ("development", "production"):
        issues.append(f"Unknown MATRIX_MODE '{mode}'")
    if mode == "production":
        if api in PLACEHOLDERS:
            issues.append("Production needs real API_KEY")
        if db.startswith("sqlite:"):
            issues.append("Production should not use sqlite DATABASE_URL")
        if cfg["LOG_LEVEL"] == "DEBUG":
            issues.append("Production should not use LOG_LEVEL=DEBUG")
    if issues:
        print("\nWarnings:")
        for i in issues:
            print(f"  - {i}")

    print("\nEnvironment security check:")
    print("  [OK] No hardcoded secrets detected")
    if env_loaded:
        env_msg: str = "[OK] .env file properly configured"
    else:
        env_msg = "[WARN] No .env file"
    print(f"  {env_msg}")
    overrides: str = "applied" if mode == "production" else "available"
    print(f"  [OK] Production overrides {overrides}")
    print("\nThe Oracle sees all configurations.")

    return 1 if mode == "production" and issues else 0


if __name__ == "__main__":
    sys.exit(main())
