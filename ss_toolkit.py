import json, csv

class ConfigParser:
    def __init__(self):
        with open("config.json") as f:
            data = json.load(f)
            self.__username = data["email"]
            self.__password = data["password"]
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
class PeopleParser:
    def __init__(self):
        self.__list = []
        with open("files/participants.csv", newline='') as f:
            participant_file = csv.reader(f)
            next(participant_file, None)
            for row in participant_file:
                self.__list.append(row)
    def get_list(self):
        return self.__list
class SelectionDatabase:
    def __init__(self, path):
        self.__file = open(path, "a")
        self.__file.write("original,recipient")
    def add(self, giver, gifted):
        self.__file.write(f'\n{giver},{gifted}')