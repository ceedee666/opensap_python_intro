import requests

search_term = input("Please enter a search term: ")

r = requests.get(f"https://itunes.apple.com/search?term={search_term}&entity=album")
result_json = r.json()

print(f'The search returned {result_json["resultCount"]} results.')
for result in result_json["results"]:
    print(
        f'Artist: {result["artistName"]} - Album: {result["collectionName"]} - Track Count: {result["trackCount"]}'
    )
