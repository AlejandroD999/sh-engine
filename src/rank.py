from difflib import SequenceMatcher 

class Ranker:
    def __init__(self, data):
        self._data = data
    
    def get_data(self):
        return self._data

    def find_score(self, title, keyword):
        # TODO Exception handling? 

        title = title.strip().lower()
        keyword = keyword.strip().lower()
        
        return SequenceMatcher(None, title, keyword).ratio()

    def sort(self, keyword):
        # score based on proximity to keyword
        # if 'matt' is keyword 'matt' has a score of 1, meanwhile mater is some other nomber of matchin letters
        for item in self._data:
            ratio = self.find_score(item['title'], keyword)
            item['score'] = ratio
        
        

