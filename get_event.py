import requests
import json


def get_events(username="EMMD474"):
    try:
        r = requests.get(f'https://api.github.com/users/{username}/events')
        if r.status_code == 200:
            events = r.json()
            if events:
                print("Displaying all events...")
                for event in events:
                    _type = event['type']
                    actor = event['actor']['login']
                    repo = event['repo']['name']
                    repo_link = event["repo"]['url']
                    if _type == "PushEvent":
                        payload_message = event['payload']['commits'][0]['message']
                    else:
                        payload_message = None
                    visibility = event['public']
                    created_at = event['created_at']

                    print(f"Actor: {actor}")
                    print(f"Type of Event: {_type}")
                    print(f'Repository: {repo}')
                    print(f"Repository url: {repo_link}")
                    if payload_message:
                        print(f"Commit message: {payload_message}")
                    print(f"Public: {visibility}")
                    print(f"Create At: {created_at}")
                    print("................................. \n")
            else:
                print("No events to display!")
        else:
            raise Exception(f'Request failed with status code: {r.status_code}')

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
