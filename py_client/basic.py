import requests 

# endpoint = "https://httpbin.org/200/"
endpoint = "http://localhost:8000/api/"



get_response = requests.post(endpoint, json={"product_id": 123 }) # HTTP Request 
# print(get_response.text) #print raw text response


print(get_response.json())
# HTTPS REQUEST -> HTML 
# REST API HTTP REQUEST -> JSON

