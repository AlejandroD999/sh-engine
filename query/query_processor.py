from nltk.stem.snowball import SnowballStemmer 
from spellchecker import SpellChecker

class QueryProcessor:
    # Architecural style: Pipeline
    def __init__(self, query):
        # TODO Language detection

        self.query = query
        self.language = "english" 
        self.checker = SpellChecker(language="en")
        
        self.__processed = self.process()
     
    def segment_query(self):
        return self.query.split() if type(self.query) == str else None

    def spell_check(self, split_query):
        # TODO Improve spell check accuracy

        if not split_query:
            print("Spell check error: missing query")
            return 

        long_word_length = 4


        for idx, word in enumerate(split_query):
            # Toggle check distance: according to word length
            self.checker.distance = 1 if len(word) <= long_word_length else 2

            if word not in self.checker:
                corr_word = self.checker.correction(word)

                if corr_word:
                    split_query[idx] = corr_word
        
        return split_query
        
    def stem(self, query):
        snowball = SnowballStemmer(self.language)
        
        # Basic Error Handling
        if not query:
            print("Stem error: a query must be provided")
            return

        if type(query) != list:
            print("Stem error: query must be a list")
            return
        
        # Stem process
        for idx, word in enumerate(query):
            stemmed = snowball.stem(word)
            query[idx] = stemmed 

        return query
         
    
    def process(self):
        # Transforms and filters query
        
        # Phase 1: Segment query
        split_query = self.segment_query() 
             
        # Phase 2: Spellcheck
        corrected_query = self.spell_check(split_query)
        
        # TODO Phase 3: Filter stop words

        # Phase 4: Stem query
        stemmed_query = self.stem(corrected_query)
    
        return stemmed_query

    def get_processed(self):
        return self.__processed 

