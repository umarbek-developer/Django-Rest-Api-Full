import requests 

endpoint = "https://httpbin.org/200/"
endpoint = "https://google.com/"



get_response = requests.get(endpoint) # HTTP Request 
print(get_response.text) #print raw text response


# HTTPS REQUEST -> HTML 
# REST API HTTP REQUEST -> JSON

