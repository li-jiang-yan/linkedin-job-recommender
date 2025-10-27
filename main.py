import requests
import bs4

# Define constants
KEYWORDS = ""
LOCATION = "Singapore%2C%20Singapore"
URL = "https://www.linkedin.com/jobs/search?keywords={}&location={}".format(KEYWORDS, LOCATION)

# Get response from server
response = requests.get(URL)

# Pass response content into bs4.BeautifulSoup
soup = bs4.BeautifulSoup(response.content, "html.parser")

# Define custom classes to help
class JobSearchResult():
    """Custom class for a job search result on LinkedIn"""

    def __init__(self, tag: bs4.element.Tag):
        self.href = tag.find("a", class_="base-card__full-link").get("href")
        self.title = tag.find("h3", class_="base-search-card__title").string.strip()
        self.employer = tag.find("h4", class_="base-search-card__subtitle").find("a").string.strip()

# Get list of job search results
job_results = [JobSearchResult(tag) for tag in soup.find("ul", class_="jobs-search__results-list").find_all("li")]
