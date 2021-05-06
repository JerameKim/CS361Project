from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file: 
    content = html_file.read()
    
    # work with html tags as objects 
    # get content in xml format 
    soup = BeautifulSoup(content, 'lxml')
    # search for first specific tag
    # tags = soup.find('h5')
    # search for all h5 tags in doc 
    # courses_html_tags = soup.find_all('h5')

    # gets all courses w/ the class (card)
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards: 
        # get all h5 tags from course_cards
        # print(course.h5)
        # get all tags within a div with class 'card' 
        # print(course)
        course_name = course.h5.text
        # get last element of text in a tag in course 
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
    