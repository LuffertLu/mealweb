import time
import requests
from requests.exceptions import TooManyRedirects

SESSION = requests.Session()
SESSION.max_redirects = 3

def requester(
        url,
        main_url=None,
        delay=0,
        cook=None,
        headers=None,
        timeout=10,
        host=None,
        user_agents=[None],
        failed=None,
    ):
    """Handle the requests and return the response body."""

    # Pause/sleep the program for specified time
    time.sleep(delay)

    def make_request(url):
        """Default request"""
        final_headers = headers or {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#            'Origin': 'https://codebeautify.org',
            'Connection': 'close',
        }
        try:
            response = SESSION.get(
                url,
                cookies=cook,
                headers=final_headers,
                verify=False,
                timeout=timeout,
                stream=True,
            )
        except TooManyRedirects:
            return 'dummy'

        if 'text/html' in response.headers['content-type'] or \
           'text/plain' in response.headers['content-type']:
            if response.status_code != '404':
                return response
            else:
                response.close()
                return 'dummy'
        else:
            response.close()
            return 'dummy'
    
    return make_request(url)

