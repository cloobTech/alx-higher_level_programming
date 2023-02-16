-- creates the table unique_id on your MySQL server with a unique ID

CREATE TABLE
    IF NOT EXISTS unique_id
    (id INT DEFAULT 1, name VARCHAR(256), UNIQUE (id));

