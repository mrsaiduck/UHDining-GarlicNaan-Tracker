# UHDining-Indian-Tracker

Craving the delicious flavor of Garlic Naan and want to be notified when it's available in your University of Houston dining hall? Look no further! This web scraper, the UHDining Indian Tracker, automatically checks the menus of UHDining locations once a day and sends you an email alert if there's freshly baked Garlic Naan, along with details on where to find it.

## Features
- Automated daily checks for the presence of Garlic Naan in popular UHDining locations.
- Email notifications sent directly to your inbox with the location and mealtime details.

## Why Garlic Naan?
Garlic Naan, a delightful Indian bread, is a flavor sensation! Our tracker ensures you stay in the loop, never missing the chance to enjoy the delectable taste of freshly baked Garlic Naan.

## How it Works
The web scraper navigates through the UHDining website, scanning menus at locations like Moody Towers 24/7 Dining Commons. If Garlic Naan is spotted during lunch or dinner, you'll receive an email notification to satisfy your cravings.

## Setup Instructions
1. Clone this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Create a `.env` file in the project root with the following content:

   ```dotenv
   # .env

   # Set your Gmail credentials
   ADMIN_EMAIL=your@gmail.com
   ADMIN_PASSWORD=your_app_password

   # Set the recipient email(s) for notifications
   RECEIVE_EMAILS=recipient1@example.com,recipient2@example.com
4. Run the script with `py main.py` and await your daily Garlic Naan alert!