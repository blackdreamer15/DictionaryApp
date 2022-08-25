import requests
word = input('Enter a word').lower()
url = "https://wordsapiv1.p.rapidapi.com/words/" + word
print(url)

headers = {
	"X-RapidAPI-Key": "697a5e28c1mshe9455b0f5976c60p16167fjsnaa4655d71142",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)