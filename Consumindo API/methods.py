from requests import get
from json import dumps

class Utils():
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_id = None
        self.user_full_name = None
        self.user_followers = None
        self.repos_count = None
        self.repo_names = None
        self.__get_user_info()
        self.__get_repo_names()

    def __get_user_info(self):
        url = f"https://api.github.com/users/{self.user_name}"
        response = get(url)
        if response.status_code == 200:
            user_info = response.json()
            self.user_id = user_info["id"]
            self.user_full_name = user_info["name"]
            self.user_followers = user_info["followers"]
            self.repos_count = user_info["public_repos"]

    def __get_repo_names(self):
        url = f"https://api.github.com/users/{self.user_name}/repos"
        response = get(url)
        if response.status_code == 200:
            repo_names = []
            user_repos = response.json()
            for repo in user_repos:
                repo_names.append(repo["name"])
            self.repo_names = repo_names

    def user_info(self):
        user_info = {
            "user_name": self.user_name,
            "user_id": self.user_id,
            "user_full_name": self.user_full_name,
            "user_followers": self.user_followers,
            "repos_count": self.repos_count,
            "repo_names": self.repo_names
        }

        return user_info

if __name__ == "__main__":
    my_class = Utils("eumts")
    print(dumps(my_class.user_info(), indent=4))
