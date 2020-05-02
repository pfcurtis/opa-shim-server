package example

import input
default allow = false

allow {
  input["X-Forwarded-Method"] == "GET"
  input["X-Real-Ip"] == "192.168.42.1"
}
