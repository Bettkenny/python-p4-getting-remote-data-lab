import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        
        if response.status_code == 200:
            return response.content  
            
            raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

        pass

    def load_json(self):
        response_body = self.get_response_body()
   
        try:
            json_data = json.loads(response_body.decode('utf-8'))  
            return json_data
        except json.JSONDecodeError as e:

            raise Exception(f"Failed to load JSON: {str(e)}")
        pass