"""Passive-Aggressive Fridge — make.fun entry.

A smart fridge leaves one passive-aggressive note for its owner: a counted
egg-tray receipt. The fridge's own inventory is the evidence.

The note follows the Vacuum blueprint as structure (smug claim, then a
specific non-round number as counted evidence, then an escalation, with the
punch in the last words) without copying any winner's voice or words. The
fridge counts its eggs; the owner does not. The missing egg is the mystery,
and the mystery is the owner.
"""
import os

ENTRY = "Egg tray, day 14: 11 eggs, 0 omelettes, 1 missing egg. The missing egg is the mystery. The mystery is you. The eggs are the evidence."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
