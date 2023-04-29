from requests_html import HTMLSession
from rake_nltk import Rake
import json


def extract_text(website_url):
    s = HTMLSession()
    response = s.get(website_url)
    return response.html.find('div#article-body', first=True).text

user_input = input("enter website url : ")
r = Rake()
r.extract_keywords_from_text(extract_text(user_input))
for rating, keyword in r.get_ranked_phrases_with_scores():
    if rating > 5:
      y=(rating,keyword)
      print(json.dumps(y))
      
# use this website link  in input "https://www.musicradar.com/reviews/tech/akg-c214-172209", as every website made with diiferent format in css class.
      
