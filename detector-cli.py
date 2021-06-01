import argparse
from detector import detect_language

parser = argparse.ArgumentParser(
    description="Detect the language of some text.")
parser.add_argument(
    "text", help="Input text of which we want to detect the language.")
args = parser.parse_args()

print(f"Detected language : { detect_language(args.text) }")
