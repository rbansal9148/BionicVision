import requests

r = requests.post(
    # "https://api.deepai.org/api/neuraltalk",
	"http://localhost:1337/api/detectDeepAI",
    files={
    'image': open('./abc.jpg', 'rb')
    },
    # headers={'api-key': 'aedb7e46-3664-494b-b30d-dfa5dff0429d' }
)

print(r.json())
