from difflib import SequenceMatcher 

class Ranker:
    def __init__(self, data, keyword):
        self._data = data
        self.keyword = keyword
    
        self.setup_scores() 
        self.sorted = self.sort(self._data)

    def get_data(self):
        return self._data

    def setup_scores(self):

        try:
            keyword = self.keyword.strip().lower()

            for item in self._data:
                title = item['title'].strip().lower()

                ratio = SequenceMatcher(None, title, keyword).ratio()
                item['score'] = round(ratio, 2)
        except TypeError:
            print("Error: Data could not be found")
            return



    def sort(self, arr):
        if not arr:
            print("Sort error: missing array")
            return

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

