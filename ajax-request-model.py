import requests

# Make an Ajax GET request to a URL
response = requests.get('https://example.com/api/data')

# Check the status code of the response
if response.status_code == 200:
    # If the response was successful, print the response content
    print(response.content)
else:
    # If the response was unsuccessful, print an error message
    print("Error:", response.status_code)
    
# Make an Ajax GET request with headers
headers = {'Authorization': 'Bearer <access_token>'}
response = requests.get('https://example.com/api/data', headers=headers)

# Make an Ajax POST request with data
data = {'name': 'John', 'age': 30}
response = requests.post('https://example.com/api/data', data=data)
