from cryptography.fernet import Fernet
import boto3


def createDB():
    try:
        db=boto3.resource('dynamodb')
    except:
        print("Error!\n Did not succeeded to create a db\n")
        return
    return db

def createTable(db,nameTable):
    try:
        table=db.Table(nameTable)
    except:
        print("Error!\n Did not succeeded to create a table\n")
        return
    return table

def addItem(nameTable,item):
    try:
        nameTable.put_item(Item=item)
    except:
        print("Error!\n Did not succeeded to add an item\n")