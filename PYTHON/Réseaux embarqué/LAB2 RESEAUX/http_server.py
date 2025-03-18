# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:27:22 2025

@author: coren
"""

import socket
import os
import datetime
import mimetypes
import platform 
import time

def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type or "application/octet-stream"


def handle_request(request):
    request_lines = request.split('\n')
    first_line = request_lines[0].split(' ')
    if len(first_line) < 2:
        return b""
    
    method, resource = first_line[0], first_line[1]
    if method != "GET":
        btn = request.split("\r\n\r\n")[1].replace("="," ")
        print(request,"\nThe button is :",btn)
        ressource = "/control.html"
   
    if resource in ["/", "/index.html"]:
        print(request)
        resource = "/index.html"    

    elif resource == "/control.html":
        print(request)
        resource = "/control.html"

    elif resource == "/status.html":
        print(request)
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

    mime_type = get_mime_type(file_path)
    with open(file_path, "rb") as f:
        file_data = f.read()

    return generate_file_response(200, "OK", mime_type, file_data)

 
def generate_response(status_code, status_message, body):
    http_head = f"HTTP/1.1 {status_code} {status_message}\r\n"
    http_head += "Content-Type: text/html; charset=utf-8\r\n"
    http_head += "Cache-Control: max-age=<10>\r\n"
    http_head += "Expires: ", time.asctime(time.gmtime(time.time()+3600)), " \r\n"
    http_head += "\r\n"
    http_data = f"<html><head><meta charset='utf-8'/></head><body><p>{body}</p></body></html>"
    return http_head.encode("utf-8") + http_data.encode("utf-8")


def generate_file_response(status_code, status_message, mime_type, file_data):
    http_head = f"HTTP/1.1 {status_code} {status_message}\r\n"
    http_head += f"Content-Type: {mime_type}\r\n"
    http_head += "\r\n"
    return http_head.encode("utf-8") + file_data
 

def generate_status_page():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    machine_name = platform.node()
    user_name = os.environ.get("USER", "Unknown")
    body = f"Date: {date}<br>Machine Name: {machine_name}<br>User Name: {user_name}"
    return generate_response(200, "OK", body)
 

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 55000))
    server_socket.listen(5)
    print("Server running on http://127.0.0.1:55000")
    try:
        while True:
            client_socket, _ = server_socket.accept()
            request = client_socket.recv(1024).decode('utf-8', errors='ignore')
            response = handle_request(request)
            client_socket.sendall(response)
            client_socket.close()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server_socket.close()


if __name__ == "__main__":
    main()

 
 