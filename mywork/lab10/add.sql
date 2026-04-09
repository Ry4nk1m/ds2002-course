INSERT INTO authors (author_id, name, country, birth_year) 
VALUES (101, 'Han Kang', 'South Korea', 1970);

INSERT INTO authors (author_id, name, country, birth_year) 
VALUES (102, 'Ted Chiang', 'USA', 1967);

INSERT INTO books (book_id, title, genre, published_year, author_id) 
VALUES (201, 'The Vegetarian', 'Fiction', 2007, 101);

INSERT INTO books (book_id, title, genre, published_year, author_id) 
VALUES (202, 'Exhalation', 'Sci-Fi', 2019, 102);

INSERT INTO books (book_id, title, genre, published_year, author_id) 
VALUES (203, 'Story of Your Life', 'Sci-Fi', 1998, 102);
