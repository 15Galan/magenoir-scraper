import io


class SPELL:
    """
    This class represents a Mage Noir's card, also known as a 'spell'.
    """

    def __init__(self):
        """
        Constructor.
        """
        self.name = ""
        self.element = ""
        self.type = "Spell"
        self.manas = {}
        self.components = {}
        self.effect = ""

    def __str__(self):
        """
        String representation of the class.
        """
        builder = io.StringIO()

        builder.write(f"Name:\t\t{self.name.capitalize()}\n")
        builder.write(f"Element:\t{self.element}\n")
        builder.write(f"Type:\t\t{self.type}\n")

        if self.manas:
            builder.write(f"Manas:\t\t{self.manas}\n")
        else:
            builder.write(f"Manas:\t\t-\n")

        if self.components:
            builder.write(f"Components:\t{self.components}\n")
        else:
            builder.write(f"Components:\t-\n")

        builder.write(f"Effect:\t\t{self.effect}\n")

        data = builder.getvalue()
        builder.close()

        return data