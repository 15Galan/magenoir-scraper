import io


class ProgressBar:
    """
    This class represents a progress bar and it's state.
    """

    def __init__(self, size):
        """
        Constructor.

        :param size: the size of the progress bar (number of elements).
        """
        self.progress = 0
        self.size = size

    def update(self, step, spell=''):
        """
        Updates the progress bar.

        :param step: the number of elements to add to the progress bar.
        :param spell: the name of the spell to display (if any).
        """
        self.progress += step

        if self.progress > self.size:
            self.progress = self.size

        print(self, '\t' + spell, end='' if self.progress < self.size else '\n')

    def __str__(self):
        """
        Returns the progress bar as a string.
        """
        bar = io.StringIO()

        # Compute the percentage of the progress
        percentage = self.progress / self.size

        # Compute the number of filled and empty spaces in the progress bar
        filled = int(percentage * 50)
        spaces = 50 - filled

        # Display the progress bar
        bar.write('\r[')
        bar.write('#' * filled)
        bar.write(' ' * spaces)
        bar.write('] ')
        bar.write(str(int(percentage * 100)))
        bar.write('%')

        return bar.getvalue()
