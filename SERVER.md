#  Server Documentation

## Hosting

For this project, the trie was hosted on the Google Cloud Platform, using Cloud Run. A Firebase database is used in conjunction with the server to store the words in the trie. When the server starts, all words are loaded from the database into one global trie that all users interact with. Code for the server can be found here: 

https://github.com/ayush055/trie-project/tree/main/server

## Client-Server Interaction


The trie application is implemented using a Flask app in Python. This app is deployed to Cloud Run using a Docker container. Services to the application are made available through REST API endpoints. The CLI interacts with the server through GET and POST requests. Before sending any requests to the server, the CLI validates the request by ensuring that words sent contain only alphabets.

### GET Requests

When the user searches for a word, uses autocomplete, or displays the trie, a GET request is sent to the server with the word as a query string (except for displaying, as a word is not required). <br>

`Example: https://trie-container-xuuikixata-uc.a.run.app/search?word=hello`

When displaying the trie, the server will traverse the trie and gather all the words present, returning them in a list such as this:

`["car", "pizza", "rocket"]`

### POST Requests

When the user inserts a word or removes a word, a POST request is sent to the server including the word in the body of the request as a JSON. If the word is successfully inserted or removed from the trie, a message such as this may be returned from the server:

`Successful Entry!` or `Successful deletion!`

## Curl Usage for REST API Endpoints


To test the REST API endpoints using curl, the following commands can be run:

### Insert

To insert a word:

```
curl -d '{"word": "pizza"}' -H 'Content-Type: application/json' https://trie-container-xuuikixata-uc.a.run.app/insert
```

Pass in the word of your choice for the `-d` option, keeping the JSON format.

### Remove

To remove a word:

```
curl -d '{"word": "pasta"}' -H 'Content-Type: application/json' https://trie-container-xuuikixata-uc.a.run.app/delete
```

Pass in the word of your choice for the `-d` option, keeping the JSON format.

### Search

To search a word:

```
curl https://trie-container-xuuikixata-uc.a.run.app/search?word=pizza
```

Ensure that the query string parameter `(?word=pizza)` points to the word of your choice.

### Autocomplete

To generate a list of matching words based on a prefix:

```
curl https://trie-container-xuuikixata-uc.a.run.app/autocomplete?word=p
```

Ensure that the query string parameter `(?word=p)` points to the prefix of your choice.

### Display

To display all existing words in the trie:

```
curl https://trie-container-xuuikixata-uc.a.run.app/display
```
