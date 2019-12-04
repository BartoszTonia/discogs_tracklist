# discogs_tracklist

This is simple application to list all tracklists of your discogs collection / wantlist or any seller inventory

## Installation

Clone this repository and install discogs_client

```sh
git clone https://github.com/BartoszTonia/discogs_tracklist.git
pip install discogs_client
```
Run

```sh
$ python discogs_tracklist.py
```

## Usage
Copy token from your discogs account at https://www.discogs.com/settings/developers
```sh
Paste your token:
```
Then choose source and watch your output
```sh
Choose your input database:
 1 - wantlist
 2 - collection
 3 - seller inventory
```
Writing - for now just uncomment the line
```sh
    # tracklist.write()
```
ToDo:
- writing function
- pagination of inventory