from xmlrpc.server import SimpleXMLRPCServer

# Define the function to be exposed
def add(x: int, y: int)-> int:
    return x + y

# Create the server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server listening on port 8000...")

# Register the function
server.register_function(add, "add")

# Start the server
server.serve_forever()
