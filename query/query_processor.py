from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker

class QueryProcessor:
    # Architecural style: Pipeline
    def __init__(self, query):
        self.query = query
        self.checker = SpellChecker(language="en")
        
        self.run()
     
    def segment_query(self):
        return self.query.split()

    def spell_check(self, split_query):
        long_word_length = 4


        for idx, word in enumerate(split_query):
            # Toggle check distance: according to word length
            self.checker.distance = 1 if len(word) <= long_word_length else 2

            if word not in self.checker:
                corr_word = self.checker.correction(word)

                if corr_word:
                    split_query[idx] = corr_word
        
        return split_query
        
    def lemmatize(self, query):
        
        if len(query) < 1 or type(query) != list:
            print("Stemming error")
            return

        wln = WordNetLemmatizer()
        
        for idx, word in enumerate(query):
            lemma = wln.lemmatize(word)

            print(lemma)
            

    
    def run(self):
        # Transforms and filters query
        split_query = self.segment_query() 
        
        corrected_query = self.spell_check(split_query)

        lemmatized_query = self.lemmatize(corrected_query)



if __name__ == "__main__":
    qp = QueryProcessor("Pizza tastses awsome, ct and minws")
