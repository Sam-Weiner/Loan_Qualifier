# Loan Qualifier

This is an app for evaluating loan opportunities based on the criteria of a collection of banks.  
A user would be able to input their financial information and be offered a list of banks where they would qualify for their desired loan.  

---

## Technologies

- Python 3.7

- **[fire](https://google.github.io/python-fire/guide/)** - Users will use the command line interface offered by this package.

- **[questionary](https://questionary.readthedocs.io/en/stable/)** - Provides interactive dialogues for the CLI.

- **[pytest](https://docs.pytest.org/en/6.2.x/)** - Used for testing purposes.
---

## Installation Guide

Please install the following dependencies prior to use.

```python
pip install fire
pip install questionary
pip install pytest
```

---

## Examples of Code Functionality

The main assignment that was asked of us in this week's challenge was to add the ability to save the results of this app as a .csv file.  
To do this we are using the `csv` library, specifically the `csv.writer` functionality and `.writerow` function.

![csvwriter_image](/images/readme_csvwriter_code.PNG)

---

## Usage

The user will first be prompted to enter a path to the bank information that has each banks loan criteria.  
For the purposes of this assignment, the bank info is located in *data/daily_rate_sheets.csv*

![retrieving-bank-data](/images/readme_enter_path_for_bank_info.PNG)

Next the user will be asked to input their own financial information.

![user-info](/images/readme_user_info.PNG)

The app then calculates and reports the users monthly debt-to-income ratio and their loan-to-home-value ratio.  
After scanning the list of banks along with their criteria, the app reports a list of banks where the user is qualified for their desired loan.  
Then the user is asked whether they would like to save this data in a more easy to read format.  

![data-output](/images/readme_raw_data_output.PNG)

If the user selected 'Yes', the app then asks the user where they would like to save their .csv file.  

![where-to-save](/images/readme_where_to_save.PNG)

With the file saved, the app closes itself in the terminal.



---

## Contributors

Sam Weiner - Developer (in training)
Built using code contributed by UC Berkeley Extension

---

## License

MIT
