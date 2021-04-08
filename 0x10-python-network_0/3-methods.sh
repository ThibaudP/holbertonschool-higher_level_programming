#!/usr/bin/env bash
# list all allowed methods on a given URI
curl -sI $1 | grep "Allow:" | cut -f2- -d' '
