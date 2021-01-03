CREATE TABLE vehicle_slot_table(
    id int NOT NULL,
    vehicle_type_id int NOT NULL,
    slot_id int NOT NULL,
    status int NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (1, 1, 1, 1);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (2, 1, 2, 1);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (3, 1, 3, 1);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (4, 1, 4, 0);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (5, 2, 1, 1);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (6, 2, 2, 1);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (7, 2, 3, 1);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (8, 2, 4, 0);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (9, 3, 1, 0);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (10, 3, 2, 1);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (11, 3, 3, 1);
INSERT INTO vehicle_slot_table (id, vehicle_type_id, slot_id, status) VALUES (12, 3, 4, 1);