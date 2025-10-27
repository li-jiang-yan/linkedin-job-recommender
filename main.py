import requests
import bs4

# Define constants
KEYWORDS = ""
LOCATION = "Singapore%2C%20Singapore"
URL = "https://www.linkedin.com/jobs/search?keywords={}&location={}&f_E=2".format(KEYWORDS, LOCATION)

# Get response from server
response = requests.get(URL)
while response.status_code != 200:
    response = requests.get(URL)

# Pass response content into bs4.BeautifulSoup
soup = bs4.BeautifulSoup(response.content, "html.parser")

# Define custom classes to help
class Employer():
    """Custom class for an employer in a job search result on LinkedIn"""

    def __init__(self, tag: bs4.element.Tag):
        self.name = tag.string.strip()

class JobSearchResult():
    """Custom class for a job search result on LinkedIn"""

    def __init__(self, tag: bs4.element.Tag):
        self.title = tag.find("h3", class_="base-search-card__title").string.strip()
        self.href = tag.find("a", class_="base-card__full-link").get("href")
        self.read_info()

    def read_info(self):
        """Read more information on the job search result"""
        info_response = requests.get(self.href)
        while info_response.status_code != 200:
            info_response = requests.get(self.href)
        info_soup = bs4.BeautifulSoup(info_response.content, "html.parser")
        self.employer = Employer(info_soup.find("a", class_="sub-nav-cta__optional-url"))
        self.description = info_soup.find("div", class_="show-more-less-html__markup")

# Get list of job search results
job_results = [JobSearchResult(tag) for tag in soup.find("ul", class_="jobs-search__results-list").find_all("li")]
