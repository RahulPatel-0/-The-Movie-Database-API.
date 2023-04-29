#!/usr/bin/env python
# coding: utf-8

# In[1]:


# api_key=62a19ed9d727c379e2419263f0828a4f


# In[2]:


import requests
import json


# In[3]:


response=requests.get('https://api.themoviedb.org/3/movie/550?api_key=62a19ed9d727c379e2419263f0828a4f')
print(response.url)


# In[4]:


data=response.json()
data


# # Find the 'id' of the movie "Andhadhun" using TMDb API.

# In[5]:


api_link = "https://api.themoviedb.org/3"
params = {'query':"Andhadhun", 'api_key':'62a19ed9d727c379e2419263f0828a4f'}
header = {'Accept': 'application/json'}

a = requests.get(api_link + "/search/movie", headers = header, params=params)
#print(a.url)
data=a.json()
p=data['results']
for i in p:
    print(i['id'])


# In[6]:


api_link = "https://api.themoviedb.org/3"
params = {'query':"Marvel Studios", 'api_key':'62a19ed9d727c379e2419263f0828a4f'}
header = {'Accept': 'application/json'}

a = requests.get(api_link , headers = header, params=params)
print(a.url)


# # Fetch the company id company 'Marvel Studios' using TMDb. Print the id.

# In[7]:


import requests
import json
api_key = "e226f4a5f5bace766952aa0d17182959" 
api_link = "https://api.themoviedb.org/3" 
params = {'query':"Marvel Studios", 'api_key':api_key} 
header = {'Accept': 'application/json'} 
response = requests.get(api_link + "/search/company", headers = header, params=params) 
data = response.json() 
results = data.get('results') 
for result in results:
    if result['name'] == 'Marvel Studios':
        print(result['id'])


# # Find the vote count and vote average of the movie "3 Idiots" using the TMDb API

# In[8]:


import requests
import json
api_link = "https://api.themoviedb.org/3"
params = {'query':"3 Idiots", 'api_key':'62a19ed9d727c379e2419263f0828a4f'}
header = {'Accept': 'application/json'}

a = requests.get(api_link + "/search/movie", headers = header, params=params)
data=a.json()
data=data['results']
for i in data:
    print(i['vote_count'])


# # Fetch the names of top 5 similar movies to 'Inception' from the TMDb API.

# In[9]:


import requests
import json
api_link = "https://api.themoviedb.org/3"
params = {'query':"Inception", 'api_key':'62a19ed9d727c379e2419263f0828a4f'}
header = {'Accept': 'application/json'}

a = requests.get(api_link + "/search/movie", headers = header, params=params)
data=a.json()
#print(a.url)
l=[]
data=data['results']
for i in data:
    p=i['original_title']
    if 'Inception' in p:
        l.append(i['original_title'])
for i in range(5):
    print(l[i])
    


# In[10]:


import requests
import json
url='https://api.themoviedb.org/3/movie/27205/similar'
h={'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
#print(a.url)
data=a.json()
data=data['results']
l=[]
for i in data:
    l.append(i['title'])
        
for i in range(5):
    print(l[i])


# # Fetch the top rated english movies in the US region using the TMDb API. From the result, print the first 10 movies which have original language as english. Also print their genres

# In[11]:


import requests


params = {"api_key":"10450dea05efda30124add40e8ac9e42","language":"en","region":"US"}
url = "https://api.themoviedb.org/3/movie/top_rated"
r = requests.get(url,params=params)

data = r.json()

films = []
genre_ids = []
count = 0

i=0
while count<10:
   
    if data["results"][i]["original_language"]=="en":
        
        films.append(data["results"][i]["title"])
        genre_ids.append(data["results"][i]["genre_ids"])
        count += 1
    i+=1

    
params = {"api_key":"10450dea05efda30124add40e8ac9e42"}
url = "https://api.themoviedb.org/3/genre/movie/list"
r = requests.get(url,params=params)
genres = r.json()

genres_d = {}
for genre in genres["genres"]:
    genres_d[genre["id"]]=genre["name"]
for m,i in zip(films,genre_ids):
    print(m,end=" - ")
    for id in i[:-1]:
        print(genres_d[id],end=", ")
      
    print(genres_d[i[-1]]+",")


# # Find the name and birthplace of the present most popular person according to TMDb API.

# In[12]:


import requests
import json
url = "https://api.themoviedb.org/3/person/"+str(id)
params = {"api_key":"10450dea05efda30124add40e8ac9e42"}#,"language":"en","region":"US"}
a=requests.get(url,params=params)
print(a.url)
data=a.json()

    


# In[13]:


import requests
import json
url = "https://api.themoviedb.org/3/person/popular"
params = {"api_key":"10450dea05efda30124add40e8ac9e42","language":"en","region":"US"}
a=requests.get(url,params=params)
#print(a.url)
data=a.json()
data=data['results']
for i in data:
    print(i['id'])
    print(i['name'])


# In[14]:


import requests
import json
url = "https://api.themoviedb.org/3/person/"+str(224513)
params = {"api_key":"10450dea05efda30124add40e8ac9e42"}#,"language":"en","region":"US"}
a=requests.get(url,params=params)
#print(a.url)
data=a.json()
print(data['id'])
print(data['name'],data['place_of_birth'])

    


# # Fetch the Instagram and Twitter handle of Indian Actress "Alia Bhatt" from the TMDb API.

# In[15]:


import requests
import json
url = "https://api.themoviedb.org/3/search/multi"
h={"api_key":"10450dea05efda30124add40e8ac9e42",'query':'Alia Bhatt'}
a=requests.get(url,params=h)
print(a.url)
data=a.json()
data


# In[16]:


import requests
import json
url = "https://api.themoviedb.org/3/person/1108120/external_ids"
h={"api_key":"10450dea05efda30124add40e8ac9e42",'query':'Alia Bhatt'}
a=requests.get(url,params=h)
#print(a.url)
data=a.json()
print(data['instagram_id'],data['twitter_id'])


# # Fetch the names of the character played by Tom Cruise in the movies:
# 
# Top Gun
# Mission: Impossible - Fallout
# Minority Report
# Edge of Tomorrow
# 

# In[17]:


import requests
import json
url = "https://api.themoviedb.org/3/search/person"
h={"api_key":"10450dea05efda30124add40e8ac9e42",'query':'Tom Cruise'}
a=requests.get(url,params=h)
print(a.url)


# In[18]:


url="https://api.themoviedb.org/3/search/movie"
h={"api_key":"10450dea05efda30124add40e8ac9e42",'query':'Top Gun'}
a=requests.get(url,params=h)
print(a.url)


# In[19]:


url='https://api.themoviedb.org/3/search/multi'
h={"api_key":"10450dea05efda30124add40e8ac9e42",'query':'Tom Cruise'}
a=requests.get(url,params=h)
print(a.url)
data=a.json()
data=data['results']
for i in data:
    print(i)


# In[20]:


import requests
import json
url="https://api.themoviedb.org/3/person/500/movie_credits"
h={"api_key":"10450dea05efda30124add40e8ac9e42",'query':'Tom Cruise'}
a=requests.get(url,params=h)
#print(a.url)
data=a.json()

for i in range(len(data['cast'])):
    if(data['cast'][i]['title']=='Top Gun'):
        print(data['cast'][i]['character'])
for i in range(len(data['cast'])):
    if(data['cast'][i]['title']=='Mission: Impossible - Fallout'):
        print(data['cast'][i]['character'])
for i in range(len(data['cast'])):
    if(data['cast'][i]['title']=='Minority Report'):
        print(data['cast'][i]['character'])
for i in range(len(data['cast'])):
    if(data['cast'][i]['title']=='Edge of Tomorrow'):
        print(data['cast'][i]['character'])


# # Did James McAvoy play a role in the movie Deadpool 2. Print Yes or No.

# In[21]:


url='https://api.themoviedb.org/3/search/movie'
h={'query':'Deadpool 2','api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
print(a.url)
data=a.json()
#for fetching the id:-383498


# In[22]:


#for movie detail
url='https://api.themoviedb.org/3/credit/str(383498)'
h={'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
a


# 

# In[23]:


import requests
import json
url='https://api.themoviedb.org/3/movie/383498/credits'
h={'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
print(a.url)
data=a.json()
data=data['cast']
l=[]
for i  in data:
     l.append(i['name'])
if 'James McAvoy' in l:
    print("Yes")
else:
    print("No")
        
    


# # Using the result obtained in previous question, find out if James McAvoy was credited for his role in movie Deadpool 2. Print Yes or No.

# In[24]:


import requests
import json
url='https://api.themoviedb.org/3/movie/383498/credits'
h={'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
print(a.url)
data=a.json()
data=data['cast']
# credit id:="5dff991126dac1001762a68f"


# In[25]:


url='https://api.themoviedb.org/3/credit/"5dff991126dac1001762a68f" '
h={'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
a


# In[26]:


url='https://api.themoviedb.org/3/movie/383498/credit/"5dff991126dac1001762a68f"'
h={'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
a


# In[27]:


url='https://api.themoviedb.org/3/movie/383498/credits'
h={'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
print(a.url)


# In[28]:


import requests
import json
credit="5dff991126dac1001762a68f"
url='https://api.themoviedb.org/3/credit/5dff991126dac1001762a68f'
h={'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
print(a.url)
data=a.json()
data=data['media']
if data['character']=="Charles Xavier (uncredited)":
    print("No")
else:
    print("Yes")


# # Fetch the overview of the TV Show "FRIENDS" using TMDb API.

# In[29]:


#url=https://api.themoviedb.org/3/person/tv_credits
import requests
import json
url="https://api.themoviedb.org/3/search/tv"
h={'query':'FRIENDS','api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
print(a.url)
data=a.json()
data=data['results']
for i in data:
    if i['name']=='Friends':
        print(i['overview'])


# # Fetch the name and air date of S06E05 of the TV Show 'The Big Bang Theory' from TMDb API.

# In[30]:


url='https://api.themoviedb.org/3/search/tv'
h={'query':'The Big Bang Theory' ,'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(url,params=h)
print(a.url)
#"id": 1418


# In[31]:


import requests
import json
u2='https://api.themoviedb.org/3/tv/1418/season/06/episode/05'
h={'api_key':'62a19ed9d727c379e2419263f0828a4f'}
a=requests.get(u2,params=h)
#print(a.url)
data=a.json()
print(data['name'],"-",data['air_date'])


# # Fetch the trending TV Shows for the week from the TMDb API and print the taglines of the top 5 shows. If there is no tagline, print 'Empty' instead

# In[32]:


import requests 
api_key = "e226f4a5f5bace766952aa0d17182959" 
api_link = "https://api.themoviedb.org/3" 
params = {'api_key':api_key} 
header = {'Accept': 'application/json'} 
response = requests.get(api_link + "/trending/tv/week", headers = header, params = params) 
data = response.json() 
results = data.get("results") 
ids=[] 
for result in results[:5]: 
    ids.append(result.get("id")) 
    
for id in ids: 
    response2 = requests.get(api_link + "/tv/" + str(id) , headers = header, params = params) 
    data2 = response2.json() 
    if (data2.get("tagline")) != "": 
        print(data2.get("tagline")) 
    else: 
        print('Empty')


# # Print the names of all the TV shows to be aired today whose original language is english.

# In[33]:


import requests
import json
url='https://api.themoviedb.org/3/search/tv'
h={'api_key':'62a19ed9d727c379e2419263f0828a4f','query':'en-US'}
a=requests.get(url,params=h)
print(a.url)
data=a.json()
data=data['results']
l=[]
n=[]
for i in data:
    if i['original_language']=='en':
        l.append(i['original_language'])
        n.append(i['name'])
for i in n:
    print(i)


# # Count the number of males and females in the cast of "Money Heist" using the TMDb API.

# In[34]:


import requests
## Write your code here
api_key = "e226f4a5f5bace766952aa0d17182959" 
api_link = "https://api.themoviedb.org/3" 
params = {'query':'Money Heist','api_key':api_key} 
header = {'Accept': 'application/json'} 
response = requests.get(api_link + '/search/tv/', headers = header, params = params) 
data = response.json() 
result=data.get('results')
if result is not None:
    for i in result:
        if i.get('name')=='Money Heist':
            id=i.get('id')    
params1={'id':id,'api_key':api_key}
response1 = requests.get(api_link + '/tv/' + str(id) + '/credits', headers = header, params = params1) 
data1 = response1.json() 
cast=data1.get('cast')
count_male=0
count_female=0
for c in cast:
    if c.get('gender')==1:
        count_female+=1
    if c.get('gender')==2:
        count_male+=1
print(count_male,count_female)


# In[ ]:




