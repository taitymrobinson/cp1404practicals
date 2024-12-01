class ProgrammingLanguage:
    """Represents a programming language object."""
    def __init__(self, name, typing, reflection, year):
        """Initialises a programming language object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Displays the data for a programming language object."""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if typing style is dynamic."""
        return self.typing == 'Dynamic'

