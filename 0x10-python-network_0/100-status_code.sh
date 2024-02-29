#!/bin/bash
# request to a URL passed as an argument and displays only the status code
curl -sLX HEAD -w "%{http_code}" $1
