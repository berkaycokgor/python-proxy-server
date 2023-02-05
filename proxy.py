import socket
import json

#customizable python server for your needs, I mainly made chatpgt generate this code for a ctf question but it can be used for anything
def start_proxy_server():
    host = '127.0.0.1'
    port = 8080

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)

    print(f"Proxy server started on {host}:{port}")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()

        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        # Receive the HTTP request
        request = client_socket.recv(4096).decode()
        print(f"Received request:\n{request}")

        # CUSTOMIZE OR DELETE IT HOWEVER YOU WANT UNTIL LINE 56
        if("value" in request):
            json_data = None
            try:
                start_index = request.index("{")
                end_index = request.rindex("}") + 1
                json_str = request[start_index:end_index]
                json_data = json.loads(json_str)
            except ValueError:
                pass

            # Modify the request's JSON data if necessary
            if json_data is not None:
                json_data["value"] = "value"
                new_json_str = json.dumps(json_data)
                request = request.replace(json_str, new_json_str)

                # Modify the Content-Length header to reflect the new length of the JSON data
                content_length_header = f"Content-Length: {len(new_json_str)}\r\n\n"
                content_length_header_index = request.index("Content-Length:")
                end_of_header_index = request.index("\r\n\r\n") + 4
                request = request[:content_length_header_index] + content_length_header + request[end_of_header_index:]

                print(f"Modified request:\n{request}")
                ok=input("Please confirm\n")
                if(ok != "ok"):
                    break
        # Forward the request to the desired server
        # (Note: This is a simplified example that assumes the desired server is always available)
        server_socketx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socketx.connect(('x.x.x.x', y))
        server_socketx.sendall(request.encode())

        # Receive the response from the desired server
        response = server_socketx.recv(4096).decode()
        print(f"Received response:\n{response}")

        # Modify the response if necessary

        # Return the response to the client
        client_socket.sendall(response.encode())

        # Close the client and server connections
        client_socket.close()
        server_socketx.close()

if __name__ == '__main__':
    start_proxy_server()
    
