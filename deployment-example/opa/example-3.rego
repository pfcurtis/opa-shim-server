
# This example refines exactly which URIs in the same path (/foo/bar) can
# GET & POST

package example

import input
default allow = false

allow {
  array.slice(input["X-Forwarded-Uri"],0,2) == ["foo","bar"]
  input["X-Forwarded-Method"] == ["GET","POST"][_]
}

allow {
  input["X-Forwarded-Uri"] == ["foo"]
  count(input["X-Forwarded-Uri"]) == 1
  input["X-Forwarded-Method"] == "GET"
}

allow {
  input["X-Forwarded-Uri"] == ["bar"]
  count(input["X-Forwarded-Uri"]) == 1
  input["X-Forwarded-Method"] == "GET"
}
