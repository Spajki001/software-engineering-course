from query_handler_base import QueryHandlerBase
import requests
import json

class CurrencyHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "currency" in query:
            return True
        return False
    
    def process(self, query):
        try:
            value = query.split()[1]
            result = self.call_api(value)*100
            self.ui.say(f"{value} EUR is {result} GBP")
        except:
            self.ui.say("Oh no! There was an error trying to contact Currency api.")
            
    def call_api(self, value):
        url = "https://currency-exchange.p.rapidapi.com/exchange"
        
        querystring = {"from":"EUR","to":"GBP","q":f"{value}"}
        
        headers = {
			"X-RapidAPI-Key": "041d4bffadmsh54d6ef9d2437b3ep18bd10jsnc77e8bae94c7",
			"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
		}
        
        response = requests.get(url, headers=headers, params=querystring)
        
        return json.loads(response.text)