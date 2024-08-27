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


<table>
    <thead>
        <tr>
            <th>Request</th>
            <th>Reply</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=32>
             curl -X 'GET'<br> 
              'http://127.0.0.1:8000/submitData/<id>/?id=2'<br> 
              -H 'accept: application/json' 
            </td>
            <td rowspan 32>
  { <br>
  "add_time": "2021-09-22T13:18:13", <br>
  "user_id": 1,  <br>
  "images": [ <br>
    { <br>
      "id": 1, <br>
      "title": "Седловина" <br>
    }, <br>
    { <br>
      "id": 2, <br>
      "title": "Подъем" <br>
    } <br>
  ], <br>
  "raw_data": { <br>
    "title": "Пхия", <br>
    "other_titles": "Триев", <br>
    "connect": "", <br>
    "coords": { <br>
      "latitude": "45.3842", <br>
      "longitude": "7.1525", <br>
      "height": "1200" <br>
    }, <br>
    "level": { <br>
      "winter": "", <br>
      "summer": "1А", <br>
      "autumn": "1А", <br>
      "spring": "" <br>
    } <br>
  }, <br>
  "id": 2, <br>
  "status": "new" <br>
}                 <br>
            </td>
        </tr>
    </tbody>
</table>
