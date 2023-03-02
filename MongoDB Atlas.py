from pymongo import MongoClient

Client = MongoClient(
    "mongodb+srv://BeCompliant:BeCompliant1234@becompliant.dn86itm.mongodb.net/?retryWrites=true&w=majority")
db = Client.get_database('fakeDB')
users = db.Users
print(users.count_documents({}))


# new_user = {
#    'name': 'Paz',
#    'id': '987654321',
#    'address': 'Dizinguf 7',
#    'email address': 'paz@gmail.com'
# }

# users.insert_one(new_user)


def create_user(name, id, address, emailAddress):
    new_user = {
        'name': name,
        'id': id,
        'address': address,
        'email address': emailAddress
    }
    users.insert_one(new_user)


print(list(users.find()))
