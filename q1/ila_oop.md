# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be used by creating a class that contains the product's name, price, and stock quantity.
The product's data will have methods to control how the values are updated. 
This can keep the product's properties and behaviors stored and organized in one class.

### 2. Abstraction
Abstraction can be applied by providing methods that mask the complicated details of how the inventory works. 
For example, the store doesn't need to know all the steps used to check the stock and update the quantity, you just have to use a method named sell_product().
This can make the program easier to use and understand since only the important features are exposed.

### 3. Inheritance
Inheritance can be used when different types of products share common properties. 
A Product class could be created, and you create classes under that umbrella like FoodProduct and HouseholdProduct that inherit properties such as name, price, and quantity. 
This reduces repetition in coding and makes it easier to add new types of products to the inventory.

### 4. Polymorphism
Polymorphism allows different product classes to use the same name while performing the method differently. 
For example, both FoodProduct and HouseholdProduct could have display_info(), but each class could display different information.
This makes the program more flexible because the inventory system can work with different products within a common interface.

## Reflection
Among the four pillars of Object-Oriented Programming, Encapsulation would be the most useful for improving the sari-sari store inventory system. 
It keeps important product information stored inside each Product. 
Aside from that, it also helps prevent incorrect changes to the inventory by controlling updates through methods. 
In conclusion, encapsulation would make the inventory system easier to manage and maintain.
