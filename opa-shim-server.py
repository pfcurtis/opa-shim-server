#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

import os, json, urllib3
import http.server
import socketserver

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
 
        data = {}
        data[opa_input_object] = {}
        data[opa_input_object]['request_path'] = self.path.strip("/").split("/")

        for hdr in self.headers.keys():
          if (hdr == opa_path_header):
            data[opa_input_object][hdr] = self.headers.get(hdr).strip("/").split("/")
          else:
            data[opa_input_object][hdr] = self.headers.get(hdr)

#       print("OPA Data Sent:\n")
#       print(json.dumps(data))
#       print("--------\n")

        opa = http.request("POST",opa_url, headers={'Content-Type': 'application/json'}, body=json.dumps(data))
        resp = json.loads(opa.data.decode('utf-8'))['result']

#       print(json.dumps(resp))
#       print("++++++++\n")

        if (resp[opa_allow_attribute]):
          self.send_response(200,"OK")
          self.end_headers()
          self.wfile.write(b"OK body\n")
        else:
          self.send_response(403,"Unauthorized")
          self.end_headers()
          self.wfile.write(b"Denied\n")
        
def main():
    print('Listening on :%s' % port)
    server = socketserver.TCPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":

    # All configuration from the environment with defaults
    port = os.environ.get('SHIM_SERVER_PORT', 8080)
    opa_url = os.environ.get('OPA_URL','http://opa.www:8181/v1/data/example')
    opa_input_object = os.environ.get('OPA_INPUT_OBJECT','input')
    opa_path_header = os.environ.get('OPA_PATH_HEADER','X-Forwarded-Uri')
    opa_allow_attribute = os.environ.get('OPA_ALLOW_ATTRIBUTE','allow')

    http = urllib3.PoolManager()

    main()
