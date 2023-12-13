# Import the Produit and Commandes classes from the 'classes' module
from classes import Produit, Commandes

# Create two instances of the Produit class
p1 = Produit("2dt3g3f4d", "pc", 46, 100)
p2 = Produit("2dt3gkk7u", "phone", 15, 70)

# Print the string representation of each product
print(p1)
print(p2)

# Check if p1 is equal to p2 based on their reference attribute
print(p1 == p2)

# Create two instances of the Commandes class
c1 = Commandes("2020/07/25", 45, p1)
c2 = Commandes("2019/06/06", 1, p2)

# Print the string representation of each order
print(c1)
print(c2)

# Check if c1 is equal to c2 based on their date and associated product
print(c1 == c2)
