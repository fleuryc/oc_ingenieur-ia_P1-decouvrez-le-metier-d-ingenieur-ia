# -*- coding: utf-8 -*-
import argparse
from detector import *

parser = argparse.ArgumentParser(description='Detect the language of some text.')
parser.add_argument("text",
                    help="Input text of which we want to detect the language.")
args = parser.parse_args()

detector = Detector()

print(detector.detect_language(args.text))
