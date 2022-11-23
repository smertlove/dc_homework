import requests
from pprint import pprint

def main():
    responce = requests.get("https://jsonplaceholder.typicode.com/posts")
    pprint(responce)

if __name__ == "__main__":
    main()
