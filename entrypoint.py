#!/usr/bin/env python3
"""Off By One — real mini-challenge (off-by-one)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'null-byte-poison')


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    with open("/challenge/offbyone.txt", "w") as fh:
        fh.write("null-byte off-by-one poisons adjacent chunk size\n")
        fh.write("merged chunk overlaps seed buffer\n")
        fh.write(f"leaked seed: {CHALLENGE_KEY}\n")
    print("Off-by-one — null byte poison reveals the seed in offbyone.txt.")


if __name__ == "__main__":
    main()
