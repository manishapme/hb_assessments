-- Include your solutions to the More Practice problems in this file.



-- INSERT
cars=# INSERT INTO models (year, brand_name, name)
cars-# VALUES(2015, 'Chevrolet', 'Malibu');
INSERT 0 1
cars=# INSERT INTO models (year, brand_name, name)
cars-# VALUES(2015, 'Subaru', 'Outback');
INSERT 0 1


-- CREATE TABLE
CREATE TABLE awards (
 name VARCHAR(50) NOT NULL,
 year INTEGER,
 winner_id INTEGER REFERENCES models);

-- More INSERT

cars-# VALUES('IIHS Safety Award', 2015, 49);
INSERT 0 1
cars=# INSERT INTO awards (name, year, winner_id)
VALUES('IIHS Safety Award', 2015, 50);
ERROR:  insert or update on table "awards" violates foreign key constraint "awards_winner_id_fkey"
DETAIL:  Key (winner_id)=(50) is not present in table "models".
cars=# 
