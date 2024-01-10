
# LMS HCMUT Notification 

## Overview

This Python script is designed to monitor changes in your LMS courses and send notifications to a Discord channel when new content is detected. It utilizes web scraping techniques to compare the current course content with the previous state and notifies users of any updates.

## Features

- **Automatic Monitoring:** The script periodically checks for updates in your LMS courses.
- **Discord Notifications:** Notifications are sent to a Discord channel with details about the new content.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed
- Required Python packages installed (`requests`, `beautifulsoup4`, `Flask`)

## Setup on Replit

1. Fork this on Replit [repository](https://replit.com/@kenhcmut/lmsnotification).
   
2. Set up environment variables:

   - Click on the **Lock icon(Secrets)** on the left sidebar.
   - Click on **Environment Variables**.
   - Add the following variables:
     - `WEBHOOK`: Discord webhook URL for notifications.
     - `USERNAME`: Your LMS username.
     - `PASSWORD`: Your LMS password.
     - `replit`: true

3. Run the script:

   - Open the `main.py` file.
   - Click the green "Run" button at the top.
  
### Keeping the Script Running 24/7 with UptimeRobot

  To ensure the script runs continuously, follow these steps:
  
  1. Go to [UptimeRobot](https://uptimerobot.com/) and create a free account.
  
  2. After logging in, click on **+ Add New Monitor**.
  
  3. Choose **HTTP(s)** as the monitor type.
  
  4. In the **Monitor Name** field, give your monitor a name (e.g., LMS Notification).
  
  5. In the **URL (or IP)** field, paste the Replit project URL. You can find this URL by clicking on the "Run" button and copying the link.
  
  6. Set the **Check Interval** to 5 minutes.
  
  7. Click **Create a Monitor**.
  
  Now, UptimeRobot will ping your Replit project every 5 minutes, keeping it active.
  
## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/e-learning-notification-script.git
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - `WEBHOOK`: Discord webhook URL for notifications.
   - `USERNAME`: Your E-Learning username.
   - `PASSWORD`: Your E-Learning password.

4. Run the script:

   ```bash
   python main.py
   ```

## Configuration

You can customize the following parameters in the script:

- `Debug`: Set to `True` for additional debug information.
- `time.sleep(1800)`: Recheck interval (in seconds).

## Notes

- This script is provided as-is, and the developer is not responsible for any misuse or damage caused by it.
- Use responsibly and adhere to the terms of service of the platforms being accessed.

Feel free to contribute to the project or report issues on the [GitHub repository](https://github.com/KenKout/lms_notification).