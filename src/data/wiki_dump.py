import requests

def fetch_articles(keyword):
    if not keyword:
        print("A keyword must be provided")
        return
    
    url = f"https://en.wikipedia.org/w/rest.php/v1/search/page?q={keyword}"
    headers = {'User-Agent': 'sh-engine/0.0 (wikipedia:de; User:MoltenDev)'}
   
    try:
        res = requests.get(url, headers=headers, timeout=5)
        res.raise_for_status()

        return res.json()
    
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
    
    except requests.exceptions.MissingSchema as errmiss:
        print("Missing schema: include HTTP or HTTPS")

    except requests.exceptions.ConnectionError as conerr:
        print("Connection error")

    except requests.exceptions.RequestException as errex:
        print("Exception request")
        
# TODO Function to parse articles & another to submit into db

if __name__ == "__main__":
    arts = fetch_articles("jupiter")

    print(arts)
