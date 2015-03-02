class Element:
	def __init__(self, name):
		self._name = name

	def name(self):
		return self._name

	def compareTo(self, Element):
		raise NotImplementedError('Not yet implemented')


class Rock(Element):
	def compareTo(self, Element):
		if Element.name() == 'Rock':
			return 'Rock equals Rock', 'Tie'
		elif Element.name() == 'Lizard':
			return 'Rock crushes Lizard', 'Win'
		elif Element.name() == 'Scissors':
			return 'Rock crushes Scissors', 'Win'
		elif Element.name() == 'Paper':
			return 'Paper covers Rock', 'Lose'
		elif Element.name() == 'Spock':
			return 'Spock vaporizes Rock', 'Lose'


class Paper(Element):
	def compareTo(self, Element):
		if Element.name() == 'Paper':
			return 'Paper equals Paper', 'Tie'
		elif Element.name() == 'Rock':
			return 'Paper covers Rock', 'Win'
		elif Element.name() == 'Spock':
			return 'Paper disproves Spock', 'Win'
		elif Element.name() == 'Scissors':
			return 'Scissors cut Paper', 'Lose'
		elif Element.name() == 'Lizard':
			return 'Lizard eats Paper', 'Lose'


class Scissors(Element):
	def compareTo(self, Element):
		if Element.name() == 'Scissors':
			return 'Scissors equals Scissors', 'Tie'
		elif Element.name() == 'Paper':
			return 'Scissors cut Paper', 'Win'
		elif Element.name() == 'Lizard':
			return 'Scissors decapitate Lizard', 'Win'
		elif Element.name() == 'Spock':
			return 'Spock smashes Scissors', 'Lose'
		elif Element.name() == 'Rock':
			return 'Rock crushes Scissors', 'Lose'


class Lizard(Element):
	def compareTo(self, Element):
		if Element.name() == 'Lizard':
			return 'Lizard equals Lizard', 'Tie'
		elif Element.name() == 'Spock':
			return 'Lizard poisons Spock', 'Win'
		elif Element.name() == 'Paper':
			return 'Lizard eats Paper', 'Win'
		elif Element.name() == 'Rock':
			return 'Rock crushes Lizard', 'Lose'
		elif Element.name() == 'Scissors':
			return 'Scissors decapitate Lizard', 'Lose'


class Spock(Element):
	def compareTo(self, Element):
		if Element.name() == 'Spock':
			return 'Spock equals Spock', 'Tie'
		elif Element.name() == 'Scissors':
			return 'Spock smashes Scissors', 'Win'
		elif Element.name() == 'Rock':
			return 'Spock vaporizes Rock', 'Win'
		elif Element.name() == 'Lizard':
			return 'Lizard poisons Spock', 'Lose'
		elif Element.name() == 'Paper':
			return 'Paper disproves Spock', 'Lose'
