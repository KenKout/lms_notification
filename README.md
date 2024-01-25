
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

## Setup on Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FKenKout%2Flms_notification%2F&env=WEBHOOK,USERNAME,PASSWORD)

After deploying this script, make sure you do this:
- https://{url}/get: Come to browser and enter this url until it returns : **Crawl Successfully**

### Keeping the Script Running 24/7 with UptimeRobot

  To ensure the script runs continuously, follow these steps:
  
  1. Go to [UptimeRobot](https://uptimerobot.com/) and create a free account.
  
  2. After logging in, click on **+ Add New Monitor**.
  
  3. Choose **HTTP(s)** as the monitor type.
  
  4. In the **Monitor Name** field, give your monitor a name (e.g., LMS Notification).
  
  5. In the **URL (or IP)** field, paste the Vercel project URL and add **/recheck**. Example: your-domain.vercel.app/recheck
  
  6. Set the **Check Interval** to 5 minutes.
  
  7. Click **Create a Monitor**.

  8. For example, if you have 21 course, create 3 monitors. Because each run it will check 10 links, so it need 3 monitors.
  
  Now, UptimeRobot will ping your Vercel project every 5 minutes, keeping it active.
  
## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/KenKout/lms_notification
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

## Notes

- This script is provided as-is, and the developer is not responsible for any misuse or damage caused by it.
- Use responsibly and adhere to the terms of service of the platforms being accessed.

Feel free to contribute to the project or report issues on the [GitHub repository](https://github.com/KenKout/lms_notification).
