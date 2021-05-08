from fastapi import FastAPI
from bs4 import BeautifulSoup
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import requests

# start fastapi 
app = FastAPI()

db = []
class Abstract(BaseModel): 
    text: str

# endpoints 
# get request 
# fastAPI will automatically expect something that is an "abstract" to be in the body of the request
@app.get('/abstract/{tag}')
def get_abstract(tag: str): 
    templateURL = "https://en.wikipedia.org/wiki/"
    url = templateURL + tag
    html = requests.get(url) 
    html_text = "none"
    if(html.status_code==200): 
        html_text = requests.get(url).text
    else: 
        print(f"Failed get request from webpage with code {html.status_code}")
        exit(0)

    # format the text in lxml format 
    soup = BeautifulSoup(html_text, "lxml")

    # gets all text content from page
    content = soup.find('div', class_ ='mw-parser-output')

    # gets all top level 'p' tags, which holds all the text
    paragraphs = content.find_all('p', recursive=False)
    

    for i in range(3): 
        # get the first paragraph tag that has content, this is usually the abstract
        if(len(paragraphs[i]) > 1): 
            firstParagraph = paragraphs[i].get_text()
            break

    return firstParagraph


# url = 'https://en.wikipedia.org/wiki/Lexus_F'
# url = 'https://en.wikipedia.org/wiki/WWE'
# url = 'https://en.wikipedia.org/wiki/Wally_Buhaj'
# url = 'https://en.wikipedia.org/wiki/Lexus_IS_(XE20)'