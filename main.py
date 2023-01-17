from fastapi import FastAPI, Response
from jinja2 import Template

app = FastAPI()

@app.get("/")
async def root():
    template = Template(open("templates/index.html").read())
    content = template.render()
    return Response(content=content, media_type="text/html")