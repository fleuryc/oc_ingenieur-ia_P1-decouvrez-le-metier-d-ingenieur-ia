[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2378cec53a2c4de8aaeedb464367e709)](https://app.codacy.com/gh/fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia?utm_source=github.com&utm_medium=referral&utm_content=fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia&utm_campaign=Badge_Grade_Settings)
[![Python application](https://github.com/fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia/actions/workflows/python-app.yml/badge.svg)](https://github.com/fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia/actions/workflows/python-app.yml) [![CodeQL](https://github.com/fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/fleuryc/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia/actions/workflows/codeql-analysis.yml)

# Language Detector

Repository of OpenClassrooms' [AI Engineer path](https://openclassrooms.com/fr/paths/188-ingenieur-ia), project #1.

Goal : use MS Azure's [Cognitive Services](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-detect) to detect the language of some text.


Check the presentation for this project : [Language Detector - Module Polyglotte presentation](https://fleuryc.github.io/oc_ingenieur-ia_P1-decouvrez-le-metier-d-ingenieur-ia/index.html)


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

### CLI : Input text

Run `python detector-cli.py --text TEXT` to detect the language of the text passed as an argument.

```bash
$ python detector-cli.py --text "We are the knights who say 'Ni!'"
> Detected language : en
```

### CLI : Random text from dataset

Run `python detector-cli.py` to detect the language of a random line of text in one of the most spoken languages (en, zh, hi, es, ar and fr) from the dataset (`data/x_test.txt`).

```bash
$ python detector-cli.py
> Text : عملية التقويم أي إذا كان هناك درجات للنشاط يحاسب عليها التلميذ في تقصيره وتفاعلة أداء ذلك إلى التحاق بالنشاط و الإمكانيات المتاحة أي إذا كان هناك توفير الأدوات والأنشطة وتوفرت الأماكن كان النشاط كثير و أخيراً التوجيه نحو الإنجاز بمعنى إذا قام المدير بتكريم أداء ذلك إلى تفعيل النشاط.
>
> Expected language : ar
> Detected language : ar
> Result: SUCCESS
```

### Test

Run `pytest` to check that the language of the most spoken languages is correctly detected.
