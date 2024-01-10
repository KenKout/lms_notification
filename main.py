import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import json
import time
import random 
import os

Debug = False
replit = os.getenv('WEBHOOK')
webhook_url = os.getenv('WEBHOOK')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
course_link = []
course_data = []
def login_sso():
    url = "https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    resp = s.get(url, headers=headers).text
    lt = resp.split('<input type="hidden" name="lt" value="')[1].split('" />')[0]
    execution = resp.split('<input type="hidden" name="execution" value="')[1].split('" />')[0]
    data = f"username={username}&password={password}&execution={execution}&_eventId=submit&submit=Login&lt={lt}"
    resp2 = s.post(url, headers=headers, data=data)
    print('Function - Login: Success')
def crawl_e_learning_link():
    global course_link
    login = s.get('https://lms.hcmut.edu.vn/login/index.php?authCAS=CAS')
    if 'Error: Database connection failed' not in login.text:
        sess_key = login.text.split('sesskey=')[1].split('"')[0]
        print(sess_key)
        get_course = s.post(f'https://lms.hcmut.edu.vn/lib/ajax/service.php?sesskey={sess_key}&info=core_course_get_enrolled_courses_by_timeline_classification', json=[{"index":0,"methodname":"core_course_get_enrolled_courses_by_timeline_classification","args":{"offset":0,"limit":0,"classification":"all","sort":"fullname","customfieldname":"","customfieldvalue":""}}])
        #print(get_course.text)
        if get_course.json()[0]['error'] == False:
            for course in get_course.json()[0]['data']['courses']:
                if str(course['id']) not in course_link:
                    course_link.append(course['viewurl'])
                    print(course['viewurl'] + ' - ' + course['fullname'] + ' - is added')
                else:
                    print('Course already exists')
        return sess_key
def crawl_data_courses(sess_key):
    global course_data
    for link in course_link:
        #data = s.get(link).text.replace(" ", "").replace("\n", "")
        data =  BeautifulSoup(s.get(link).text,'html.parser').select_one('ul.topics[data-for="course_sectionlist"]')
        #print(data.prettify())
        json = {'id': link.split('id=')[1], 'data': data}
        course_data.append(json)
        #print(json)

def convert_to_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <ul> elements with the 'topics' class
    ul_elements = soup.find_all('ul', class_='topics')

    # Initialize an empty list to hold the parsed data
    parsed_data = []

    # Iterate over all <ul> elements
    for ul in ul_elements:
        # Find all <li> elements within the <ul> with the 'section' class
        li_elements = ul.find_all('li', class_='section', recursive=False)
        # Iterate over each <li> element
        for li in li_elements:
            # Extract the section number from the data-sectionid attribute
            section_number = li.get('data-sectionid', 0)

            # Find all cmitem elements within the section
            cm_items = li.find_all('li', attrs={"data-for": "cmitem"})

            # Iterate over each cmitem
            for cm_item in cm_items:
                # Extract the data-id attribute
                item_id = cm_item.get('data-id')

                # Initialize the URL as an empty string
                url = ""

                # Try to find the <a> tag with the URL and extract it
                a_tag = cm_item.find('a', href=True)
                if a_tag and 'href' in a_tag.attrs:
                    url = a_tag['href']
                title = None
                # Extract the title from the data-activityname attribute or from the text content
                title_area = cm_item.find('div', class_="activity-name-area")
                if title_area:
                    title = title_area.get_text(strip=False)
                if not title:
                    title = cm_item.get_text(strip=True)

                # Append the parsed data to the list
                parsed_data.append({
                    "section": int(section_number),
                    "data": {
                        "item": int(item_id),
                        "title": title.strip(),
                        "url": url
                    }
                })

    # Convert the parsed data to JSON
    # json_data = json.dumps(parsed_data)
    # Return the JSON data
    return parsed_data


def compare_json(old,new):
    # Convert the old data into a set of item IDs for faster lookup
    old_item_ids = set(item['data']['item'] for item in old)
    # Initialize a list to hold new items
    new_items = []

    # Iterate through the items in the new data
    for item in new:
        # Check if the item ID is not in the set of old item IDs
        if item['data']['item'] not in old_item_ids:
            # If it's not, then it's a new item
            new_items.append(item)
    return new_items

def send_notification_discord(item):
    title = item['data']['title']
    url = item['data']['url']
    payload = {
        "content": "",
        "tts": False,
        "embeds": [
            {
                "title": f"{title}",
                "description": f"Click title to check new content.",
                "color": random.randint(1000000, 9999999),
                "fields": [],
                "url": url
            }
        ],
        "components": [],
        "actions": {},
        "username": "E-Learning Notification",
        "avatar_url": "https://message.style/app/logo.svg"
    }
    
    response = requests.post(webhook_url, json=payload)
    
    if response.status_code == 204:
        print(f"Message sent for {title}")
    else:
        print(f"Failed to send message for {title}")

def recheck_data(sess_key):
    global course_data
    for i in range(len(course_data)):
        link = 'https://lms.hcmut.edu.vn/course/view.php?id=' + course_data[i]['id']
        #data = s.get(link).text.replace(" ", "").replace("\n", "")
        data =  BeautifulSoup(s.get(link).text,'html.parser').select_one('ul.topics[data-for="course_sectionlist"]')
        json = {'id': link.split('id=')[1], 'data': data}
        if str(data) not in str(course_data[i]['data']):
            json_old = convert_to_json(str(course_data[i]['data']))
            json_new = convert_to_json(str(data))
            diff_results = compare_json(json_old,json_new)
            for result in diff_results:
                send_notification_discord(result)
                time.sleep(1)
            course_data[i] = json
            print('New data added')
        else:
            if Debug:
                json_old = convert_to_json(str(course_data[i]['data']))
                for result in json_old:
                    send_notification_discord(result)
                    time.sleep(2)
            print('Data already exists')

s = requests.session()
login_sso()
sess_key = crawl_e_learning_link()
crawl_data_courses(sess_key)
if not replit:
    while True:
      recheck_data(sess_key)
else:
    from flask import Flask
    app = Flask('')
    @app.route('/')
    def main():
        return "alive"
    def run():
        app.run(host="0.0.0.0", port=8080)
    def keep_alive():
        server = Thread(target=run)
        server.start()
    keep_alive()
    while True:
      recheck_data(sess_key)
