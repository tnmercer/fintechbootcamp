# Loan Analyzer

Loan Analyzer is an interactive app used to filter qualifying bank loans and save them to a new CSV file.

The app reads data from a CSV file of available loans, filters based on user criteria and provides a list of qualifying loans with the option to save to a CSV.

---

## Technologies

This app is built using Python 3.7 with the following packages: 

* [Fire](https://github.com/google/python-fire) to create a command line interface (CLI) 
* [Questionary](https://github.com/tmbo/questionary) to allow the user to interact with the app and provide inputs through the CLI

---

## Installation Guide

Before using the app, run the following commands to install Fire and Questionary.

```
pip install fire
pip install questionary
```

---

## Usage

To use the app, clone the repository and run app.py.

```python app.py```

The CLI will run through various questions to collect data and confirm whether a CSV output is required. The screenshot below shows the questions and some example responses.

![CLI screenshot example of questions and answers.](images/terminal_screenshot.png)

---

## Contributors

This app was built by [Toni Mercer](https://www.linkedin.com/in/toni-mercer/) using the Starter Code from the UW FinTech Bootcamp course notes. 

---

## License

MIT