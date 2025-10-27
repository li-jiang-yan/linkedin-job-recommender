import requests
import bs4
import os

# Define constants
URL = "https://sg.linkedin.com/jobs/view/marketing-intern-category-management-travel-retail-at-parfums-christian-dior-4309522957?position=1&pageNum=0&refId=8SN5%2FjRs0cRNnEfmSHYg9Q%3D%3D&trackingId=djrAMd8ZYsnPRgd6z7r3fg%3D%3D"
FOLDERNAME = os.path.dirname(__file__)
FILENAME = os.path.join(FOLDERNAME, "response.html")

# Get response
response = requests.get(URL)

# Feed response into bs4.BeautifulSoup
soup = bs4.BeautifulSoup(response.content, "html.parser")

# Save prettified response into file
with open(FILENAME, "w", encoding="utf-8") as file:
    file.write(soup.prettify())
