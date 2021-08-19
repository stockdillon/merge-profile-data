from ..business_entity import BusinessEntity

class Organization(BusinessEntity):
    def __init__(self, name="Organization"):
        super().__init__(name)
        self.packages = []
        self.people = []
