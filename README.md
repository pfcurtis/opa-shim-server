# opa-shim-server

A Proof of Concept to enable OPA policies for traefik without anything but standard Traefik middlewares.

The application `ops-shim-server.py` listens for `fwdauth` requests from the standard Traefik v2.0 forward auth middleware. It
passes the request, complete with all the headers, to a *Open Policy Agent* server. Traefik provides a lot of information
about the request, and those headers can be used to enforce traffic related policy. If there are HTTP authentication or
JWT headers incuded in the request, those will be available to the *Open Polcy Agent* server as well.

This can be run as a pod on Kubernetes, a standalone container in a Docker environment, or as a standalone process.

Unix environment variables are used to configure the *Open Policy Agent* URL and other parameters. Sample Traefik chained 
middleware YAML is provided.

