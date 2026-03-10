-- Step A: Create the tables
CREATE TABLE IF NOT EXISTS authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    birth_year INT
);

CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    genre VARCHAR(50),
    published_year INT,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Step B: Insert 10 Authors
INSERT INTO authors VALUES (1, 'J.K. Rowling', 'UK', 1965);
INSERT INTO authors VALUES (2, 'George R.R. Martin', 'USA', 1948);
INSERT INTO authors VALUES (3, 'Toni Morrison', 'USA', 1931);
INSERT INTO authors VALUES (4, 'Gabriel García Márquez', 'Colombia', 1927);
INSERT INTO authors VALUES (5, 'Haruki Murakami', 'Japan', 1949);
INSERT INTO authors VALUES (6, 'Agatha Christie', 'UK', 1890);
INSERT INTO authors VALUES (7, 'Chinua Achebe', 'Nigeria', 1930);
INSERT INTO authors VALUES (8, 'Margaret Atwood', 'Canada', 1939);
INSERT INTO authors VALUES (9, 'Jorge Luis Borges', 'Argentina', 1899);
INSERT INTO authors VALUES (10, 'Virginia Woolf', 'UK', 1882);

-- Step C: Insert 10 Books linked to those Authors
INSERT INTO books VALUES (101, 'Harry Potter', 'Fantasy', 1997, 1);
INSERT INTO books VALUES (102, 'A Game of Thrones', 'Fantasy', 1996, 2);
INSERT INTO books VALUES (103, 'Beloved', 'Fiction', 1987, 3);
INSERT INTO books VALUES (104, 'One Hundred Years of Solitude', 'Magical Realism', 1967, 4);
INSERT INTO books VALUES (105, 'Norwegian Wood', 'Fiction', 1987, 5);
INSERT INTO books VALUES (106, 'Murder on the Orient Express', 'Mystery', 1934, 6);
INSERT INTO books VALUES (107, 'Things Fall Apart', 'Fiction', 1958, 7);
INSERT INTO books VALUES (108, 'The Handmaids Tale', 'Dystopian', 1985, 8);
INSERT INTO books VALUES (109, 'The Aleph', 'Short Stories', 1945, 9);
INSERT INTO books VALUES (110, 'To the Lighthouse', 'Modernism', 1927, 10);
