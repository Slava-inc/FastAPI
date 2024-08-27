# Info

| | |
|:---|:---|
| Author | V. Danchenko |
| Task   | New mountain pass addition in DB |
| Description | Users are tourists. They insert pass infomation in mobile app | 

# User registation

![](images/register.png?raw=true)


| Request | Reply |
|:---|:---|
| curl -X 'POST' 
  'http://127.0.0.1:8000/register/?username=user2&email=user2%40example.com&password=123' 
  -H 'accept: application/json' 
  -d '' | "user user2 registered!" |
