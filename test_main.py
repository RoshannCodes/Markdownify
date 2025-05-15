from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "endpoints" in response.json()

def test_convert_markdown():
    test_markdown = "# Test\nThis is **bold**"
    response = client.post(
        "/convert",
        json={"content": test_markdown}
    )
    assert response.status_code == 200
    html_response = response.json()["html"]
    assert '<h1 id="test">Test</h1>' in html_response
    assert "<strong>bold</strong>" in html_response

def test_convert_markdown_with_extensions():
    test_markdown = """
# Table Example
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

# Code Example
```python
def hello():
    print("Hello World")
```
"""
    response = client.post(
        "/convert",
        json={"content": test_markdown, "enable_extensions": True}
    )
    assert response.status_code == 200
    html_response = response.json()["html"]
    assert '<table>' in html_response
    assert 'class="codehilite"' in html_response  # Check for code highlighting
    assert '<td>Cell 1</td>' in html_response  # Check table cell
