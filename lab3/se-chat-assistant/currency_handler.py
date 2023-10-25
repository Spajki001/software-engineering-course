from query_handler_base import QueryHandlerBase
import requests
import json

class CurrencyHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "exchange" in query:
            return True
        return False
    
    def process(self, query):
        try:
            currency = query.split()
            currency1 = currency[1]
            currency2 = currency[2]
            result = self.call_api(currency1, currency2)
            self.ui.say(f"The exchange rate between {currency1} and {currency2} is {result}.")
        except:
            self.ui.say("Oh no! There was an error trying to contact Currency api.")
            
    def call_api(self, currency1, currency2):
        url = "https://currency-exchange.p.rapidapi.com/exchange"
        
        querystring = {"from":f"{currency1}","to":f"{currency2}","q":"1"}
        
        headers = {
			"X-RapidAPI-Key": "041d4bffadmsh54d6ef9d2437b3ep18bd10jsnc77e8bae94c7",
			"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
		}
        
        response = requests.get(url, headers=headers, params=querystring)
        
        return json.loads(response.text)