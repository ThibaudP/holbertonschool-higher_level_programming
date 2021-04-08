#!/usr/bin/env bash
# curl given URI, get the header and display the Content-Length value
curl -sI $1 | grep "Content-Length" | cut -f2 -d' '