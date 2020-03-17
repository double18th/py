import requests

#1
def crawl(base_url):
    response = requests.get( base_url )
    if response.status_code == 200:
        return response.text

if __name__ == "__main__":
    crawl()