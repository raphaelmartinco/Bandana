def get_user(username):
    try:
       return users[username]
    except KeyError:
       return None


users = {
    "raphaelco@gmail.com":{"password":"rapha",
                         "first_name":"Raphael",
                         "last_name":"Co"},
    "iannapalacios@gmail.com":{"password":"kristiannaidapalacios",
                         "first_name":"Ianna",
                         "last_name":"Palacios"},
    "angeloong@example.com":{"password":"angelosyong",
                        "first_name":"Angelo",
                        "last_name":"Ong"},
   
}



