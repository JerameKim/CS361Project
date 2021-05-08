from bs4 import BeautifulSoup
import re
import requests

class citation(object): 
    def __init__(self, link, text, id):
        self.link = link
        # gives all the text of the citation, stuff in quotes is the linked portion 
        # if nothing in quotes, whole thing is linked
        self.text = text
        self.id = id

# gets first paragraph in article
def get_abstract(tag): 
    # downloads article and gives response if it doens't work
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

# gets all the text in the article (including abstract)
def get_main_text(tag): 
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
    # paragraphs = content.find_all('p', recursive=False)
    paragraphs = content.find_all('p')


    # used to help remove brackets and their contents (regex)
    pattern = r'\[[^\]]*\]'
    for i in range(len(paragraphs)): 
        # removes HTML tags
        paragraphs[i] = paragraphs[i].get_text()
        # removes brackets and their contents 
        paragraphs[i] = re.sub(pattern, '', paragraphs[i])
        # print(paragraphs[i])

    return paragraphs

def get_citations(tag): 
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

    # gets all text content from citations
    content = soup.find('ol', class_ ='references')
    idx = 1

    citations = content.find_all('li')
    citation_obj_array = []
    citation_num = 1

    # creates array of objects
    for single_citation in citations: 
        empty_citation = citation("", "", citation_num)
        citation_num+=1
        citation_obj_array.append(empty_citation)

    single_counter = 0
    # grabs the relevant text 
    for single_citation in citations: 
        citation_text = single_citation.get_text()
        # ignore first 2 chars and remove \n
        citation_text = citation_text[2:].rstrip()
        # populate object
        citation_obj_array[single_counter].text= citation_text
        # print(citation_obj_array[single_counter].text)
        single_counter += 1


    link_counter = 0
    # if it exists, grabs the link associated to text 
    reference_wrapper = soup.find_all('span', class_="reference-text")
    for single_citation in reference_wrapper: 
        # if it has a link, add it 
        if single_citation.find_all('a', href=True):
        # if single_citation.find('cite'):
            for a in single_citation.find_all('a', href=True): 
                # print(a['href'])
                citation_obj_array[link_counter].link = a['href']
                link_counter +=1
                break
        else: 
            link_counter +=1
            continue

    for cit_obj in citation_obj_array: 
        print(f"Text: {cit_obj.text}")
        print(f"Link: {cit_obj.link}")
        print(f"Id: {cit_obj.id}")
        print()


def main(): 
    # tag = 'Lexus_F'
    # tag = 'WWE'
    # tag = 'Wally_Buhaj'
    tag = 'Lexus_IS_(XE20)'

    # abstract = get_abstract(tag)
    # main_text = get_main_text(tag)
    citations = get_citations(tag)
    # print(abstract)


if __name__ == "__main__": 
    main()
