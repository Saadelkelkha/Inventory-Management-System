import copy

# Define a class named "Produit"
class Produit:
    __nbrp = 0  # Class variable to keep track of the number of instances

    # Constructor method
    def __init__(self, reference, name, prixa, prixv):
        self.__reference = reference
        self.__name = name
        self.__prixa = prixa
        self.__prixv = prixv
        self.__nbrex = 0
        Produit.__nbrp += 1

    # Getter method for the number of products in stock
    @property
    def Getnbra(self):
        return self.__nbrex

    # Class method to get the total number of instances of the class
    @classmethod
    def Getnbrp(cls):
        return Produit.__nbrp

    # Setter method to update the quantity in stock
    def Setnbrex(self, nbrex1):
        if self.__nbrex + nbrex1 > 0:
            self.__nbrex += nbrex1
        else:
            print("There are not enough products in stock")

    # Setter method to update the purchase price
    def Setprixa(self, prixa1):
        self.__prixa = prixa1

    # Setter method to update the selling price
    def Setprixv(self, prixv1):
        self.__prixv = prixv1

    # String representation of the object
    def __str__(self):
        return  "; Name: " + self.__name + "; Reference: " + self.__reference + "; Purchase Price: " + str(self.__prixa) + " $" + "; Selling Price: " + str(self.__prixv) + " $" + "; Stock: " + str(self.__nbrex)
        

    # Equality comparison method
    def __eq__(self, p1):
        return self.__reference == p1.__reference


# Define a class named "Commandes"
class Commandes:
    # Constructor method
    def __init__(self, date, qa, produit):
        self.__date = date
        self.__qa = qa
        self.__produit = copy.copy(produit)

    # Getter method for the date
    @property
    def Getdate(self):
        return self.__date

    # Getter method for the product associated with the command
    @property
    def Getpro(self):
        return self.__produit

    # Setter method to update the product associated with the command
    def Setpro(self, pro1):
        self.__produit = pro1

    # Setter method to update the date
    def Setdate(self, date):
        self.__date = date

    # String representation of the object
    def __str__(self):
        return "Date :" + self.__date + "; Quantity :" + str(self.__qa) + str(self.__produit)

    # Equality comparison method
    def __eq__(self, c1):
        return self.__date == c1.__date and self.__produit == c1.__produit
