"""Language Detector CLI

This file defines the `detector-cli.py` command line.

usage: detector-cli.py [-h] [-t TEXT]

Detect and print the language of the text passed as an argument.
If no text is defined, then a random text in one of the most spoken languages
is selected from the dataset.

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Input text of which we want to detect the language.
"""
import argparse
import csv
from random import randint
from typing import Tuple
from detector import Detector


def process_text(detector: Detector, text: str) -> None:
    """Process input text

    - calls `Decorator.detect_language()`
    - prints the detected language
    """
    print(f'Detected language : { detector.detect_language(text) }')


def pick_from_data(text_file_path: str,
                   language_file_path: str,
                   language_labels_file_path: str) -> Tuple[str, str]:
    """Process random text from dataset

    - open data files : text and expected language, and language labels
    - create a dict `language_labels_dict` : Label -> Wiki Code (IETF format)
    - pick a random line until the language is one of the most spoken
    - return the picked text and expected language
    """

    # Open data files
    with open(text_file_path, mode='r') as text_file:
        text_lines = text_file.readlines()
    with open(language_file_path, mode='r') as language_file:
        language_lines = language_file.readlines()

    # Build a dict of language formats compatible with Azure Service
    language_labels_dict = {}
    with open(language_labels_file_path, mode='r') as language_labels_file:
        reader = csv.reader(language_labels_file)
        next(reader)  # skip header
        for row in reader:
            labels = row[0].split(';')
            language_labels_dict[labels[0]] = labels[2]

    # Pick a rando line containing text in one of the most spoken languages
    # Most spoken languages : en, zh, hi, es, ar and fr
    line_number = randint(0, len(text_lines))
    while (expected_language :=
           language_labels_dict[language_lines[line_number].strip()]
           ) not in ['en', 'zh', 'hi', 'es', 'ar', 'fr']:
        line_number = randint(0, len(text_lines))

    # return text and expected language
    return text_lines[line_number], expected_language


def process_random_text(detector: Detector) -> None:
    """Process random text from dataset

    - call `Decorator.detect_language()`
    - print the text, expected language, detected language and SUCCESS or ERROR
    """
    text, expected_language = pick_from_data(
        'data/x_test.txt', 'data/y_test.txt', 'data/labels.csv')

    detected_language = detector.detect_language(text)

    result = "SUCCESS" if expected_language == detected_language else "ERROR"

    print(f'Text : { text }\n'
          f'Expected language : { expected_language }\n'
          f'Detected language : { detected_language }\n'
          f'Result: { result }')


def main(detector: Detector) -> None:
    """Main function

    - parses the user input
    - if the --text argument is set, the text is processed :
        - call `process_text()` on the input text
        - call `process_random_text()`
    """
    parser = argparse.ArgumentParser(
        description='Detect and print the language of the text passed as an '
        'argument. If no argument is passed, a random text is picked from the '
        'dataset.')
    parser.add_argument('-t', '--text',
                        help='Input text of which we want to detect the '
                        'language.')
    args = parser.parse_args()
    if args.text:
        process_text(detector, args.text)
    else:
        process_random_text(detector)


if __name__ == '__main__':
    main(Detector())
