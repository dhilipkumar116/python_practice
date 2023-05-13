class Nokia:
    company = "nokia india"
    website = "www.nokia.in"

    def address(self):
        print('Address : no 232 , xxxx, yyyy')

class Nokia1100(Nokia):
    def __init__(self):
        self.name = 'nokia 1100'
        self.year = 1998

    def product_details(self):
        print("Name :",self.name)
        print("year :",self.year)
        print("Company :",self.company)
        print("Website :",self.website)

mobile = Nokia1100()
mobile.product_details()
mobile.address()