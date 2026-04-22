import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def get_star_rating(star_str):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(star_str, 0)

def get_book_details(book_url):
    print(f"Fetching details for book: {book_url}")
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, "html.parser")
    breadcrumb = soup.select("ul.breadcrumb li a")
    author = breadcrumb[-1].text.strip() if breadcrumb else "Unknown"
    pub_date = "Unknown"
    table = soup.find("table", {"class": "table table-striped"})
    if table:
        for row in table.find_all("tr"):
            heading = row.th.text.strip()
            if heading.lower() == "publication date":
                pub_date = row.td.text.strip()
                break
    return author, pub_date

def scrape_top_10_books():
    url = "https://books.toscrape.com/"
    print("Starting to scrape the website...")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the website. Status code: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    print("Searching for books...")
    for book in soup.select("article.product_pod"):
        try:
            title = book.h3.a["title"]
            price = book.select_one("p.price_color").text.strip()
            star_class = book.select_one("p.star-rating")["class"]
            star_rating = get_star_rating(star_class[1]) if len(star_class) > 1 else 0
            rel_url = book.h3.a["href"]
            book_url = url + rel_url if "catalogue" not in rel_url else url + rel_url
            if not book_url.startswith("http"):
                book_url = url + rel_url.lstrip("./")
            if "catalogue/" not in book_url:
                book_url = url + "catalogue/" + rel_url.lstrip("./")
            author, pub_date = get_book_details(book_url)
            books.append({
                "title": title,
                "price": price,
                "star_rating": star_rating,
                "author": author,
                "pub_date": pub_date,
                "book_url": book_url
            })
            print(f"Book '{title}' added.")
        except Exception as e:
            print(f"Error parsing book data: {e}")
            continue

    if not books:
        print("No books were scraped. Check the website structure or selectors.")
        return

    print(f"Scraped {len(books)} books.")

    # Generate a unique file name with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"Top_10_Books_{timestamp}.txt"

    # Get the Downloads folder path
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = os.path.join(downloads_folder, file_name)

    try:
        print(f"Creating new structured file in Downloads: {file_path}...")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Top 10 Best Selling Books:\n")
            books_sorted = sorted(books, key=lambda x: -x["star_rating"])
            for idx, book in enumerate(books_sorted[:10], 1):
                file.write(f"{idx}. {book['title']}\n")
                file.write(f"   Price: {book['price']}\n")
                file.write(f"   Star Rating: {book['star_rating']} stars\n")
                file.write(f"   Author: {book['author']}\n")
                file.write(f"   Publication Date: {book['pub_date']}\n")
                file.write(f"   URL: {book['book_url']}\n\n")
                print(f"Added book {idx}: {book['title']}")

            least_popular = min(books, key=lambda x: x["star_rating"])
            file.write("Least Popular Book on the First Page:\n")
            file.write(f"Title: {least_popular['title']}\n")
            file.write(f"Price: {least_popular['price']}\n")
            file.write(f"Star Rating: {least_popular['star_rating']} stars\n")
            file.write(f"Author: {least_popular['author']}\n")
            file.write(f"Publication Date: {least_popular['pub_date']}\n")
            file.write(f"URL: {least_popular['book_url']}\n")
        print(f"All information has been saved to '{file_path}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

    # Print large message at the end
    print("\n" + "=" * 80)
    print("CHECK YOUR DOWNLOADS FOLDER TO SEE YOUR TEXT DOCUMENT".center(80))
    print("=" * 80)

if __name__ == "__main__":
    scrape_top_10_books()