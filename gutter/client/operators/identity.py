from gutter.client.operators import Base


class Truthy(Base):

    label = 'true'
    group = 'identity'
    preposition = 'true'

    def applies_to(self, argument):
        return bool(argument)

    def __str__(self):
        return 'true'
