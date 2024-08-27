# Info

| | |
|:---|:---|
| Author | V. Danchenko |
| Task   | New mountain pass addition in DB |
| Description | Users are tourists. They insert pass infomation in mobile app | 

# User registation

![](images/register.png?raw=true)


<table>
    <thead>
        <tr>
            <th>Request</th>
            <th>Reply</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>
             curl -X 'POST'<br> 
              'http://127.0.0.1:8000/register/?username=user2&email=user2%40example.com&password=123'<br> 
              -H 'accept: application/json'<br> 
              -d '' 
            </td>
            <td>"user user2 registered!"</td>
        </tr>
    </tbody>
</table>

# get information about mountain pass

![](images/get_map.png?raw=true)

| Request | Reply |
|:---|:---|
| curl -X 'GET' 
  'http://127.0.0.1:8000/submitData/<id>/?id=2' 
  -H 'accept: application/json' | {
  "add_time": "2021-09-22T13:18:13",
  "user_id": 1,
  "images": [
    {
      "id": 1,
      "title": "Седловина"
    },
    {
      "id": 2,
      "title": "Подъем"
    }
  ],
  "raw_data": {
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "",
    "coords": {
      "latitude": "45.3842",
      "longitude": "7.1525",
      "height": "1200"
    },
    "level": {
      "winter": "",
      "summer": "1А",
      "autumn": "1А",
      "spring": ""
    }
  },
  "id": 2,
  "status": "new"
} |