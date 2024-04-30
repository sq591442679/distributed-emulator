class LinkDirection:
	def __init__(self, direction: str) -> None:
		if direction in ['n', 's', 'e', 'w']:
			self.direction = direction
		else:
			raise Exception('invalid direction str')
		
	def get_reverse_direction(self) -> str:
		if self.direction == 'n':
			return 's'
		elif self.direction == 's':
			return 'n'
		elif self.direction == 'e':
			return 'w'
		elif self.direction == 'w':
			return 'e'
		else:
			raise Exception('invalid direction str')
		
	def __str__(self) -> str:
		return self.direction