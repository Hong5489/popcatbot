import requests
import time

# Edit here
captcha_token = ""
token = ""
# Note pop count maximum is 800
pop_count = 800

total = 0
headers = {
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Origin': 'https://popcat.click',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://popcat.click/',
    'Accept-Language': 'en-GB,en;q=0.9',
}

params = (
    ('pop_count', str(pop_count)),
    ('captcha_token', captcha_token),
    ('token', token),
)


while(1):
    response = requests.post('https://stats.popcat.click/pop', headers=headers, params=params)
    if response.status_code == 201:
        total += pop_count
    else:
        print("Error: "+response.text)
    print("Total poped: "+str(total))
    # Note minimum time is 30s per IP address
    time.sleep(30)