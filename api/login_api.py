import requests
import config
def login(session, email, password):
    data = {
        "email":email,
        "password":password
    }
    response = session.post(f"{config.BASE_URL}/api/login",json = data)
    return response

def register(session, email, password):
    data = {
        "email":email,
        "password":password
    }
    response = session.post(f"{config.BASE_URL}/api/register",json = data)
    return response


