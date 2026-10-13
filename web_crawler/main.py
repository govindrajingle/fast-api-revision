import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

# url = "http://example.com"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title.text)

app = FastAPI()


@app.get("/news")
def get_news():
    url = "https://indianexpress.com"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        titles = []

        for item in soup.find_all("a", class_="topblockNews__sidebarLink"):
            title = item.get_text(strip=True)

            if title:
                titles.append(title)

        return {"news": titles[:5]}

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch news: {str(e)}")
