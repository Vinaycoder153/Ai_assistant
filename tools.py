import asyncio
import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun
import os
import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from typing import Optional
from dotenv import load_dotenv
from email.message import EmailMessage
from datetime import datetime

load_dotenv()

# Instantiate once at module level to avoid per-call overhead
_search_tool = DuckDuckGoSearchRun()


@function_tool()
async def get_weather(
    context: RunContext,  # type: ignore
    city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        # Run the blocking HTTP call in a thread pool to avoid blocking the event loop
        response = await asyncio.to_thread(
            requests.get, f"https://wttr.in/{city}?format=3"
        )
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.strip()   
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: {e}")
        return f"An error occurred while retrieving weather for {city}." 

@function_tool()
async def search_web(
    context: RunContext,  # type: ignore
    query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """
    try:
        # Reuse the module-level instance; run in a thread pool to avoid blocking
        results = await asyncio.to_thread(_search_tool.run, query)
        logging.info(f"Search results for '{query}': {results}")
        return results
    except Exception as e:
        logging.error(f"Error searching the web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'."    

@function_tool()    
async def send_email(
    context: RunContext,  # type: ignore
    to_email: str,
    subject: str,
    message: str,
    cc_email: Optional[str] = None
) -> str:
    """
    Send an email through Gmail.
    
    Args:
        to_email: Recipient email address
        subject: Email subject line
        message: Email body content
        cc_email: Optional CC email address
    """
    try:
        # Gmail SMTP configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        # Get credentials from environment variables
        gmail_user = os.getenv("GMAIL_USER")
        gmail_password = os.getenv("GMAIL_APP_PASSWORD")  # Use App Password, not regular password
        
        if not gmail_user or not gmail_password:
            logging.error("Gmail credentials not found in environment variables")
            return "Email sending failed: Gmail credentials not configured."
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Add CC if provided
        recipients = [to_email]
        if cc_email:
            msg['Cc'] = cc_email
            recipients.append(cc_email)
        
        # Attach message body
        msg.attach(MIMEText(message, 'plain'))
        
        # Connect to Gmail SMTP server and send in a thread pool
        def _send():
            smtp = smtplib.SMTP(smtp_server, smtp_port)
            try:
                smtp.starttls()
                smtp.login(gmail_user, gmail_password)
                smtp.sendmail(gmail_user, recipients, msg.as_string())
            finally:
                smtp.quit()

        await asyncio.to_thread(_send)
        logging.info(f"Email sent successfully to {to_email}")
        return f"Email sent successfully to {to_email}"
        
    except smtplib.SMTPAuthenticationError:
        logging.error("Gmail authentication failed")
        return "Email sending failed: Authentication error. Please check your Gmail credentials."
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
        return f"Email sending failed: SMTP error - {str(e)}"
    except Exception as e:
        logging.error(f"Error sending email: {e}")
        return f"An error occurred while sending email: {str(e)}"
   
@function_tool()
async def get_current_time(
    context: RunContext  # type: ignore
) -> str:
    """
    Get the current time on the user's device.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Current time: {current_time}")
    return f"Current time is {current_time}"
    
    
@function_tool()
async def open_app(
    context: RunContext,  # type: ignore
    app_name: str) -> str:
    """
    Open an app on the user's device.
    """
    try:
        # Placeholder for actual app opening logic
        logging.info(f"Opening {app_name}")
        return f"Opening {app_name}..."
    except Exception as e:
        logging.error(f"Error opening {app_name}: {e}")
        return f"An error occurred while trying to open {app_name}."

@function_tool()
async def run_command(
    context: RunContext,  # type: ignore
    command: str) -> str:
    """
    Run a system command.
    """
    try:
        # Placeholder for actual command execution logic
        logging.info(f"Running command: {command}")
        return f"Running command: {command}"
    except Exception as e:
        logging.error(f"Error running command '{command}': {e}")
        return f"An error occurred while trying to run the command '{command}'."
    
@function_tool()
async def db_add_data(
    context: RunContext,  # type: ignore
    task: str,
    time: str) -> str:
    """
    Add a schedule entry to the database.
    """
    from db_driver import PersonalAssistantDB
    try:
        with PersonalAssistantDB() as db:
            db.add_schedule(task, time)
        logging.info(f"Added schedule: {task} at {time}")
        return f"Schedule added: {task} at {time}"
    except Exception as e:
        logging.error(f"Error adding schedule '{task}': {e}")
        return f"An error occurred while adding the schedule '{task}'."
   
@function_tool()
async def db_query_data(
    context: RunContext,  # type: ignore
    task: Optional[str] = None) -> str:
    """
    Query schedule entries from the database.
    
    Args:
        task: Optional task to filter results. If None, returns all schedules.
    """
    from db_driver import PersonalAssistantDB
    try:
        with PersonalAssistantDB() as db:
            # Use SQL-level filtering to avoid fetching all rows unnecessarily
            schedules = db.get_schedules_by_task(task) if task else db.get_all_schedules()
        if schedules:
            result = "\n".join([f"{s[1]} at {s[2]}" for s in schedules])
            logging.info(f"Queried schedules: {result}")
            return f"Schedules:\n{result}"
        else:
            return "No schedules found."
    except Exception as e:
        logging.error(f"Error querying schedules: {e}")
        return "An error occurred while querying schedules."

