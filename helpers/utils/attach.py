import allure
import requests
import os
from allure_commons.types import AttachmentType


def get_video_url(session_id: str):
    session = requests.Session()
    session.auth = (os.getenv('browserstack.user'), os.getenv('browserstack.key'))
    response = session.get(f'https://api.browserstack.com/app-automate/sessions/{session_id}.json')
    return response.json().get('automation_session').get('video_url')


def video(session_id: str, name: str):
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + get_video_url(session_id) \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, name, AttachmentType.HTML, '.html')
