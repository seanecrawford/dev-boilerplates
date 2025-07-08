#!/usr/bin/env python3
"""
📦 Python CLI Boilerplate
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description="Say hello to Phantom")
    parser.add_argument("name", help="Your name")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    if args.verbose:
        print(f"👋 Hello there, {args.name}! You're running this script with verbosity ON.")
    else:
        print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
# ===================================================
# 🧠 Concepts Not Shown in This Python Boilerplate
# ===================================================
# 
# input()         → Prompt the user for keyboard input
# sys.argv        → Access raw command-line arguments as a list
# os module       → Interact with the file system or operating system
# datetime        → Handle and format dates/times
# logging         → Create logs instead of using print() for debugging
# open()          → Read/write to files
# with ... as     → Context manager for safe file/resource handling
# try/except      → Error handling to manage exceptions
# list comprehensions → Quick, clean way to build lists
# 
# BONUS:
# if __name__ == "__main__" → Prevents code from running on import
