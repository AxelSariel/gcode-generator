class Gcode:
	def __init__(self, username):
		self.code = '( Generated G-Code )\n'
		self.code = self.code + '( Hello World! )\n'
		self.code = self.code + '(' + username + ')\n'

	def __str__(self):
		return self.code