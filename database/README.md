# Commands to create our DB


CREATE TABLE customer_data
(
customer_id INT,
first_name VARCHAR(45),
last_name VARCHAR(45),
e_mail VARCHAR(45),
pass VARCHAR(45),
PRIMARY KEY(customer_id)
);

CREATE TABLE customer_address
(
street_name VARCHAR(45),
street_number INT,
city VARCHAR(45),
state VARCHAR(45),
zip INT,
FOREIGN KEY (customer_id) REFERENCES customer_data(customer_id) 
);

CREATE TABLE customer_payment
(
customer_id INT,
cardholder_name VARCHAR(45),
cardholder_company VARCHAR(45),
card_number VARCHAR(45),
card_CSV INT,
expiration_month INT,
expiration_year INT,
FOREIGN KEY (customer_id) REFERENCES customer_data(customer_id) 
);

CREATE TABLE restaurant_data
(
restaurant_id INT,
restaurant_name VARCHAR(45),
e_mail VARCHAR(45),
pass VARCHAR(45),
street_name VARCHAR(45),
street_number INT,
city VARCHAR(45),
state VARCHAR(45),
zip INT,
cuisine VARCHAR(45),
min_order INT,
discount_interval INT,
restaurant_url VARHAR(45),
PRIMARY KEY (restaurant_id)
);

CREATE TABLE appetizers_menu
(
restaurant_id INT,
item_name VARCHAR(45),
item price FLOAT,
item_description VARCHAR(140),
FOREIGN KEY (restaurant_id) REFERENCES restaurant_data(restaurant_id) 
);

CREATE TABLE mains_menu
(
restaurant_id INT,
item_name VARCHAR(45),
item price FLOAT,
item_description VARCHAR(140),
FOREIGN KEY (restaurant_id) REFERENCES restaurant_data(restaurant_id) 
);

CREATE TABLE desserts_menu
(
restaurant_id INT,
item_name VARCHAR(45),
item price FLOAT,
item_description VARCHAR(140),
FOREIGN KEY (restaurant_id) REFERENCES restaurant_data(restaurant_id) 
);

CREATE TABLE other_menu
(
restaurant_id INT,
item_name VARCHAR(45),
item price FLOAT,
item_description VARCHAR(140),
FOREIGN KEY (restaurant_id) REFERENCES restaurant_data(restaurant_id) 
);

CREATE TABLE orders
(
order_id INT,
restaurant_id INT,
customer_id INT,
item_name VARCHAR(45),
item_quantity INT,
item_price FLOAT,
FOREIGN KEY (restaurant_id) REFERENCES restaurant_data(restaurant_id) 
FOREIGN KEY (customer_id) REFERENCES customer_data(customer_id) 
);
