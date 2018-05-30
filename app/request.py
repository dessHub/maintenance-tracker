"""This module defines a request class and methods associated to it"""
#used to validate names
import re
import uuid


class Requests(object):
    """ A class to handle activities related to a request"""
    def __init__(self):
        # A list to hold all user objects
        self.request_list = []

	def create(self, category, description, location, date, time, status, userid):
		"""A method for creating a new event"""
		self.request_details = {}
		if self.existing_request(category, userid, date):
			return "Request Already exists"	
		else:
			#validate event name
			if not self.valid_description(description):
				return "description too short or invalid"
			#validate event date
			elif not self.valid_date(date):
				return "event can only have a future date"
			else:
				self.event_details['description'] = description
				self.event_details['category'] = category
				self.event_details['location'] = location
				self.event_details['date'] = date
				self.event_details['time'] = time
				self.event_details['status'] = status
				self.event_details['date_created'] = date.today().isoformat()
				self.event_details['userid'] = userid
				self.event_details['id'] = uuid.uuid1()
				self.event_list.append(self.event_details)
				return "Reuest Send"


      