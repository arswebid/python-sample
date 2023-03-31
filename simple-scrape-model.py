import requests
from bs4 import BeautifulSoup

# Make a request to the webpage
response = requests.get('https://example.com')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Print the href attributes of each link
for link in links:
    print(link.get('href'))
