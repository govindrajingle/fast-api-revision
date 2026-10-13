import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

# url = "http://example.com"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title.text)

app = FastAPI()


@app.get("/news")
def get_news(page: int = 1, limit: int = 5):
    url = "https://news.ycombinator.com"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        titles = []

        for item in soup.find_all("span", class_="titleline"):
            titles.append(item.text)

        start = (page - 1) * limit
        end = start + limit

        return {
            "page": page,
            "limit": limit,
            "total": len(titles),
            "news": titles[start:end],
        }

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch news: {str(e)}")
