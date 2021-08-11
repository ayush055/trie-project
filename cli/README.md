#  Py-Trie

Py-Trie is a command-line interface which enables communication with a global trie hosted on the Google Cloud Platform. Users can execute basic commands such as inserting, deleting, and searching words in the trie. A list of matching words can be generated through an input prefix. Users are also able to display the words present in the trie.

## Requirements


The following are required to be installed on your system before using Py-Trie:

* Python 3.8 or higher
* Pip

## Installation

To install Py-Trie, run the following command:

```
pip install py-trie
```

## Testing Suite

There are several test cases that can be found in the `test.py` file located in the `cli/pytrie` folder. These tests execute the commands listed in the Usage section. Some tests also simulate multiple users sending requests to the server by running processes on different threads.

To run all the test cases with the trie, run:

```
py-trie test
```

## Usage

There are 5 basic commands that can be executed using Py-Trie:
* Insert
* Remove
* Search
* Autocomplete
* Display

To get a list of all possible commands, run:

```
py-trie --help
```

### Insert

To insert a word:

```
py-trie insert [WORD]
```

### Remove

To remove a word:

```
py-trie remove [WORD]
```

### Search

To search a word:

```
py-trie search [WORD]
```

### Autocomplete

To generate a list of matching words based on a prefix:

```
py-trie autocomplete [PREFIX]
```

### Display

To display all existing words in the trie:

```
py-trie display
```