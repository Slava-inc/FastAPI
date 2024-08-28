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
            <th>Response</th>
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
            <th>Response</th>
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

# load new pass data

![](images/new_map_parameters.png?raw=true)

<table>
    <thead>
        <tr>
            <th>Request</th>
            <th>Response</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=16>
             curl -X 'POST'<br> 
            'http://127.0.0.1:8000/submitData/?data=%7B%20%09%22beautyTitle%22%3A%20%22%D0%BF%D0%B5%D1%80.%20%22%2C%20%09%22add_time%22%3A%20%222021-09-22%2013%3A18%3A13%22%2C%09%20%09%22raw_data%22%3A%7B%20%09%09%22title%22%3A%20%22%D0%9F%D1%85%D0%B8%D1%8F%22%2C%20%09%09%22other_titles%22%3A%20%22%D0%A2%D1%80%D0%B8%D0%B5%D0%B2%22%2C%20%09%09%22connect%22%3A%20%22%22%2C%20%09%09%22coords%22%3A%20%7B%20%09%09%09%22latitude%22%3A%20%2245.3842%22%2C%20%09%09%09%22longitude%22%3A%20%227.1525%22%2C%20%09%09%09%22height%22%3A%20%221200%22%20%09%09%09%7D%2C%20%09%09%22level%22%3A%20%7B%20%09%09%09%22winter%22%3A%20%22%22%2C%20%09%09%09%22summer%22%3A%20%221%D0%90%22%2C%20%09%09%09%22autumn%22%3A%20%221%D0%90%22%2C%20%09%09%09%22spring%22%3A%20%22%22%20%09%09%7D%09%09%20%09%09%7D%2C%20%09%22user%22%3A%201%2C%20%09%22images%22%3A%20%20%20%20%20%20%20%20%20%20%5B%7B%22id%22%3A%201%2C%20%22title%22%3A%22%D0%A1%D0%B5%D0%B4%D0%BB%D0%BE%D0%B2%D0%B8%D0%BD%D0%B0%22%7D%2C%20%20%20%20%20%20%20%20%20%20%20%7B%22id%22%3A%202%2C%20%22title%22%3A%22%D0%9F%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC%22%7D%5D%20%20%20%20%20%20%7D' <br> 
            -H 'accept: application/json' <br> 
            -H 'Content-Type: multipart/form-data' <br>
            -F 'files=@get_map.png;type=image/png' <br>
            -F 'files=@register.png;type=image/png'<br>
            </td>
            <td rowspan 5>
                {<br>
                "status": 200,<br>
                "message": null,<br>
                "id": 5<br>
                }<br>
            </td>
        </tr>
    </tbody>
</table>

# edit pass data

![](images/edit_map.png?raw=true)

<table>
    <thead>
        <tr>
            <th>Request</th>
            <th>Response</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=30>
                curl -X 'PATCH' <br>
                'http://127.0.0.1:8000/submitData/<id>/?id=5' <br>
                -H 'accept: application/json' <br>
                -H 'Content-Type: application/json'<br>
                -d '{ 	"beautyTitle": "пер. ", <br>
                    "add_time": "2021-09-28 09:18:13",<br>
                    "raw_data":{<br>
                        "title": "Пхия",<br>
                        "other_titles": "Триев", <br>		
                        "connect": "",<br>
                        "coords": {<br>
                            "latitude": "45.3842",<br>
                            "longitude": "7.1525",<br>
                            "height": "200"<br>
                            }, <br>		
                        "level": {<br>
                            "winter": "1B",<br>
                            "summer": "1А",<br>
                            "autumn": "1А",<br>
                            "spring": "1C"<br>
                            }<br>		 		
                            },<br>
                    "user": 1,<br>
                    "images":<br>
                        [<br>
                            {<br>
                            "id": 1,<br>
                            "title":"Спуск"},<br>
                            {"id": 2, "title":"Подъем"}<br>
                        ] }'<br>
            </td>
            <td rowspan 3>
                {<br>
                "state": 1,<br>
                }<br>
            </td>
        </tr>
    </tbody>
</table>

# user passes request

![](images/on_email_request.png?raw=true)

<table>
    <thead>
        <tr>
            <th>Request</th>
            <th>Response</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=32>
             curl -X 'GET'<br> 
            'http://127.0.0.1:8000/submitData/<email>?email=user%40example.com'<br>
            -H 'accept: application/json' <br> 
            </td>
            <td rowspan 32>
  { <br>
  "add_time": "2021-08-23T13:18:13", <br>
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
      "height": "1400" <br>
    }, <br>
    "level": { <br>
      "winter": "", <br>
      "summer": "1А", <br>
      "autumn": "1А", <br>
      "spring": "1B" <br>
    } <br>
  }, <br>
  "status": "new" <br>
},                 <br>
   "id": 5,<br>
    "raw_data": {<br>
      "title": "Пхия",<br>
      "other_titles": "Триев",<br>
      "connect": "",<br>
      "coords": {<br>
        "latitude": "45.3842",<br>
        "longitude": "7.1525",<br>
        "height": "200"<br>
      },<br>
      "level": {<br>
        "winter": "1B",<br>
        "summer": "1А",<br>
        "autumn": "1А",<br>
        "spring": "1C"<br>
      }<br>
    },<br>
    "status": "new"<br>
            </td>
        </tr>
    </tbody>
</table>

# error Resposes

## 