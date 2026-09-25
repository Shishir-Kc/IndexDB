import subprocess
import sys


def main():
    commands = [
        ["ruff", "check", "."],
        ["ruff", "format", "--check", "."],
        ["pyright", "."],
        ["pytest"],
    ]
    for cmd in commands:
        print(f"\n$ {' '.join(cmd)}")
        result = subprocess.run(cmd, check=False)
        if result.returncode != 0:
            sys.exit(result.returncode)
    print("\nAll checks passed.")
