import re

content = None

with open('ParseData.txt') as file:
    content = file.read()

def log(content):
    data = re.findall(r'\d{2}/[A-z]{3}/\d{4}', content)
    errors_location = re.findall(r'(([a-z]+\.*)+:\d+)', content)
    text = re.findall(r'(([A-Z]*\s)+\"\w*\"\s.*)', content)    


    print("""
    DATA: [{}] 
    {}

    ERROR LOCATION: [{}]
    {}
    """.format(len(data),data, len(errors_location), errors_location))
    
    #for text_item in text:
    print("TEXT")
    for text_item in text:
        print(text_item)
        


    

def main():
    log(content)

if __name__ == '__main__':
    main()