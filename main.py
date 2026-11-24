"""One Letter for Your Day — entry for make.fun.

Writes one letter to /output/entry.txt.
The letter Z stands for "zero sleep": a whole night of bounty hunting.
The rules ask for exactly one letter, A to Z, and nothing else.
"""
import os

LINE = "Z"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
