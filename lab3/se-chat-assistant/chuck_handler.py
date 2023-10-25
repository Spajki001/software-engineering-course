from query_handler_base import QueryHandlerBase
import requests
import json

class ChuckHandler(QueryHandlerBase):
	def can_process_query(self, query):
		if "chuck" in query:
			return True
		return False
	
	def process(self, query):
		try:
			result = self.call_api()
			fact = result["value"]
			self.ui.say(fact)
		except:
			self.ui.say("Oh no! There was an error trying to contact Chuck Norris api.")

	def call_api(self):
		url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

		headers = {
			"accept": "application/json",
			"X-RapidAPI-Key": "041d4bffadmsh54d6ef9d2437b3ep18bd10jsnc77e8bae94c7",
			"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
		}

		response = requests.get(url, headers=headers)

		return json.loads(response.text)