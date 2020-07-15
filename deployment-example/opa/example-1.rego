
# A simple allow all GET requests from anywhere

package example

import input
default allow = false

allow {
  input["X-Forwarded-Method"] == "GET"
}
