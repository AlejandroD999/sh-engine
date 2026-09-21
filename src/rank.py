from difflib import SequenceMatcher 

class Ranker:
    def __init__(self, data, keyword):
        self._data = data
        self.keyword = keyword
    
        self.setup_scores() 

    def get_data(self):
        return self._data

    def setup_scores(self):
        # TODO Exception handling? 

        keyword = self.keyword.strip().lower()
             
        for item in self._data:
            title = item['title'].strip().lower()

            ratio = SequenceMatcher(None, title, keyword).ratio()
            item['score'] = ratio

    def sort(self):
        # score based on proximity to keyword
        # if 'matt' is keyword 'matt' has a score of 1, meanwhile mater is some other nomber of matchin letters
        pass
