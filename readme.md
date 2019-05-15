Garbage Monitoring System

Hardware:
Arduino Uno
Ultrasonic Sensors
Servo Motors
Node MCU
Jumper Wires
TrashCan

Softwares:
Arduino IDE
Pycharm
Ubidots(To send data online)

**SuperUser can add the Contractors via Admin interface.

**Privilege to Contractors:
Register and delete Clients.
Register and delete Drivers.
Add and remove Dustbins.
(Statistics part is not included yet.)

Database Fields:  
Contractor:
ID/Username 
Password

Clients:
Client Username 
Password 
Name 
Address 
Contact
Driver ID as Foreign Key
Dustbin ID

Drivers:
Username
Password
Name
Address
Contact
Truck_no
TrashCan:
Trashcan ID
Position Coordinates
Customer ID as Foreign Key
Driver ID as Foreign Key

Login portals for Contractors and Drivers.
Contractors can access and manage all the details of Clients,Drivers and Trashcans.
Contractor will provide the Username and passwords to drivers.
Drivers will get the real-time reading from the trash cans within their login-portal.

Working:
First ultasonic sensor is used to measure the filled Trashcan and send the data to the ubidots server.From their we fetch out the data in our web application (drivers’ portal) for a particular trashcan associated with that driver.
Second ultrasonic sensor is used to detect the  person standing near it and the flap of trashcan will open automatically using the servo motor. 


 
