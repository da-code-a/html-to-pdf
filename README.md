HTML-to-PDF
==

This is a simple Docker container that accepts a string of HTML posted to `/pdf` and returns PDF data rendered by Chromium and printed to PDF through Selenium. Made for a personal project, but here for anyone who might need an accurate HTML to PDF renderer.

Usage
==

Usage is simple:

```bash
docker run \
-p <YOUR_DESIRED_PORT>:8080 \
-d \
--restart=always \
donaldkbrown214/html-to-pdf
```

Then simply POST raw HTML to `http://<your_host>:<your_port>/pdf` and save the returned PDF data.