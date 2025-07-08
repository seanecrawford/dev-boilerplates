#!/usr/bin/env python3
"""
Simple CLI Application Template
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument("name", help="Your name")
    args = parser.parse_args()

    print(f"Hello, {args.name}! Welcome to the CLI world.")

if __name__ == "__main__":
    main()

