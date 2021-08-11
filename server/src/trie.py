from node import *

class Trie():
    def __init__(self):
        self.root = Node()
        self.words = []

    def insert(self, word):
        parent_node = self.root

        # Iterates through the word and creates nodes in the trie if they do not already exist

        for char in word:
            char_index = ord(char) - 97
            child_node = parent_node.child_nodes[char_index]
            if not isinstance(child_node, Node):
                parent_node.child_nodes[char_index] = Node(parent=parent_node, data=char)
            parent_node = parent_node.child_nodes[char_index]
        
        # Adds word to trie by marking the node as "isWordEnd"
        if not parent_node.isWordEnd:
            parent_node.isWordEnd = True
            return True, "Successful Entry!"

        return False, "Word already exists"

    def autocomplete(self, prefix):
        # Finds final node of prefix in the trie
        last_node, _ = self.findFinalNode(prefix)
        if last_node == None:
            return "No matching words"
        
        # Generates a list of words by traversing the trie starting at last_node
        autocomplete_words = self.displayWords(last_node, '', [])
        autocomplete_words = [prefix + word for word in autocomplete_words]

        # Inserts the prefix into the list of autocomplete words
        # if the prefix is a word in the trie
        if last_node.isWordEnd:
            autocomplete_words.insert(0, prefix)
        return autocomplete_words

    def search(self, word):
        # Finds final node of prefix in the trie
        node, _ = self.findFinalNode(word)

        # If the node does not exist or it does not have a "isWordEnd" flag, 
        # then the word does not exist
        if node is None or not node.isWordEnd:
            return "False, word does not exist!"

        return "True, word found!"

    def delete(self, word):
        # Finds final node of prefix in the trie
        last_node, indices = self.findFinalNode(word)

        # If the node does not exist or it does not have a "isWordEnd" flag, 
        # then the word does not exist
        if last_node is None or not last_node.isWordEnd:
            return False, "Word not found"

        # If word exists, the "isWordEnd" flag is removed
        last_node.isWordEnd = False

        # If possible, nodes are deleted from the trie      
        self.deleteNode(last_node, indices)

        return True, "Successful Deletion!"

    def deleteNode(self, node, indices):

        # Base case - if the current node has child nodes, or it is the end of a word,
        # or it is the root node, it is not deleted
        if self.hasChildNodes(node) or node.isWordEnd or node is self.root:
            return
        
        # Get parent node
        parent_node = node.parent_node
        index = indices.pop(-1)

        # Delete child node of parent node
        parent_node.child_nodes[index] = None

        # Call method again using the parent node
        self.deleteNode(parent_node, indices)

    def findFinalNode(self, word):
        indices = []
        try:
            # Finds final node by traversing the trie based on the characters of the word
            node = self.root
            for char in word:
                char_index = ord(char) - 97
                indices.append(char_index)
                node = node.child_nodes[char_index]
            return node, indices
        except:
            # If an error is thrown during the trie traversal, then the word does not exist
            return None, None

    def hasChildNodes(self, node):
        return not all(child_node is None for child_node in node.child_nodes)

    def display(self):
        count = 0
        self.words = self.displayWords(self.root, '', [])
        return self.words

    def displayWords(self, node, word, wordList):
        # print("nodeid: ", id(node))
        # sys.stdout.flush()
        # Traverses the trie starting at node and finds all words that exist in the trie
        for child in node.child_nodes:
            if isinstance(child, Node):
                # Builds the word one letter at a time
                word += child.data

                # If the node is a "isWordEnd" node, add the word to wordList
                if child.isWordEnd and word not in wordList:
                    wordList.append(word)

                # Call the method again to continue traversing the trie
                self.displayWords(child, word, wordList)

                # Removes the last letter on word,
                # as a sibling node may have a different letter
                # that needs to be added to word
                word = word[:-1]
        
        return wordList