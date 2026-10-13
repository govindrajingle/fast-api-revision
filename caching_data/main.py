import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import time

# url = "http://example.com"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title.text)

app = FastAPI()

cache_data = []
last_fetch = 0


@app.get("/news")
def get_news():
    global cache_data, last_fetch
    start = time.time()
    if time.time() - last_fetch > 60:
        print("fetching fresh data")
        url = "https://news.ycombinator.com"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            titles = []
            for item in soup.find_all("span", class_="titleline"):
                titles.append(item.text)
            cache_data = [
                item.text for item in soup.find_all("span", class_="titleline")
            ]
            last_fetch = time.time()
            return {"news": titles[:5]}
        except requests.RequestException as e:
            raise HTTPException(
                status_code=502, detail=f"Failed to fetch news: {str(e)}"
            )
    else:
        print("using cached data")
        end = time.time()
        time_taken = round(end - start, 4)
        print("time taken: ", time_taken)
        return {"time_taken": time_taken, "news": cache_data}
