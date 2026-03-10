SELECT 
    b.title, 
    a.name AS author_name, 
    b.genre, 
    b.published_year
FROM books b
JOIN authors a ON b.author_id = a.author_id
WHERE b.genre = 'Fiction'
ORDER BY b.published_year DESC;
