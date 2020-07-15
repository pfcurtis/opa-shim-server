#!/bin/bash

URL="http://a13becbaa050c42d2a063ca8a63d77cf-1908540072.us-east-2.elb.amazonaws.com/foo"

JWT=$(curl -sd 'anon' ${URL}/token | jq -r .token)

curl -H "Authorization: Bearer $JWT" ${URL}/token/validate
