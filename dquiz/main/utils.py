import requests
from bs4 import BeautifulSoup
from django.conf import settings


def get_answer(description):
	headers = {'User-Agent': 'Mozilla/5.0'}
	raw = requests.post(settings.ANSWER_URL, headers=headers, data={'question': description})
	soup  = BeautifulSoup(raw.text, 'html.parser')
	html_answer = soup.find("code")
	return html_answer.text
