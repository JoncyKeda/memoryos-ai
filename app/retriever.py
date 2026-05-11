from app.ranking_engine import RankingEngine

class Retriever:

    def __init__(self):

        self.ranker = RankingEngine()

    def retrieve(self, query, memories):

        ranked = self.ranker.rank(query, memories)

        return ranked
