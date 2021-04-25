
class Algorithm:

    def __init__(self, language, concept, excerpt):
        self.language = language
        self.concept = concept
        self.excerpt = excerpt

    def request_algorithm(self):
        link = f"https://github.com/loej/AlgoDS/blob/master/Algorithms/{self.language}/{self.language}%20-%20" \
               f"{self.concept}/{self.excerpt}.{str(self.language).lower()} "
        return link
