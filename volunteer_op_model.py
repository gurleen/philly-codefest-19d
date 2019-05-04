import uuid

class Resource:
	def __init__(self, name, dates, location, description, contact, resourceId, uid=str(uuid.uuid4())):
		self.name = name
		self.dates = dates
		self.location = location
		self.description = description
		self.contact = contact
		self.uid = uid

	def get_json(self):
		rv = self.__dict__
		rv["__type__"] = "VolunteerOp"
		return rv
