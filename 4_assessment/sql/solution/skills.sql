-- Note: Please consult the directions for this assignment
-- for the most explanatory version of each question.

-- Part 1

-- 1. Select all columns for all brands in the brands table.
SELECT *
    FROM brands;

-- 2. Select all columns for all car models made by Pontiac in the models table.
SELECT *
    FROM models
    WHERE brand_name='Pontiac';

-- 3. Select the brand name and model
--    name for all models made in 1964 from the models table.
SELECT brand_name, name
    FROM models
    WHERE year = 1964;


-- 4. Select the model name, brand name, and headquarters for the Ford Mustang
--    from the models and brands tables.
SELECT m.name, m.brand_name, b.headquarters
    FROM models AS m
    JOIN brands AS b
    ON m.brand_name = b.name
    WHERE b.name = 'Ford'
    AND m.name = 'Mustang';

-- 5. Select all rows for the three oldest brands
--    from the brands table (Hint: you can use LIMIT and ORDER BY).
SELECT * FROM brands
    ORDER BY founded
    LIMIT 3;

-- 6. Count the Ford models in the database (output should be a number).
SELECT COUNT(*)
    FROM models
    WHERE brand_name = 'Ford';

-- 7. Select the name of any and all car brands that are not discontinued.
SELECT name
    FROM brands
    WHERE discontinued IS NULL;

.. FIXME
    I believe this solution is incorrect. Should be LIMIT 11, yes?

-- 8. Select everything from rows 15-25 of the models table in
--    alphabetical order by name.
--    (Hint: how can you show only part of a result set?)
SELECT *
    FROM models
    ORDER BY name
    LIMIT 10
    OFFSET 14;

-- 9. Select the brand, name, and year the model's brand was
--    founded for all of the models from 1960. Include row(s)
--    for model(s) even if its brand is not in the brands table.
--    (The year the brand was founded should be ``null`` if
--    the brand is not in the brands table.)
SELECT m.name, m.brand_name, b.founded
    FROM models AS m
    LEFT JOIN brands AS b
    ON b.name = m.brand_name
    WHERE year = 1960;



-- Part 2

-- 1. Modify this query so it shows all brands that are not discontinued
-- regardless of whether they have any models in the models table.
-- before:
-- SELECT b.name, b.founded, m.name
    -- FROM models AS m
    --     LEFT JOIN brands AS b
    --     ON b.name = m.brand_name
    --     WHERE b.discontinued IS NULL;

-- answer
SELECT m.name, m.brand_name, b.founded
    FROM brands AS b
    LEFT JOIN models AS m
    ON b.name = m.brand_name
    WHERE b.discontinued IS NULL;


-- 2. Modify this left join so it only selects models that have brands in the brands table.
-- before:
-- SELECT m.name, m.brand_name, b.founded
--     FROM models AS m
--     LEFT JOIN brands AS b
--     ON b.name = m.brand_name;

SELECT m.name, m.brand_name, b.founded
    FROM models AS m
    JOIN brands AS b
    ON b.name = m.brand_name;

-- followup question: In your own words, describe the difference between
-- left joins and inner joins. Feel free to use this problem in your explanation.

-- 3. Modify the query so that it only selects brands that don't have
--    any models in the models table. (Hint: it should only show Tesla.)
-- before:
-- SELECT name, founded
--     FROM brands
--     LEFT JOIN models
--     ON brands.name = models.brand_name
--     WHERE models.year > 1940;

SELECT brands.name, founded
    FROM brands
    LEFT JOIN models
    ON brands.name = models.brand_name
    WHERE models.brand_name IS NULL;


-- 4. Modify the query to add another column to the results to show
-- the number of years from the year of the model *until* the brand becomes discontinued
-- Display this column with the name years_until_brand_discontinued.
-- SELECT b.name, m.name, m.year, b.discontinued
    -- FROM models AS m
    -- LEFT JOIN brands AS b
    -- ON m.brand_name = b.name
    -- WHERE b.discontinued not null;

.. FIXME
    problem says to add a column, solution removes a column and adds one??

SELECT b.name as brand_name,
       m.name as model_name,
       m.year,
       (b.discontinued - m.year)
            AS years_until_brand_discontinued
    FROM models AS m
    LEFT JOIN brands AS b
    ON m.brand_name = b.name;



-- Part 3: Further Study

-- 1. Select the brands with more than 5 models.
SELECT name
FROM models
GROUP BY name
HAVING COUNT(name) > 5;

-- 2. Insert two rows into the models table.
INSERT INTO models (year, brand_name, name)
VALUES
    (2015, 'Chevrolet', 'Malibu'),
    (2015, 'Subaru', 'Outback');

-- 3. Create a table called Awards with columns
--    name, year, and winner.

.. FIXME
    Solution has id SERIAL, no mention of it in the instructions

CREATE TABLE awards (
    id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    winner_id INTEGER NULL,
    name VARCHAR(50) NOT NULL
);

-- 4. Write a SQL statement that adds the following rows to the Awards table:
--    (no need to do subqueries here).
INSERT INTO awards (name, year, winner_id)
    VALUES
        ('IIHS Safety Award', 2015, 49),
        ('IIHS Safety Award', 2015, 50);

-- 5. Using a subquery, select only the *name* of any model whose
-- year is the same year that *any* brand was founded.

SELECT name, year
    FROM models
    WHERE year IN
        (SELECT founded
            FROM brands);


