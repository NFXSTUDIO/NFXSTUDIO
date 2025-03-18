# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 15:42:16 2025

@author: arthu
"""

import socket
import os
import datetime
import mimetypes
import platform
import time
import threading

def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type or "application/octet-stream"

def handle_request(request):
    request_lines = request.split('\n')
    first_line = request_lines[0].split(' ')
    if len(first_line) < 2:
        return b""

    method, resource = first_line[0], first_line[1]

    if method == "POST":
        return handle_post_request(request)

    if method != "GET":
        return generate_response(405, "405 Method Not Allowed", "Cette méthode n'est pas prise en charge.")

    if resource in ["/", "/index.html"]:
        resource = "/index.html"
    elif resource == "/status.html":
        return generate_status_page()
    file_path = "www" + resource
    if not os.path.isfile(file_path):
        return generate_response(404, "404 Not Found", "Page non trouvée.")

    mime_type = get_mime_type(file_path)
    file_mod_time = os.path.getmtime(file_path)
    file_mod_gmt = time.gmtime(file_mod_time)
    file_mod_str = time.strftime("%a, %d %b %Y %H:%M:%S GMT", file_mod_gmt)

    # Check for If-Modified-Since header
    if_modified_since = None
    for line in request_lines:
        if line.startswith("If-Modified-Since:"):
            if_modified_since = line.split(":", 1)[1].strip()
            break

    if if_modified_since and if_modified_since == file_mod_str:
        return generate_response(304, "Not Modified")

    # Read file content
    with open(file_path, "rb") as f:
        file_data = f.read()

    return generate_response(200, "OK", file_data=file_data, mime_type=mime_type,
                            last_modified=file_mod_str)

def handle_post_request(request):
    binsep = b"\r\n\r\n"
    request_parts = request.encode('utf-8').split(binsep, 1)
    if len(request_parts) < 2:
        return generate_response(400, "400 Bad Request", "Requête mal formée.")
    
    post_data = request_parts[1].decode('utf-8')
    print(post_data)
    
    file_path = "www/control.html"
    if not os.path.isfile(file_path):
        return generate_response(404, "404 Not Found", "Page non trouvée.")
    
    # Read and return the control.html file
    with open(file_path, "rb") as f:
        file_data = f.read()

    return generate_response(200, "OK", file_data=file_data, mime_type="text/html")

def generate_response(status_code, status_message, body=None, mime_type="text/html", file_data=None, last_modified=None):
    http_head = f"HTTP/1.1 {status_code} {status_message}\r\n"
    http_head += f"Content-Type: {mime_type}\r\n"
    http_head += "Cache-Control: max-age=10\r\n"
    http_head += f"Expires: {time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(time.time() + 10))}\r\n"
    
    if last_modified:
        http_head += f"Last-Modified: {last_modified}\r\n"

    http_head += "\r\n"
    
    if file_data:
        return http_head.encode("utf-8") + file_data
    else:
        http_data = f"<html><head><meta charset='utf-8'/></head><body><p>{body}</p></body></html>"
        return http_head.encode("utf-8") + http_data.encode("utf-8")

def generate_status_page():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    machine_name = platform.node()
    user_name = os.environ.get("USER", "Unknown")
    body = f"Date: {date}<br>Machine Name: {machine_name}<br>User Name: {user_name}"
    return generate_response(200, "OK", body)

def handle_client(client_socket):
    try:
        client_address = client_socket.getpeername()  # Récupère l'adresse IP et le port du client
        print(f"Connexion de {client_address[0]}:{client_address[1]}")  # Affiche l'adresse IP et le port du client
        request = client_socket.recv(1024).decode('utf-8', errors='ignore')
        response = handle_request(request)
        client_socket.sendall(response)
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.9.158.25', 55000))
    server_socket.listen(5)
    print("Server running on http://10.9.158.25:55000")
    
    try:
        while True:
            client_socket, _ = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server_socket.close()

if __name__ == "__main__":
    main()