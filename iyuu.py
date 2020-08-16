import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class iyuu(object):
    token = None
    def __init__(self, IYUU_TOKEN):
        self.token = f"https://iyuu.cn/{IYUU_TOKEN}.send"

    def __call__(self, text, desp=""):
        Form = {'text': text, 'desp': desp}
        return requests.post(self.token, data=Form, headers={'Content-type': 'application/x-www-form-urlencoded'}, verify=False)

if __name__ == "__main__":
    info = iyuu('IYUU2325Tb0e7aff495efcced893463190750ecbefe0ae8ae')
    info('Host online', 'send by python')