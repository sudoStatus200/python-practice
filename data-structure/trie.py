class TrieNode:
    def __init__(self) -> None:
        self.children = [None for _ in range(26)]
        self.is_end_of_word = False


class Trie:

    def __init__(self) -> None:
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _chartoindex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):

        current_node = self.root

        for char in word:

            char_idx = self._chartoindex(char)
            if not current_node.children[char_idx]:
                current_node.children[char_idx] = self.get_node()
            current_node = current_node.children[char_idx]

        current_node.is_end_of_word = True

    def search(self, word):

        current_node = self.root

        for char in word:

            char_idx = self._chartoindex(char)

            if not current_node.children[char_idx]:
                return False

            current_node = current_node.children[char_idx]

        return current_node.is_end_of_word


def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()
