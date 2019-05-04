import uuid

class Resource:
	def __init__(self, name, categories, location, description, contact, uid=str(uuid.uuid4())):
		self.name = name
		self.categories = categories
		self.location = location
		self.description = description
		self.contact = contact
		self.uid = uid

	def get_json(self):
		rv = self.__dict__
		rv["__type__"] = "Resource"
		return rv
