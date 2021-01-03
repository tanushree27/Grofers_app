CREATE TABLE order_table(
    id int NOT NULL,
    weight float NOT NULL,
    slot_id int,
    delivery_partner_id int,
    PRIMARY KEY (id)
);