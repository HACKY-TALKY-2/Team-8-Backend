import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from course_detail_search import course_detail_search
import json
import os


keywords = ["업무자동화", "머신러닝", "딥러닝","웹개발","게임개발","앱개발","프론트엔드","백엔드","크롤링","데이터분석"]
base_url = "https://www.inflearn.com/courses?s="
course_info_list = []


def keyword_search(keywords):
  for keyword in keywords:
    search_query = base_url + quote(keyword) + "&page=" + str(1)    # base + keyword + page
    response = requests.get(search_query)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 강의 제목
    course_titles = soup.find_all('div', class_='course_title')
    
    # 강사
    instructors = soup.find_all('div', class_='instructor')
    
    # 강의 가격
    course_prices = soup.find_all('div', class_='price')
    
    # 강의 링크
    courses_card_list_body = soup.find('div', class_= 'courses_card_list_body')
    hrefs = courses_card_list_body.find_all('a', class_='course_card_front')
    
    
    for i in range(len(course_titles)):
      course_info = {}
      
      if course_titles[i]:
        course_info['title'] = course_titles[i].text.strip()
        course_info['keyword'] = keyword
        
      if hrefs[i]:
        
        course_info['link'] = hrefs[i]['href']
      if instructors[i]:
        course_info['lecturer'] = instructors[i].text.strip()
        
      if course_prices[i]:
        course_price = course_prices[i].text.strip()
        course_price = course_price.replace('₩', '')
        course_info['price'] = course_price
        

      course_info_list.append(course_info)


 
        
  return course_info_list

result = keyword_search(keywords)

print(result)



