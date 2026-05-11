from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RankingEngine:

    def rank(self, query, memories):

        if not memories:
            return []

        documents = [m[2] for m in memories]

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform([query] + documents)

        similarities = cosine_similarity(
            vectors[0:1],
            vectors[1:]
        ).flatten()

        ranked = sorted(
            zip(memories, similarities),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked
