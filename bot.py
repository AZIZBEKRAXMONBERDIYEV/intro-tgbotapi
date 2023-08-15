import requests


BASE_URL = 'https://api.telegram.org/bot'
TOKEN    = "6214348294:AAGnxgya_9o0i-uWMnIuqT0nuqG3VCCbjlg"


def getMe() -> dict:
    '''getting info about the bot'''
    url = f"{BASE_URL}{TOKEN}/getUpdates"                          

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return False

print(getMe())
