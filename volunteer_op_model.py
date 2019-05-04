import uuid

class Volunteer_Op:
	def __init__(self, name, dates, location, description, contact, resource_id, uid=str(uuid.uuid4())):
		self.name = name
		self.dates = dates
		self.location = location
		self.description = description
		self.contact = contact
		self.resource_id = resource_id
		self._id = uid

	def get_json(self):
		rv = self.__dict__
		rv["__type__"] = "VolunteerOp"
		return rv
