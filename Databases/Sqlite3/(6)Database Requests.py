'''import requests

response = requests.get("https://ek.dk")
print(response.status_code)     # Prints 200 if things go well
print(response.text)            # Prints the content of the response in unicode
print(response.content)         # Prints the content of the response in bytes'''

import requests

payload = {'username': 'Alice', 'password': 'strongpassword'}

response = requests.post("https://httpbin.org/post", data=payload)

print(response.text)