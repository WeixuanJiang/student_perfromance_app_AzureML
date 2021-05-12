import urllib.request
import json
import os
import ssl
import logging as lg

class Inference:

    def __init__(self):
        self.url = None
        self.key = None
        self.headers = None
        self.data = None
        self.request = None
        self.body = None

    def allowSelfSignedHttps(self,allowed=True):
        # bypass the server certificate verification on client side
        if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
            ssl._create_default_https_context = ssl._create_unverified_context

    def input_url_key(self,url,key):
        self.url = url
        self.key = key

    def input_data(self,
                   schools,
                   sex,
                   age,
                   address,
                   famsize,
                   parent_cohabitation_status,
                   mother_education,
                   father_education,
                   Mjob,
                   Fjob,
                   reason,
                   guardian,
                   traveltime,
                   studytime,
                   failures,
                   schoolsup,
                   famsup,
                   paid,
                   activities,
                   nursery,
                   higher,
                   internet,
                   romantic,
                   famrel,
                   freetime,
                   goout,
                   Dalc,
                   Walc,
                   health,
                   absences):
        data = {
            "data":
            [
                {
                    'school': schools,
                    'sex': sex,
                    'age': age,
                    'address': address,
                    'famsize': famsize,
                    'parent_cohabitation_status': parent_cohabitation_status,
                    'mother_education': mother_education,
                    'father_education': father_education,
                    'Mjob': Mjob,
                    'Fjob': Fjob,
                    'reason': reason,
                    'guardian': guardian,
                    'traveltime': traveltime,
                    'studytime': studytime,
                    'failures': failures,
                    'schoolsup': schoolsup,
                    'famsup': famsup,
                    'paid': paid,
                    'activities': activities,
                    'nursery': nursery,
                    'higher': higher,
                    'internet': internet,
                    'romantic': romantic,
                    'famrel': famrel,
                    'freetime': freetime,
                    'goout': goout,
                    'Dalc': Dalc,
                    'Walc': Walc,
                    'health': health,
                    'absences': absences,
                },
            ],
        }
        self.data = data
        self.body = str.encode(json.dumps(self.data))
        self.headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + self.key)}
        self.request = urllib.request.Request(self.url, self.body, self.headers)

    def get_result(self):
        try:
            response = urllib.request.urlopen(self.request)
            result = response.read()
            return result
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))
        
            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(json.loads(error.read().decode("utf8", 'ignore')))