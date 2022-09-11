from methods import Utils
from json import dumps

github_matheus = Utils("eumts")
github_bender = Utils("benderf")

print(dumps(github_matheus.user_info(), indent=4))
print(dumps(github_bender.user_info(), indent=4))