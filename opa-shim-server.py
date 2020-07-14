#!/usr/bin/env python3

import os, json, urllib3
import http.server
import socketserver

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
 
        data = {}
        data[opa_input_object] = {}
        try:
            data[opa_input_object]['request_path'] = self.path.strip("/").split("/")
        except:
            pass

        for hdr in self.headers.keys():
          if (hdr == opa_path_header):
            data[opa_input_object][hdr] = self.headers.get(hdr).strip("/").split("/")
          else:
            data[opa_input_object][hdr] = self.headers.get(hdr)

        if (opa_debug == "True"):
          print("OPA Data Sent:\n")
          print(json.dumps(data))
          print("--------\n")

        try:
            opa = http.request("POST",opa_url, headers={'Content-Type': 'application/json'}, body=json.dumps(data))
        except:
            self.send_response(403,"Unauthorized")
            self.end_headers()
            self.wfile.write(b"Access Denied. Failed to contact policy server.\n")
            return

        try:
            resp = json.loads(opa.data.decode('utf-8'))['result']
        except:
            self.send_response(403,"Unauthorized")
            self.end_headers()
            self.wfile.write(b"Access Denied. Failed to decode policy server response\n")
            return

        if (opa_debug == "True"):
          print(json.dumps(resp))
          print("++++++++\n")

        if (resp[opa_allow_attribute]):
          self.send_response(200,"OK")
          self.end_headers()
          self.wfile.write(b"OK body\n")
        else:
          self.send_response(403,"Unauthorized")
          self.end_headers()
          self.wfile.write(b"Access Denied. Policy does not allow access.\n")
        
def main():
    print('Listening on :%s' % port)
    server = socketserver.ThreadingTCPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":

    # All configuration from the environment with defaults
    port = os.environ.get('SHIM_SERVER_PORT', 8080)
    opa_url = os.environ.get('OPA_URL','http://opa.www:8181/v1/data/example')
    opa_input_object = os.environ.get('OPA_INPUT_OBJECT','input')
    opa_path_header = os.environ.get('OPA_PATH_HEADER','X-Forwarded-Uri')
    opa_allow_attribute = os.environ.get('OPA_ALLOW_ATTRIBUTE','allow')
    opa_debug = os.environ.get('OPA_DEBUG','False')

    http = urllib3.PoolManager()

    main()
