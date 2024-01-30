import requests
import smtplib
import os
from bs4 import BeautifulSoup
from email.message import EmailMessage
from dotenv import load_dotenv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

sender_email = os.getenv('ADMIN_EMAIL')
sender_password = os.getenv('ADMIN_PASSWORD')
receive_email = os.getenv('RECEIVE_PASSWORD')

# URL of the webpage you want to scrape
url = 'https://dineoncampus.com/uh/whats-on-the-menu'

# Dining hall and meal times to check
dining_hall = 'Moody Towers 24/7 Dining Commons'
meal_times = ['Lunch', 'Dinner']

# Add more emails, and it will send separate messages to all emails
emails = [receive_email]

def send_email(msg):
    # Function to send emails
    for email in emails:
        message = EmailMessage()
        message['Subject'] = "Garlic Naan Found!"
        message['From'] = sender_email
        message['To'] = email
        message.set_content(msg)
        server = None
        # Connect to the SMTP server and send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
        finally:
            server.quit()

found = False
msg = ""

# This web scraper is unique to the University of Houston's dining website.
# Change where you look for content regarding the site you are looking on.

try:
    print(f"Start - {dining_hall}")
    # Send a GET request to the URL for the specific dining hall
    response = requests.get(f'{url}/{dining_hall}', verify=False)
    print("Good response")
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the HTML content
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the tabs for different meal times
        meal_tabs = soup.find_all('a', class_='tab-item')  # Adjust based on the actual HTML structure

        # Iterate through each meal time
        for meal_tab in meal_tabs:
            meal_time = meal_tab.text.strip()
            
            # Check if the meal time is in the list of times to check (e.g., Lunch, Dinner)
            if meal_time in meal_times:
                # Click on the tab to fetch the content for that meal time
                meal_response = requests.get(f'{url}/{dining_hall}/{meal_time}', verify=False)
                if meal_response.status_code == 200:
                    meal_html_content = meal_response.text
                    meal_soup = BeautifulSoup(meal_html_content, 'html.parser')

                    # Find all menu items or relevant elements based on the structure of the website
                    menu_items = meal_soup.find_all('div', class_='menu-item')  # Adjust based on the actual HTML structure

                    # Iterate through each menu item
                    for menu_item in menu_items:
                        # Check if the menu item contains "Garlic Naan"
                        if 'Garlic Naan' in menu_item.get_text():
                            print("Garlic Naan found!")
                            msg += f"Garlic Naan has been found at {dining_hall} during {meal_time}!\n"
                            found = True
                            break
                else:
                    print(f"Failed to fetch the webpage for {meal_time}. Status code: {meal_response.status_code}")

    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
except requests.RequestException as e:
    print(f"Error fetching the webpage: {e}")

# If no Garlic Naan was found
if not found:
    send_email("No Garlic Naan found during Lunch or Dinner at Moody Towers 24/7 Dining Commons :(")
else:
    send_email(msg)