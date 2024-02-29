#!/bin/bash
# send a request to the URL and displays the size of the body of the response
curl -Is "$1"| grep "Content-Length" | cut -d " " -f2
