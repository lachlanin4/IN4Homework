class Item:
    """
    A Class that encapsulates the features of an item
    """

    def __init__(self, item_name, description):
        """
        Initialise member variables
        """
        self._item_name = item_name
        self._description = description

    @property
    def item_name(self):
        return self._item_name

    @property
    def description(self):
        return self._description
