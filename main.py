from fastapi import FastAPI, Response
from jinja2 import Template
import requests

GOOGLE_HREF = "https://www.googleapis.com/books/v1/volumes?q=search+terms"

app = FastAPI()

@app.get("/")
async def root():
    template = Template(open("templates/index.html").read())
    content = template.render()
    return Response(content=content, media_type="text/html")


@app.get("/scrape_book/{book_id}")
async def scrape_book(book_id: int):
    params = {
        "q": "9780321127310"
    }
    response = requests.get(GOOGLE_HREF, params=params)

    return response.json()