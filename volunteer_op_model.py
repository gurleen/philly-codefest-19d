import uuid

class Volunteer_Op:
	def __init__(self, name, location, description, contact, uid=str(uuid.uuid4())):
		self.name = name
		self.location = location
		self.description = description
		self.contact = contact
		self._id = uid

	def get_json(self):
		rv = self.__dict__
		rv["__type__"] = "VolunteerOp"
		return rv
