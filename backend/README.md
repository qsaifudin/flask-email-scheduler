# Backend Flask Email Scheduler

## Author

- **Saifudin**
  - Email: qsaifudin.official@gmail.com
  - LinkedIn: [https://www.linkedin.com/in/qsaifudin/](https://www.linkedin.com/in/qsaifudin/)
  - Personal Web: [https://qsaifudin.site/](https://qsaifudin.site/)

## System Requirements
Ensure that your system meets the following requirements:

- python
- pip

## Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Initialize database
   ```bash
   python init_db.py
   ```


## Usage
1. Navigate to the backend directory
   ```bash
   cd backend
   ```
2. Run the application using the following command:
   ```bash
   python run.py
   ```
   The application will be accessible at http://localhost:5000 by default. You can customize the port by changing the value in the .env file.

## Testing
1. Navigate to the backend directory
   ```bash
   cd backend
   ```
2. Run the testing using the following command:
   ```bash
   python -m pytest tests/
   ```

## API Endpoints

### save email
- Method: POST
- URL: `localhost:5000/save_emails`
- Description: Endpoint to save an email with provided data.
- Request Body:
   ```json
   {
    "event_id": "1",
    "email_subject": "halo",
    "email_content": "ini halo",
    "timestamp": "11 Feb 2025 12:03"
   }
   ```
### Get All Emails
- Method: GET
- URL: `localhost:5000/emails/all`

### Toggle Email Scheduler
- Method: POST
- URL: `localhost:5000/toggle_email_scheduler?enabled=on`
- Description: Endpoint to toggle the email scheduler on/off.