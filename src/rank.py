from difflib import SequenceMatcher 
from .data.db import fetch_articles
from .data.wiki_api import get_new_articles 

class Ranker:
    def __init__(self, data, keyword):
        self.data = data
        self.keyword = keyword
    
        if self.setup_scores(): 
            self.sorted = self.sort(self.data)
        else:
            self.sorted = None


    def setup_scores(self, _retried=False):
        keyword = self.keyword.strip().lower()

        for item in self.data or []:
            title = item.get('title') if isinstance(item, dict) else None

            if not isinstance(title, str):
                continue
            title = title.strip().lower()
            item['score'] = round(SequenceMatcher(None, title, keyword).ratio(), 2)

        if self.data:
            return True

        if _retried:
            print(f"Could not find: {self.keyword}")
            return False

        print("Data not found, attempting to update database")
        if self.update_data():
            return self.setup_scores(_retried=True)
    

    def update_data(self):
         
        if get_new_articles(self.keyword):
            self.data = fetch_articles(self.keyword) 
            return True 
        return False


           
    def sort(self, arr):
        if not arr:
            return arr

        # score based on proximity to keyword
        # if 'matt' is keyword 'matt' has a score of 1, meanwhile mater is some other nomber of matchin letters
         
        for i in range(len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j]['score'] < key['score']:
                arr[j + 1] = arr[j]
                arr[j] = key
                j -= 1

        return arr

