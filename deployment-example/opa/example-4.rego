
# This example refines exactly which URIs in the same path (/foo/bar) can
# GET & POST. It also allows for ANY get or POST including and below the /foo URI GET & POST


package example

import input
default allow = false

allow {
  array.slice(input["X-Forwarded-Uri"],0,2) == ["foo","bar"]
  input["X-Forwarded-Method"] == ["GET","POST"][_]
}

allow {
  input["X-Forwarded-Uri"][0] == "bar"
  input["X-Forwarded-Method"] == ["GET","POST"][_]
}

allow {
  input["X-Forwarded-Uri"] == ["foo"]
  count(input["X-Forwarded-Uri"]) == 1
  input["X-Forwarded-Method"] == "GET"
}
