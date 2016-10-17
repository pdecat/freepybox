import requests
import json
from urllib.parse import urljoin

class Access:
    def __init__(self, base_url, session_token, http_timeout):
        self.header = {'X-Fbx-App-Auth': session_token}
        self.base_url = base_url
        self.timeout = http_timeout


    def get(self, end_url):
        '''
        Send get request and return results
        '''
        url = urljoin(self.base_url, end_url)
        r = requests.get(url, headers=self.header, timeout=self.timeout)
        resp = r.json()

        if resp['success'] != True:
            raise Exception('HTT Request failed : {0}'.format(resp['error_code']))

        if 'result' in resp:
            return resp['result']


    def post(self, end_url, payload=None):
        '''
        Send post request and return results
        '''
        url = urljoin(self.base_url, end_url)
        data = json.dumps(payload) if payload is not None else None
        r = requests.post(url, headers=self.header, data=data, timeout=self.timeout)
        resp = r.json()

        if resp['success'] != True:
            raise Exception('HTT Request failed : {0}'.format(resp['error_code']))

        if 'result' in resp:
            return resp['result']


    def put(self, end_url, payload=None):
        '''
        Send post request and return results
        '''
        url = urljoin(self.base_url, end_url)
        data = json.dumps(payload) if payload is not None else None
        r = requests.put(url, headers=self.header, data=data, timeout=self.timeout)
        resp = r.json()

        if resp['success'] != True:
            raise Exception('HTT Request failed : {0}'.format(resp['error_code']))

        if 'result' in resp:
            return resp['result']
