from query_handler_base import QueryHandlerBase
import requests
import json

class TranslateHandler(QueryHandlerBase):
	def can_process_query(self, query):
		if "translate" in query:
			return True
		return False

	def process(self, query):
		try:
			result = self.call_api()
			translation = result["data"]["translatedText"]
			self.ui.say(translation)
		except:
			self.ui.say("Oh no! There was an error trying to contact Translate api.")
	def call_api(self):
		url = "https://text-translator2.p.rapidapi.com/translate"

		text = input("Input string to translate: ")

		payload = {
			"source_language": "en",
			"target_language": "hr",
			"text": f"{text}"
			}
		headers = {
			"content-type": "application/x-www-form-urlencoded",
			"X-RapidAPI-Key": "041d4bffadmsh54d6ef9d2437b3ep18bd10jsnc77e8bae94c7",
			"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
		}

		response = requests.post(url, data=payload, headers=headers)

		return json.loads(response.text)