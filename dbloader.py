from pymongo import MongoClient
import json

from resource_model import Resource
from volunteer_op_model import Volunteer_Op

client = MongoClient()  # assumes local
db = client['auxilium']


def complex_handler(obj):           # used to get the dict representation of custom objects
    if hasattr(obj, 'get_json'):
        return obj.get_json()


def decoder(obj):              # used to reconstitute custom objects from stored dictionaries
    if '__type__' in obj:
        if obj["__type__"] == 'VolunteerOp':
            return Volunteer_Op(obj["name"], obj["location"], obj["description"], obj["contact"], obj["_id"])
        elif obj["__type__"] == 'Resource':
            return Resource(obj["name"], obj["categories"], obj["location"], obj["description"], obj["contact"],
                            obj["_id"])
    else:
        return obj


def store_resource(resource):
    collection = db['resource']
    serialized = json.dumps(resource, default=complex_handler)
    dicted = json.loads(serialized)
    collection.insert(dicted)


def get_resources_matching(search_term):
    collection = db['resource']
    result = collection.find(search_term)
    rv = []
    for record in result:
        serialized = json.dumps(record)
        deserialized = json.loads(serialized, object_hook=decoder)
        rv.append(deserialized)
    return rv


def delete_resource(resource):
    collection = db['resource']
    collection.delete_one({"_id": resource._id})    # delete by _id


def replace_resource(resource):
    delete_resource(resource)                           # replace, preserving the correct _id
    store_resource(resource)


def store_Volunteer_Op(Volunteer_Op):
    collection = db['Volunteer_Op']
    serialized = json.dumps(Volunteer_Op, default=complex_handler)
    dicted = json.loads(serialized)
    collection.insert(dicted)


def get_Volunteer_Ops_matching(search_term):
    collection = db['Volunteer_Op']
    result = collection.find(search_term)
    rv = []
    for record in result:
        serialized = json.dumps(record)
        deserialized = json.loads(serialized, object_hook=decoder)
        rv.append(deserialized)
    return rv


def delete_Volunteer_Op(Volunteer_Op):
    collection = db['Volunteer_Op']
    collection.delete_one({"_id": Volunteer_Op._id})


def replace_Volunteer_Op(Volunteer_Op):
    delete_Volunteer_Op(Volunteer_Op)
    store_Volunteer_Op(Volunteer_Op)
