from difflib import SequenceMatcher 

class Ranker:
    def __init__(self, data):
        self.data = data
    
    def find_ratio(self, title, keyword):
        # TODO Exception handling? 

        title = title.strip().lower()
        keyword = keyword.strip().lower()
        
        return SequenceMatcher(None, title, keyword).ratio()

    def sort(self, keyword):
        # score based on proximity to keyword
        # if 'matt' is keyword 'matt' has a score of 1, meanwhile mater is some other nomber of matchin letters
        pass
        
if __name__ == "__main__":
    r = Ranker("")

    print(r.find_score("Some guy named Matt", "Matt"))
