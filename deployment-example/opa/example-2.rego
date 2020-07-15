
# This allows GETs and POSTs

package example

import input
default allow = false

allow {
  input["X-Forwarded-Method"] == ["GET","POST"][_]
}
