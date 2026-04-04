import config

def get_users(session, page=1):
    response = session.get(f"{config.BASE_URL}/api/users?page={page}")
    return response

def get_user(session, user_id):
    response = session.get(f"{config.BASE_URL}/api/users/{user_id}")
    return response


def update_user(session, user_id, name, job):
    json_data = {
        "name": name,
        "job": job
    }
    response = session.put(f"{config.BASE_URL}/api/users/{user_id}", json = json_data)
    return response


def delete_user(session, user_id):
    response = session.delete(f"{config.BASE_URL}/api/users/{user_id}")
    return response