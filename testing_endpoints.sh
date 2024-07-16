#!/bin/bash

URL="http://127.0.0.1:5000/api/timeline_post"
ID_FILE="last_id.txt"


get_next_id() {
  if [ ! -f "$ID_FILE" ]; then
    echo 1 > "$ID_FILE"
  fi

  LAST=$(cat "$ID_FILE")
  NEXT=$((LAST+1))
  echo $NEXT > "$ID_FILE"

  echo $NEXT

}

ID=$(get_next_id)

# POST REQUEST
echo "POST REQUEST"
POST=$(curl --request POST $URL -H "Content-Type: application/json" -d  "{
  "name": "TESTING SSH",
  "email": "TESTING'${ID}'@example_ssh.com",
  "content": "testing"
}")


CREATED=$(echo $POST | jq '.id')
if [ -z "$CREATED" ]; then
  echo "Failure!"
  exit 1
else
  echo "Post created successfully!"
fi


echo "GET REQUEST"
GET=$(curl --request GET $URL)
echo $GET | jq .

