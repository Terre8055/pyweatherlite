"""BaseClass module establishes methods to seek longitude and latitude coordinates"""


class BaseClass:
	"""This class defines the base model for getting cooords"""

	def __init__(
		self,
		longitude:float=0.0,
		latitude:float=0.0,
		):

		self._longitude = longitude
		self._latitude = latitude

	@property
	def get_longitude(self):
		"""Method to return longitude coords
			can definitely set longitude to 
			custom without using pre-defined
			to generate			
			"""
		return self._longitude
	

	@property
	def get_latitude(self):
		"""Method to return lat coords
			can definitely set latitude to 
			custom without using pre-defined
			to generate			
			"""	
		return self._latitude
	








