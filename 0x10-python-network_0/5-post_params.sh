#!/usr/bin/env bash
# sends a POST request to a given URI with specific parameters
curl -X POST -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
