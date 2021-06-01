[![Python application](https://github.com/fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia/actions/workflows/python-app.yml/badge.svg)](https://github.com/fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia/actions/workflows/python-app.yml) [![CodeQL](https://github.com/fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia/actions/workflows/codeql-analysis.yml)

# Language Detector

Repository of OpenClassrooms' [AI Engineer path](https://openclassrooms.com/fr/paths/188-ingenieur-ia), project #1.

Goal : use MS Azure's [Cognitive Services](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-detect) to detect the language of some text.

## Installation

1. Install dependencies

```bash
$ pip install -r requirements.txt
```

2. Create a Translator resource in Azure

Follow Azure's official documentation : [Create a Translator resource
](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-how-to-signup)

3. Configure your environment

Rename `.env.example` into `.env` and set the parameters with the values provided by Azure.

## Usage

### CLI

Run `detector-cli.py` to detect the language of the text passed as an argument.

```bash
$ python3 detector-cli.py "We are the knights who say 'Ni!'"
> Detected language : en
```

### Test

Run `pytest` to check that the language of the most spoken languages is correctly detected.
