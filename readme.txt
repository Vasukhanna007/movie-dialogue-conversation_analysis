
For code to work:

├── data
│   ├── clean_dialog.csv
│   └── words_alpha.txt
├── scripts
│   └── analysis.py
└── src
    └── hw3
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-38.pyc
        │   ├── follow_on_comments.cpython-38.pyc
        │   ├── mentions.cpython-38.pyc
        │   ├── non_dictionary_words.cpython-38.pyc
        │   ├── test.cpython-38.pyc
        │   └── verbosity.cpython-38.pyc
        ├── follow_on_comments.py
        ├── mentions.py
        ├── non_dictionary_words.py
        ├── test.py
        ├── tests
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-38.pyc
        │   │   └── all_tests.cpython-38.pyc
        │   ├── all_tests.py
        │   └── clean_dialog.csv
        └── verbosity.py


run the analysis.py script from scripts/ using command python analysis.py ../data/clean_dialog.csv 

run tests from src/hw3 using command python -m hw3.test

The tests contain a .csv file which is used for testing all the functions