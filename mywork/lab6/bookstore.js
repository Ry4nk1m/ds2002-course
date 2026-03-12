// Task 2: use database
use bookstore;

// Task 3: insert first author
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
});

// Task 4: update to add birthday
db.authors.updateOne(
  { "name": "Jane Austen" },
  { $set: { "birthday": "1775-12-16" } }
);

// Task 5: insert four more authors
db.authors.insertMany([
  {
    "name": "Ernest Hemingway",
    "nationality": "American",
    "bio": { "short": "20th-century novelist.", "long": "Winner of the Nobel Prize in Literature." },
    "birthday": "1899-07-21"
  },
  {
    "name": "Virginia Woolf",
    "nationality": "British",
    "bio": { "short": "Modernist writer.", "long": "Famous for using stream of consciousness in novels like Mrs Dalloway." },
    "birthday": "1882-01-25"
  },
  {
    "name": "Chinua Achebe",
    "nationality": "Nigerian",
    "bio": { "short": "Father of modern African literature.", "long": "Author of Things Fall Apart." },
    "birthday": "1930-11-16"
  },
  {
    "name": "Isabel Allende",
    "nationality": "Chilean",
    "bio": { "short": "Magic realist.", "long": "Known for The House of the Spirits." },
    "birthday": "1942-08-02"
  }
]);

// Task 6: total count
db.authors.countDocuments({});

// Task 7: British authors, sorted by name
db.authors.find({ "nationality": "British" }).sort({ "name": 1 });
