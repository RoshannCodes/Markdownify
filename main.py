from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import markdown
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI(title="Markdown Converter API",
             description="A service that converts Markdown to HTML with advanced features")

# Enable CORS for web interface
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MarkupInput(BaseModel):
    content: str
    enable_extensions: Optional[bool] = True

@app.post("/convert")
def convert_markup_to_html(input: MarkupInput):
    try:
        # Use additional extensions for better markdown support
        extensions = [
            'markdown.extensions.fenced_code',  # Code blocks with ```
            'markdown.extensions.tables',       # Tables support
            'markdown.extensions.footnotes',    # Footnotes
            'markdown.extensions.toc',          # Table of contents
            'markdown.extensions.codehilite',   # Syntax highlighting
        ] if input.enable_extensions else []
        
        html = markdown.markdown(input.content, extensions=extensions)
        return {"html": html}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Markdown Converter API",
        "endpoints": {
            "convert": "POST - Convert markdown to HTML",
            "docs": "GET - API documentation"
        },
        "example": {
            "request": {
                "content": "# Hello\\nThis is **markdown**",
                "enable_extensions": True
            }
        }
    }