# Python and REST APIs: Interacting With Web Services

It's not standard or protocol but just a set of design principle.

Python provides some great tools not only to get data from REST APIs but also to build your own Python REST APIs.

By using Python and REST APIs, you can retrieve, parse, update, and manipulate the data provided by any web service you’re interested in.

## REST Architecture

REST stands for representational state transfer and is a software architecture style that defines a pattern for client and server communications over a network.

### REST defines the following architectural constraints:
To promote performance, scalability, simplicity, and reliability in the system.

- Stateless: 
    The server won’t maintain any state between requests from the client.
- Client-server: 
    The client and server must be decoupled from each other, allowing each to develop independently.
- Cacheable: 
    The data retrieved from the server should be cacheable either by the client or by the server.

- Uniform interface: 
    The server will provide a uniform interface for accessing resources without defining their representation.
- Layered system: 
    The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.
- Code on demand (optional): 
    The server may transfer code to the client that it can run, such as JavaScript for a single-page application.

### REST APIs and Web Services
- A REST web service is any web service that adheres to REST architecture constraints.
- These web services expose their data to the outside world through an API. 
- REST APIs provide access to web service data through public web URLs.

### HTTP Methods

```
HTTP method             Description

GET	                    Retrieve an existing resource.
POST	                Create a new resource.
PUT	                    Update an existing resource.
PATCH	                Partially update an existing resource.
DELETE	                Delete a resource.
```

### Status Codes

```
Code    Meaning             Description

200	    OK	                The requested action was successful.
201	    Created             A new resource was created.
202	    Accepted	        Request received, but no modification has been made yet.
204	    No Content	        Request was successful, but the response has no content.
400	    Bad Request	        The request was malformed.
401	    Unauthorized	    Client isn't authorized to perform the requested action.
404	    Not Found	        The requested resource was not found.

415	    Unsupported Media	The request data format is not supported by the server.

422	    Unprocessable Entity Request data properly formatted but contained invalid or missing data.

500	    Internal Server Error	Server threw an error when processing the request.
```

### API Endpoints
A REST API exposes a set of public URLs that client applications use to access the resources of a web service. These URLs, in the context of an API, are called endpoints.

## REST and Python: Consuming APIs
To consume or use api endpoints, we use `requests` library in python.

> Installation: ```$ python -m pip install requests```

### GET
GET is a read-only operation, so you shouldn’t use it to modify an existing resource.

```
import requests as rq
api_url = "https://jsonplaceholder.typicode.com/todos/1"
res = rq.get(api_url)
print(f"Response: {res.json()}")
print(f"\nResponse Status Code: {res.status_code}")
print(f"\nResponse header: {res.headers["Content-Type"]}")
```

### POST
```
api_url = "https://jsonplaceholder.typicode.com/todos/"
todo = {'userId': 1, 'title': 'Hello', 'completed': False}
res = rq.post(api_url, todo)
print(res.status_code)
print(res.json())
```

We can even set headers :
```
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
```

### PUT
```
todo = {'userId': 154, 'title': 'Hello', 'completed': False}
api_url = "https://jsonplaceholder.typicode.com/todos/10"
res = rq.put(api_url, json=todo)
print(res.json())
print(res)
```

### PATCH
Patch differs from put as put changes the whole record or row while patch only changes the specific field.

```
todo = {'completed': True}
res = rq.patch(api_url, json=todo)
print(res.json())
print(res)
```

### DELETE
```
res = rq.delete(api_url)
print(res.json())
print(res)
```

## REST and Python: Building APIs

1. Identify Resources
2. Define Your Endpoints
    - GET url/guests
    - GET url/guests?event_id=23
3. Pick Your Data Interchange Format
    - SOAP with XML format
    - REST with JSON format 
4. Design Success Responses
    ```
    GET /cars HTTP/1.1
    Host: api.example.com
    ```
    This HTTP request is made up of four parts:
    - GET is the HTTP method type.
    - /cars is the API endpoint.
    - HTTP/1.1 is the HTTP version.
    - Host: api.example.com is the API host.

    -> These four parts are all you need to send a GET request to /cars.
    ```
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    [
        {
            "id": 1,
            "make": "GMC",
            "model": "1500 Club Coupe",
            "year": 1998,
            "vin": "1D7RV1GTXAS806941",
            "color": "Red"
        },
        {
            "id": 2,
            "make": "Lamborghini",
            "model":"Gallardo",
            "year":2006,
            "vin":"JN1BY1PR0FM736887",
            "color":"Mauve"
        }
    ]
    ```
    Here, Content-Type is imp. Similarly, we can do the same with other http methods.

5. Design Error Responses:
    Input:
    ```
    GET /motorcycles HTTP/1.1
    Host: api.example.com
    ```
    To send:
    ```
    HTTP/1.1 404 Not Found
    Content-Type: application/json
    {
        "error": "The requested resource was not found."
    }
    ```

#### Note
It’s very unlikely that your REST API will stay the same throughout the life of your web service. Resources will change, and you’ll need to update your endpoints to reflect these changes. This is where API versioning comes in. 

Most popular options for API versioning : 
- URI versioning
- HTTP header versioning
- Query string versioning
- Media type versioning


## REST and Python: Tools of the Trade

### Flask
Flask is a Python microframework used to build web applications and REST APIs.

> Installation: ```$ python -m pip install flask```

```
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415
```

> To run:
```
set FLASK_APP=app.py
C:\> set FLASK_ENV=development
flask run
```
