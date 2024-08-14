#Welcomes the user into the porta;
class Data_Solutions:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome to Data Solutions", self.name,"!!")

# Class Client displays the client loaction and other details, class abstraction is implemented 
# for the function to start contract.        
class Client:
    def __init__(self, client, location):
        self.client = client
        self.location = location
        self.agreed = False                    
        self.signed = False
        self.amount_paid = False

    @staticmethod
    def welcome():
        print("Client details are displayed here, Proceed to start Contract")

    def display_details(self):
        print("Name:", self.client)
        print("Area of Service:", self.location)

    def contract_started(self):                #Abstarction 
        self.agreed = True
        self.signed = True
        self.amount_paid = True
        print("Contract has been started")

#Child class that inherited the properties from its parent class Client    
class ThirdPartyClient(Client):                #Inheritance
    def __init__(self, client, location, sub_client):
        super().__init__(client, location)
        self.sub_client = sub_client
        
    @staticmethod                              #Polymorphism 
    def welcome():
        print("Secondary Client details are displayed here, Proceed to start Contract")

    def display_details(self):                 #Polymorphism 
        super().display_details()
        print("Secondary Client Name:", self.sub_client)


#calls 
user1 = Data_Solutions("Thejaswini")
user1.welcome()

client1 = Client("AZ", "Australia")
client1.welcome()
client1.display_details()
client1.contract_started()


client2 = ThirdPartyClient("AZ", "Australia", "AZW")
client2.welcome()
client2.display_details()
client2.contract_started()
    



