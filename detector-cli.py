"""Language Detector CLI

This file defines the `detector-cli.py` command line.

usage: detector-cli.py [-h] text

Detect and print the language of the text passed as an argument.

positional arguments:
  text        Input text of which we want to detect the language.

optional arguments:
  -h, --help  show this help message and exit
"""
import argparse
from detector import Detector


def main():
    """Main function

    - parses the user input
    - calls `Decorator.detect_language()`
    - prints the detected language
    """
    parser = argparse.ArgumentParser(
        description="Detect and print the language of the text passed as an "
        "argument.")
    parser.add_argument(
        "text", help="Input text of which we want to detect the language.")
    args = parser.parse_args()

    detector = Detector()

    print(f"Detected language : { detector.detect_language(args.text) }")


if __name__ == "__main__":
    main()
