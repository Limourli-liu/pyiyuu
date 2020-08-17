import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def iyuu(IYUU_TOKEN):
    url = f"https://iyuu.cn/{IYUU_TOKEN}.send"
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    def send(text, desp=""):
        Form = {'text': text, 'desp': desp}
        return requests.post(url, data=Form, headers=headers, verify=False)
    return send
if __name__ == "__main__":
    #get token via http://iyuu.cn/
    info = iyuu('IYUU2325Tb0e7aff495efcced893463190750ecbefe0ae8ae')
    info('Host online1', 'send by python')
    info('Host online2', 'send by python')