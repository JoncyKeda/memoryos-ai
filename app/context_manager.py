class ContextManager:

    def build_context(self, ranked_memories, top_k=3):

        context = []

        for memory, score in ranked_memories[:top_k]:

            context.append(memory[2])

        return "\n".join(context)
