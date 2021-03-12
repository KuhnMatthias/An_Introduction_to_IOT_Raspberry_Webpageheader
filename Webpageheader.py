import http.client                                   # importing of the http library
conn = http.client.HTTPSConnection("www.uci.edu")    # defining the connection
conn.request("GET", "/")                             # sending a get request
rsp = conn.getresponse()                             # to get / save the response of the server
print(rsp.status, rsp.reason)                        # Prints that the request went through
data = rsp.read()                                    # this will return entire content.
print (data[:1000])                                  # Prints 1000 bytes

