# Accessing the Apple iTunes Search Service

In this assignment you are going to build a Python program to access the
[Apple iTunes Search Service](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html).
This service can be used to search information about musicians, albums, songs and so on.

Using the following URL a search for the term _ramones_ and for the entity type
_album_ is performed:
[https://itunes.apple.com/search?term=ramones&entity=album](https://itunes.apple.com/search?term=ramones&entity=album)

Other possible entity types are musicArtist, musicTrack or song. Below is an (abbreviated)
example result of the service:

```json
{
  "resultCount": 1,
  "results": [
    {
      "wrapperType": "collection",
      "collectionType": "Album",
      "artistId": 60715,
      "amgArtistId": 5223,
      "artistName": "Ramones",
      "collectionName": "Ramones",
      "collectionPrice": 9.99,
      "collectionExplicitness": "notExplicit",
      "trackCount": 14,
      "copyright": "℗ 1976 Sire Records. Marketed by Rhino Entertainment Company, a Warner Music Group Company.",
      "country": "USA",
      "currency": "USD",
      "releaseDate": "1976-04-23T08:00:00Z",
      "primaryGenreName": "Punk"
    }
  ]
}
```

The response in the example above consist of one result (`resultCount` is 1). This result is the album
"Ramones" (element `collectionName`) by the artist "Ramones" (element `artistName`)
The response is in [JSON](https://en.wikipedia.org/wiki/JSON) format.

The [Requests](https://docs.python-requests.org/en/latest/)
library is used to inoke the Apple iTunes Search Service.
In order to perform a search a Get-request needs to be performed. This is one using the `get()` function.
After that the method `json()` of the Requests
library can be used to mapped the response from JSON to Python data types `dict` and `list`.

## Assignment

Write a program that asks the user for a search term. Perform a search using the iTunes search service
for the entity type album. Teh program should then print how many serach results where returned.
For each result print the artist name, the album name and track count.

Below is an example execution of the program. Note that the output is abbreviated.

```
Please enter a search term: cash
The search returned 50 results.
Artist: Luke Bryan - Album: Crash My Party - Track Count: 13
Artist: Johnny Cash - Album: The Essential Johnny Cash - Track Count: 36
Artist: Dave Matthews Band - Album: Crash - Track Count: 12
...
```
