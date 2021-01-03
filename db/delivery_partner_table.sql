CREATE TABLE delivery_partner_table(
    id int NOT NULL,
    vehicle_type_id int NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO delivery_partner_table (id, vehicle_type_id) VALUES (1, 1);
INSERT INTO delivery_partner_table (id, vehicle_type_id) VALUES (2, 1);
INSERT INTO delivery_partner_table (id, vehicle_type_id) VALUES (3, 1);
INSERT INTO delivery_partner_table (id, vehicle_type_id) VALUES (4, 2);
INSERT INTO delivery_partner_table (id, vehicle_type_id) VALUES (5, 2);
INSERT INTO delivery_partner_table (id, vehicle_type_id) VALUES (6, 3);

