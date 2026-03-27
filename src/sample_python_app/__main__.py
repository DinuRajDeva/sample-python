"""CLI entry when running: python -m sample_python_app"""

import argparse
import sys

from sample_python_app.app import run


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="sample-app",
        description="A minimal sample Python CLI application.",
    )
    parser.add_argument(
        "-n",
        "--name",
        default=None,
        help="Name to greet (default: world)",
    )
    args = parser.parse_args()
    sys.exit(run(name=args.name))


if __name__ == "__main__":
    main()
