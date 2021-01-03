CREATE TABLE vehicle_table(
    id int NOT NULL,
    capacity int NOT NULL,
    type varchar(255),
    PRIMARY KEY (id)
);

INSERT INTO vehicle_table (id, capacity, type) VALUES (1, 30, 'Bike');
INSERT INTO vehicle_table (id, capacity, type) VALUES (2, 50, 'Scooter');
INSERT INTO vehicle_table (id, capacity, type) VALUES (3, 100, 'Truck');