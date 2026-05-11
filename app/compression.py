class MemoryCompression:

    def compress(self, text):

        words = text.split()

        if len(words) <= 20:
            return text

        return " ".join(words[:20]) + "..."
