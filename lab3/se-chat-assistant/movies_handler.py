from query_handler_base import QueryHandlerBase
import requests
import json

class MoviesHandler(QueryHandlerBase):
	def can_process_query(self, query):
		if "movies" in query:
			return True
		return False

	def process(self, query):
		try:
			result = self.call_api()
			for movie in result["results"]:
				title = movie["titleText"]["text"]
				self.ui.say(title)
		except:
			self.ui.say("Oh no! There was an error trying to contact Movies api.")

	def call_api(self):
		url = "https://moviesdatabase.p.rapidapi.com/titles/random"

		querystring = {"list":"most_pop_movies"}

		headers = {
			"X-RapidAPI-Key": "041d4bffadmsh54d6ef9d2437b3ep18bd10jsnc77e8bae94c7",
			"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
		}

		response = requests.get(url, headers=headers, params=querystring)

		return json.loads(response.text)
