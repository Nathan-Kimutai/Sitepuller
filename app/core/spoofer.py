import requests

class CustomRequest(requests):
    """
    This is the custom request that will act like a browser to
    prevent other sites from blocking this request
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
