from query_handler_base import QueryHandlerBase
import requests
import json

class LoveHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "love" in query:
            return True
        return False

    def process(self, query):
        names = query.split()
        fname = names[1]
        sname = names[2]

        try:
            result = self.call_api(fname, sname)
            score = result["percentage"]
            text = result["result"]
            self.ui.say(f"Love score between {fname} and {sname} is {score}%")
            self.ui.say(f"The doctor said: {text}")
        except: 
            self.ui.say("Oh no! There was an error trying to contact Love api.")
            self.ui.say("Try something else!")



    def call_api(self, fname, sname):
        url = "https://love-calculator.p.rapidapi.com/getPercentage"

        querystring = {"fname":fname,"sname":sname}

        headers = {
                "X-RapidAPI-Key": "0a79803ed3mshc384cde749c0e05p119b5ajsnc9242f1839cf",
                "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return json.loads(response.text)
