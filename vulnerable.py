# vulnerable.py
def get_user_data(username):
    query = "SELECT * FROM users WHERE name = '" + username + "';"
    print("Executing:", query)
    return query

get_user_data(input("Enter username: "))
