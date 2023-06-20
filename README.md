HTML-to-PDF
==

This is a simple Docker container that accepts a string of HTML posted to `/pdf` and returns PDF data rendered by Chromium and printed to PDF through Selenium. Made for a personal project, but here for anyone who might need an accurate HTML to PDF renderer.

Usage
==

Usage is simple:

```bash
docker build . -t html2pdf
docker run \
-p 8080:8080 \
-d \
--restart=always \
html2pdf
```

Then simply POST raw HTML to `http://localhost:8080/pdf` and save the returned PDF data:

```bash
curl \
-X POST \
-d "<html><p>Your HTML here.</p></html>" \
http://localhost:8080/pdf
```