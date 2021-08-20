from ..business_entity import BusinessEntity

class Team(BusinessEntity):
    def __init__(self, name="Team"):
        super().__init__(name)
