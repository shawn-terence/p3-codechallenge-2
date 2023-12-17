class Customer:
    all_customers = []
    def __init__(self, given_name, family_name):
        # First name of the customer
        self.given_name = given_name
        # Last name of the customer
        self.family_name = family_name
        # List to store reviews written by this customer
        self.reviews = []
        Customer.all_customers.append(self)

    # Method to return the full name of the customer
    def full_name(self):
        return f'{self.family_name} {self.given_name}'
