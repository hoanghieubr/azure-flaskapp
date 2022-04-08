import requests
id = input("Product ID: ")
result = requests.get(f"http://zmapi.azurewebsites.net/api/product/{id}").json()
print(result['name'])
