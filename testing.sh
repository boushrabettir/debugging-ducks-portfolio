#!/bin/bash

URL="http://127.0.0.1:5000/api/timeline_post"
FILE="id.txt"

nextid() {
  if [ ! -f "$FILE" ]; then
    echo 1 > "$FILE"
  fi

  LAST=$(cat "$FILE")
  NEXT=$((LAST+1))
  echo $NEXT > "$FILE"

  echo $NEXT

}


getreq() {
  GET=$(curl --request GET $URL)
  echo $GET | jq .
}

postreq() {
  ID=$(nextid)
  POST=$(curl --request POST $URL -H "Content-Type: application/json" -d '{
    "name": "Post testing request!",
    "email": "test'${ID}'@example_ssh.com",
    "content": "foo"
  }')

  CREATED_POST_REQ=$(echo $POST | jq '.id')
  if [ -z "$CREATED_POST_REQ" ]; then
    echo "Post request failed."
    exit 1
  else
    echo "Post request successful."
  fi
}

echo "Testing post request!"
postreq

echo "Testing get request!"
getreq

echo "Post and get successful!"




