#!/usr/bin/env python3

# SpecterText
# Invisible Text Steganography Tool
# Made by Cyber Specterz

import sys
import argparse

ZERO = "\u200B"
ONE = "\u200C"
DELIM = "\u200D"


def banner():
    print("\n===============================")
    print("   SpecterText Stego Tool")
    print("   Made by Cyber Specterz")
    print("===============================\n")


def text_to_binary(data):
    binary = ""
    for ch in data:
        binary += format(ord(ch), "08b")
    return binary


def binary_to_text(binary):
    result = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        result += chr(int(byte, 2))
    return result


def encode_zw(binary):
    encoded = ""
    for bit in binary:
        if bit == "0":
            encoded += ZERO
        else:
            encoded += ONE
    return encoded


def decode_zw(data):
    binary = ""
    for ch in data:
        if ch == ZERO:
            binary += "0"
        elif ch == ONE:
            binary += "1"
    return binary


def embed(secret, target_file):
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()
    except:
        print("Error reading file")
        return

    binary = text_to_binary(secret)
    hidden = encode_zw(binary)

    final = content + DELIM + hidden + DELIM

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(final)

    print("[+] Secret embedded successfully.")


def extract(target_file):
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            data = f.read()
    except:
        print("Error reading file")
        return

    parts = data.split(DELIM)

    if len(parts) < 3:
        print("No hidden message found.")
        return

    hidden = parts[1]

    binary = decode_zw(hidden)

    message = binary_to_text(binary)

    print("\nHidden Message:\n")
    print(message)
    print()


def main():
    banner()

    parser = argparse.ArgumentParser(description="Invisible text steganography tool")
    parser.add_argument("-e", "--embed", help="Embed secret message")
    parser.add_argument("-x", "--extract", action="store_true", help="Extract hidden message")
    parser.add_argument("-f", "--file", help="Target text file")

    args = parser.parse_args()

    if args.embed and args.file:
        embed(args.embed, args.file)

    elif args.extract and args.file:
        extract(args.file)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
