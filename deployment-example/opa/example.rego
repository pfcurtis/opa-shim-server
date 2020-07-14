package example

import input
default allow = false

allow {
  input["X-Forwarded-Method"] == "GET"
}
