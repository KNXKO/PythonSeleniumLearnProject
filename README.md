# Selenium Cookie Clicker Script

This script automates the gameplay of the Cookie Clicker game available at https://orteil.dashnet.org/cookieclicker/.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python
- Selenium library (`pip install selenium`)
- ChromeDriver (which is managed automatically by `webdriver_manager`)

## Description

The script performs the following tasks:

1. Opens the Cookie Clicker game page.
2. Handles the initial pop-up window if it appears.
3. Clicks the language selection button if available.
4. Starts clicking the cookie to accumulate cookies.
5. Automatically purchases available products when sufficient cookies are available.

## Usage

1. Clone or download the script.
2. Make sure you have Python and the required libraries installed.
3. Run the script using the Python interpreter (`python cookie_clicker.py`).

## Notes

- The script continuously clicks the cookie to accumulate cookies and automatically purchases products whenever enough cookies are available.
- It handles stale element reference exceptions that may occur during the automation process.
- Make sure to keep the Chrome window open while the script is running.