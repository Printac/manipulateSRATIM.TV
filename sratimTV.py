from time import sleep
import pip._vendor.requests as requests

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
URL_AUTH = token_time_auth[token_time_auth.index('?'):-3]

print(f"{WATCH_URL}{movie_id}.mp4{URL_AUTH}")
print(session.get(f"{WATCH_URL}{movie_id}.mp4{URL_AUTH}").status_code)


#get request to the movie url gets an status code 200(OK) but when opening it in broswer gets error 401
#TO DO: FIX --- 401 Authorization Required -- only when copying url to broswer 
