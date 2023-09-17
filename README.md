# Password Strength Analyzer


> Analyze the strength of your passwords and improve your online security :))

---

## Description

The Password Strength Analyzer is a web-based application that allows users to assess the strength of their passwords quickly. With increasing cybersecurity threats, having a strong password is essential for online security. This tool helps users determine the quality of their passwords and provides suggestions for improvement.

---

## Demo

![Screenshot from 2023-09-17 07-46-27](https://github.com/naveenkumar20012/password_strength/assets/141645194/36753ec6-c58a-4fe4-84ee-9f5cb8b505ff)

---

## Features

- **Password Strength Analysis**: Evaluate the strength of your passwords based on criteria such as length, complexity, and character variety.
- **Password Suggestions**: Receive recommendations on how to make your password stronger, including adding special characters or increasing its length.
- **Task Queue (Celery)**: Utilizes Celery for asynchronous processing, ensuring that password analysis does not impact application performance.
- **Password History**: Maintain a history of password checks, allowing you to track improvements over time.
- **User Authentication**: Secure user authentication ensures that your password data remains private.
- **User-Friendly Interface**: An intuitive and user-friendly interface makes it easy for anyone to check their password strength. - but not implemented yet::
- **Open Source**: This project is open-source, allowing for community contributions and customization.

---

## Usage

- Visit the application's URL (e.g., http://localhost:8000).
- Sign up or log in to your account.
- Enter a password that you want to analyze.
- Click the "Check Password" button.
- Receive a password strength score and suggestions for improvement.

## Task Queue (Celery)
This project uses Celery for asynchronous password analysis. To start the Celery worker, use the following command:

# Start Celery worker

celery -A password_checker worker --loglevel=info

## Installation

Follow these steps to set up the Password Strength Analyzer locally:

```shell
# Clone the repository
git clone https://github.com/your-username/password-strength-analyzer.git

# Navigate to the project directory
cd password-strength-analyzer

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
