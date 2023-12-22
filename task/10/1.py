'''
    Напишите программу,
    которая делает запрос к открытому API (например, GitHub API)
    и выводит информацию о пользователе
'''

import requests


def get_user_info(username):
    headers = {'Authorization': 'Bearer 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'}

    
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url, headers=headers)

    
    if response.status_code == 200:
        user_data = response.json()

        print(f"Username: {user_data['login']}")
        print(f"Name: {user_data['name']}")
        print(f"Bio: {user_data['bio']}")
        print(f"Followers: {user_data['followers']}")
        print(f"Following: {user_data['following']}")
        print(f"Public Repositories: {user_data['public_repos']}")
    else:
        print(f"Error: Unable to fetch user data (Status Code: {response.status_code})")

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    get_user_info(username)
