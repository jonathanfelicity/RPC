import xmlrpc.client

# Create an RPC proxy
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call the remote function
result: int = proxy.add(50, 345)

# Print the result
print("Result:", result)
