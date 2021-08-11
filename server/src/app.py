from flask import Flask, request
import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from trie import Trie

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "trie-2e59c",
})

db = firestore.client()
db_words = db.collection('words')

app = Flask(__name__)

def load_words():
  trie = Trie()
  word_docs = db_words.get()
  for word_doc in word_docs:
    word = word_doc.get('word')
    if word.isalpha():
      trie.insert(word.lower())
  return trie

def delete_words():
  word_docs = db_words.get()
  for word_doc in word_docs:
    word_doc.reference.delete()
  return "Deleted all documents"

# Load trie from Firebase
trie = load_words()

@app.route('/insert', methods=['POST'])
def insertWordApi():
    # global trie
    word = json.loads(request.data)['word']
    success, result = trie.insert(word)
    if success:
      db_words.add({
        'word': word
      })
    return result

@app.route('/delete', methods=['POST'])
def deleteWordApi():
    # global trie
    word = json.loads(request.data)['word']
    success, result = trie.delete(word)
    if success:
      docs = db_words.where(u'word', u'==', word).get()
      for doc in docs:
        doc.reference.delete()
    return result

@app.route('/search', methods=['GET'])
def searchTrieApi():
  # global trie
  word = request.args['word']
  result = trie.search(word)
  return result

@app.route('/autocomplete', methods=['GET'])
def autocompleteTrieApi():
  # global trie
  word = request.args['word']
  result = trie.autocomplete(word)
  if isinstance(result, list):
    result = json.dumps(result)
  return result

@app.route('/display')
def displayTrieApi():
  # global trie
  result = json.dumps(trie.display())
  return result

@app.route('/load', methods=['GET'])
def loadTrie():
  global trie
  trie = load_words()
  return "Loaded words"

@app.route('/empty', methods=['GET'])
def resetTrie():
  global trie
  delete_words()
  trie = load_words()
  return "Deleted and created empty trie"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))