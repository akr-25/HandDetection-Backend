# HandDetection-Backend

## Installation

Step 1: Clone the repository
Step 2: Initialize virtual environment using ```py -3 -m venv venv```
Step 3: Activate virtual environment using ```venv\Scripts\activate```
Step 4: Install dependencies with ```pip install -r requirements.txt```
Step 5: Set environment variables, for powershell:

- ```$env:FLASK_ENV = "development"```
- ```$env:FLASK_APP = "run.py"```

Step 6: Fill config.demo.py (in ./handDetector) with your credentials and rename it to config.py
Step 7: Run the application using ```flask run```
