class Element:
	def __init__(self, name):
		self._name = name

	def name(self):
		return self._name

	def compareTo(self, element):
		raise NotImplementedError('Not yet implemented')


class Rock(Element):
	def compareTo(self, element):
		if element.name() == 'Rock':
			return 'Rock equals Rock', 'Tie'
		elif element.name() == 'Lizard':
			return 'Rock crushes Lizard', 'Win'
		elif element.name() == 'Scissors':
			return 'Rock crushes Scissors', 'Win'
		elif element.name() == 'Paper':
			return 'Paper covers Rock', 'Lose'
		elif element.name() == 'Spock':
			return 'Spock vaporizes Rock', 'Lose'


class Paper(Element):
	def compareTo(self, element):
		if element.name() == 'Paper':
			return 'Paper equals Paper', 'Tie'
		elif element.name() == 'Rock':
			return 'Paper covers Rock', 'Win'
		elif element.name() == 'Spock':
			return 'Paper disproves Spock', 'Win'
		elif element.name() == 'Scissors':
			return 'Scissors cut Paper', 'Lose'
		elif element.name() == 'Lizard':
			return 'Lizard eats Paper', 'Lose'


class Scissors(Element):
	def compareTo(self, element):
		if element.name() == 'Scissors':
			return 'Scissors equals Scissors', 'Tie'
		elif element.name() == 'Paper':
			return 'Scissors cut Paper', 'Win'
		elif element.name() == 'Lizard':
			return 'Scissors decapitate Lizard', 'Win'
		elif element.name() == 'Spock':
			return 'Spock smashes Scissors', 'Lose'
		elif element.name() == 'Rock':
			return 'Rock crushes Scissors', 'Lose'


class Lizard(Element):
	def compareTo(self, element):
		if element.name() == 'Lizard':
			return 'Lizard equals Lizard', 'Tie'
		elif element.name() == 'Spock':
			return 'Lizard poisons Spock', 'Win'
		elif element.name() == 'Paper':
			return 'Lizard eats Paper', 'Win'
		elif element.name() == 'Rock':
			return 'Rock crushes Lizard', 'Lose'
		elif element.name() == 'Scissors':
			return 'Scissors decapitate Lizard', 'Lose'


class Spock(Element):
	def compareTo(self, element):
		if element.name() == 'Spock':
			return 'Spock equals Spock', 'Tie'
		elif element.name() == 'Scissors':
			return 'Spock smashes Scissors', 'Win'
		elif element.name() == 'Rock':
			return 'Spock vaporizes Rock', 'Win'
		elif element.name() == 'Lizard':
			return 'Lizard poisons Spock', 'Lose'
		elif element.name() == 'Paper':
			return 'Paper disproves Spock', 'Lose'

if __name__ == '__main__':
	
