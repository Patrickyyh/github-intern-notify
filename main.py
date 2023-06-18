
import requests
import datetime
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv()
GIHUB_TOKEN = os.getenv('GITHUB_TOKEN')
"""
    send email from the script
"""
def send_email(from_email, to_email, subject, body):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    email_body = MIMEText(body, 'plain')
    msg.attach(email_body)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    #TLS connection
    s.starttls()
    s.login(from_email, "mqnjwmzbdegjuwgc")
    s.sendmail(from_email, to_email, msg.as_string())
    s.quit()


## https://github.com/bsovs/Fall2023-Internships
def get_github_commit():
    url  = 'https://api.github.com/repos/pittcsc/Summer2024-Internships/commits'
    headers = {'Authorization':f'{GIHUB_TOKEN}'}
    response  = requests.get(url,headers = headers)
    response.raise_for_status()
    commit_data = response.json()
    return datetime.datetime.strptime(commit_data[0]['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')


def main():
    last_check_time = None
    FROM_EMAIL = "yeyuhao1998@gmail.com"
    TO_EMAIL   = "yeyuhao1998@gmail.com"
    SUBJECT    = "Github Update notification!!"
    BODY       = "Githob update notification!!"
    # print(get_github_commit())
    while True:
        try:
            latest_commit_time  = get_github_commit()
            print(latest_commit_time)
            if not last_check_time or latest_commit_time > last_check_time:
                send_email(FROM_EMAIL , TO_EMAIL , SUBJECT , BODY)
                last_check_time  = latest_commit_time
            time.sleep(60 * 60)
        except Exception as e:
            print(f'Error: {e}')




if __name__ == "__main__":
    main()

