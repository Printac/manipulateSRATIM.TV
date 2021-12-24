from time import sleep
import pip._vendor.requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome()
sleep(5)
session = requests.Session()
MovieToWatch = input('{*} enter movie to watch: ')

MOVIE_NAME = {f"term": {MovieToWatch}}
SEARCH_MOOVIE_API = "https://api.sratim.tv/movie/search"
PRE_WATCH_API_TIMER = "https://api.sratim.tv/movie/preWatch"
WATCH_URL = "https://s1.sratim.tv/movie/SD/480/"

search_request = session.post(SEARCH_MOOVIE_API,MOVIE_NAME)
searchOutputs =  search_request.json()['results']
id_options = []
for i in searchOutputs:
        id_options.append(i['id'])
        print("ID : " + i['id'] + " - "+ i['name'][int(i['name'].find('/'))+1:])

movie_id = str(input("{*}enter movie id : "))
while movie_id not in id_options: movie_id = str(input('enter valid movie id : '))


TOKEN = str(session.get(PRE_WATCH_API_TIMER).text)

print("loading... 30 Sec remmaing..")
sleep(30)
token_time_auth = session.get(f"http://api.sratim.tv/movie/watch/id/{movie_id}/token/{TOKEN}").text
SRATIM_COOKIE = session.cookies.get_dict()
print(SRATIM_COOKIE)
COOKIE_DICT = {'name':'Sratim','value':SRATIM_COOKIE['Sratim'],'domain':'.sratim.tv'}
print(COOKIE_DICT)
URL_AUTH = token_time_auth[token_time_auth.index('?'):-3]

print(f"{WATCH_URL}{movie_id}.mp4{URL_AUTH}")

browser.get("http://sratim.tv")
browser.add_cookie(COOKIE_DICT)
browser.get(f"{WATCH_URL}{movie_id}.mp4{URL_AUTH}")


sleep(50)

