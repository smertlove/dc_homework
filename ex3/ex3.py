import requests
import json
import pickle
from pprint import pprint

def main():

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    data = {user["id"]: {
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "posts": 0,
            "comments": 0
        } for user in json.loads(users.text)}
    ids = [id for id in data]

    for id in ids:
        posts = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}/posts")
        posts = json.loads(posts.text)
        data[id]["posts"] = len(posts)


    comments = requests.get(f"https://jsonplaceholder.typicode.com/comments")
    comments = json.loads(comments.text)

    for comment in comments:
        for id in data:
            if data[id]["email"] == comment["email"]:
                data[id]["comments"] += 1

    response = requests.post(
        "",  # сюда нужно воткнуть ссылку на вебхук (https://webhook.site/)
        data=json.dumps({"statistics": [data[id] for id in data]})
        )

    with open("solution.pickle", 'wb') as f:
        pickle.dump(response, f )




if __name__ == "__main__":
    main()
