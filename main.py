from fastapi import FastAPI, File, Form, UploadFile, Response, HTTPException
from jinja2 import Template
import requests
import random

GOOGLE_HREF = "https://www.googleapis.com/books/v1/volumes?q=search+terms"

app = FastAPI()

@app.get("/")
async def root():
    template = Template(open("templates/index.html").read())
    content = template.render()

    return Response(content=content, media_type="text/html")

@app.post("/submit-form/")
async def submit_form(
    name: str = Form(...),
    age: int = Form(...),
    email: str = Form(...)
):
    return {"name": name, "age": age, "email": email}

@app.get("/search/")
async def search(
    q: str = Form(...),
    page: int = Form(...)
):
    return {"query": q, "page": page}


@app.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }

@app.get("/scrape_book/{book_id}")
async def scrape_book(book_id):
    params = {
        "q": "9780321127310"
        "key", 
    }
    
    response = requests.get(GOOGLE_HREF, params=params)

    return response.json()

@app.get("/book")
def get_random_book():
    try:
        # Make a request to the Google Books API to get a random book
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=random")
        
        # Raise an exception if the request failed
        response.raise_for_status()
        
        # Get the first book from the response
        book = response.json()['items'][random.randint(0, 9)]
        
        # Return the book
        return book
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Failed to fetch book from Google Books API")