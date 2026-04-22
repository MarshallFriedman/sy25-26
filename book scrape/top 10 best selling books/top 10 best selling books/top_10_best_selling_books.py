import requests
from bs4 import BeautifulSoup

def get_star_rating(star_str):
    # Converts star rating string to integer
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(star_str, 0)

def scrape_top_10_books():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    
    # Debugging: Check if the response is successful
    if response.status_code != 200:
        print(f"Failed to fetch the website. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    for book in soup.select("article.product_pod")[:10]:
        try:
            title = book.h3.a["title"]
            price = book.select_one("p.price_color").text.strip()
            star_class = book.select_one("p.star-rating")["class"]
            # The second class is the rating (e.g., "Three")
            star_rating = get_star_rating(star_class[1]) if len(star_class) > 1 else 0

            books.append({
                "title": title,
                "price": price,
                "star_rating": star_rating
            })
        except Exception as e:
            print(f"Error parsing book data: {e}")
            continue

    # Debugging: Check if books were scraped
    if not books:
        print("No books were scraped. Check the website structure or selectors.")
        return

    # Print the top 10 books to the console
    print("Top 10 Best Selling Books:")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book['title']}")
        print(f"   Price: {book['price']}")
        print(f"   Star Rating: {book['star_rating']} stars")
        print()

if __name__ == "__main__":
    scrape_top_10_books()