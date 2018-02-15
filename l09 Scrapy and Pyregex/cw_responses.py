import urllib
import urllib3
import json
import requests
import re

__author__ = 'pospolitaki'

http = urllib3.PoolManager()


def get_wiki():
    """
    making requests by using urllib3 - not the best way
    """
    response = http.request('GET', 'https://habrahabr.ru/')
    print("!!! STATUS !!! {} !!! STATUS !!!".format( response.status))
    print("!!! DATA !!! {} !!! DATA !!!".format(response.data))
    print("!!! HEADERS !!! {} !!! HEADERS !!!".format( response.headers))

def get_hab():
    r = requests.get('https://habrahabr.ru/')
    print(r.status_code)
    print(r.headers)
    print('!!! CONTENT !!! {} !!! CONTENT !!!'.format(r.content))

def regular():
    name_pattern = r'My name is .*\.'
    patterns = ['My name is Kirill.', 'I i\'m just a string']
    for pattern in patterns:
        is_name = re.match(name_pattern, pattern)
        print('is_name:', bool(is_name))
        
    name_pattern_group = r'My name is (.*)\.'
    name = re.findall(name_pattern_group, patterns[0])
    print(name)

def main():
    #get_wiki()    
    #get_hab()
    regular()
if __name__ == '__main__':
    main()

"""
task on ragular ex in pythex:

1. to match data:
    \d{2}/[A-z]{3}/\d{4}

2. where occured:
    [\w]*\.[\w]*\.[\w]*\.[\w]*:\d*

3. to match text:
    ([A-Z]*\s)+\"\w*\"\s.*

[22/Jun/2017 13:53:22] DEBUG [django.db.backends.schema:103] CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
[22/Jun/2017 13:53:22] DEBUG [django.db.backends:90] (0.022) CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); args=None
[22/Jun/2017 13:53:22] DEBUG [django.db.backends.schema:103] ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params [])
[22/Jun/2017 13:53:22] DEBUG [django.db.backends:90] (0.001) ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_76bd3d3b_uniq" UNIQUE ("app_label", "model"); args=[]
"""
