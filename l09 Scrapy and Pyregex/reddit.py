import requests
import re

url = 'https://www.reddit.com/r/Python/comments/7wv6jb/building_daw_with_python/'

def get_comments(url):
    page = requests.get(url)
    content = page.content    
    #print(start_content)
    with open('content.txt', mode='w') as file:
        file.write(str(start_content))
     users = re.findall(r'https://www.reddit.com/user/(\w+)', str(content))

    


get_comments(url)