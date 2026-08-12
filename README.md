# DDOS Attack HTTPS HTTP

A lightweight Python script designed to send multi-threaded HTTP/HTTPS GET requests to a target URL for testing and educational purposes.

## Features
* Multi-threaded request execution using Python's `threading` library.
* Automatic URL scheme handling (adds `https://` if missing).
* Built-in error handling for connection resets and dropped responses.
* Clean exit mechanism (`Ctrl + C`).

## Prerequisites
Make sure you have Python 3 and the `requests` library installed on your system.

```bash
pip install requests
