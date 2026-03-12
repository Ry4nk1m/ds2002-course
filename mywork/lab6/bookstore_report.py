import os
from pymongo import MongoClient

def main():
    # Get credentials from environment
    url = os.getenv("MONGODB_ATLAS_URL")
    user = os.getenv("MONGODB_ATLAS_USER")
    pwd = os.getenv("MONGODB_ATLAS_PWD")

    # Connection URI
    uri = f"mongodb+srv://{user}:{pwd}@{url}/?retryWrites=true&w=majority"
    client = MongoClient(uri)

    try:
        db = client.bookstore
        authors = db.authors

        print(f"\nTotal Authors: {authors.count_documents({})}")
        print("-" * 40)
        for a in authors.find():
            print(f"{a['name']} | {a['nationality']}")
        print("-" * 40)

    finally:
        client.close()

if __name__ == "__main__":
    main()
