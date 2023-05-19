import xmlrpc.client

# Create an RPC proxy
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call the remote function
result = proxy.add(5, 3)

# Print the result
print("Result:", result)
