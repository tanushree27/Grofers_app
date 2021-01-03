CREATE TABLE slot_table(
    id int NOT NULL,
    type varchar(255) NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO slot_table (id, type) VALUES (1, '6-9');
INSERT INTO slot_table (id, type) VALUES (2, '9-13');
INSERT INTO slot_table (id, type) VALUES (3, '16-19');
INSERT INTO slot_table (id, type) VALUES (4, '19-23');