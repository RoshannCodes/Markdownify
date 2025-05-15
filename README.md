# FastAPI Markdown Converter

A robust FastAPI application that converts Markdown to HTML with support for advanced markdown features. Perfect for integrating into documentation systems, blog platforms, or any application requiring markdown processing.

[GitHub Repository Link] - *Add your GitHub repository link here after pushing the code*

## Features

- Convert Markdown to HTML
- Support for advanced Markdown extensions:
  - Fenced code blocks with syntax highlighting
  - Tables
  - Footnotes
  - Table of contents generation
  - Code syntax highlighting
- RESTful API with Swagger documentation
- CORS enabled for web integration
- Comprehensive test suite
- Docker support for easy deployment

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Docker (optional)

### Running Locally

1. Clone the repository:
```bash
git clone [your-repo-url]
cd [repository-name]
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

### Running with Docker

1. Build the Docker image:
```bash
docker build -t markdown-converter .
```

2. Run the container:
```bash
docker run -p 8000:8000 markdown-converter
```

The application will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Swagger UI documentation at `http://localhost:8000/docs`
- ReDoc documentation at `http://localhost:8000/redoc`

## Testing

Run the tests using pytest:
```bash
pytest
```

## Demo

[Screen Recording Link] - *Add your screen recording link here*

The demo shows:
- Application startup
- API endpoints in action
- Test execution
- CI workflow (if applicable)

## CI/CD

*Add information about your CI setup once configured*

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the application:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Using Docker

1. Build the Docker image:
```bash
docker build -t fastapi-markdown .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 --name markdown-converter fastapi-markdown
```

## API Usage

### Convert Markdown to HTML

```bash
curl -X POST "http://localhost:8000/convert" \
     -H "Content-Type: application/json" \
     -d '{"content": "# Hello\nThis is **markdown**"}'
```

### API Documentation

Visit http://localhost:8000/docs for interactive API documentation.

## Testing

Run the tests using pytest:

```bash
pytest test_main.py -v
```

## Configuration

No additional configuration is required. The API is ready to use out of the box.

## Project Structure

```
.
├── Dockerfile           # Docker configuration
├── README.md           # Project documentation
├── main.py            # FastAPI application
├── requirements.txt   # Python dependencies
└── test_main.py      # Test suite
```

## Sample Markdown Features

The API supports various markdown features:

1. Headers
2. **Bold** and *italic* text
3. Code blocks with syntax highlighting
4. Tables
5. Footnotes
6. And more!

Example with all features:

\```markdown
# Title

## Table Example
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

## Code Example
\```python
def hello_world():
    print("Hello from Python!")
\```

## Footnotes
Here's a footnote[^1]

[^1]: This is the footnote content
\```

## Next Steps

- [ ] Add support for custom CSS
- [ ] Implement rate limiting
- [ ] Add caching for frequent conversions
- [ ] Create a web frontend
