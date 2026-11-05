# Program Name: Assignment2.py
# Course: IT3883/Section 85540
# # Student Name: Harash Banga
# Assignment Number: Lab4
# Due Date: 11/06/2026
# Purpose: This is the server side of a two-program socket exercise. It listens for a string
# sent by Program A, converts the received string to all upper case, and sends it back.


import socket

#All global variables need to match
HOST = "127.0.0.1"
PORT = 45000
BUFFER_SIZE = 1024


def main():
    # TCP socket used to connect with the Client program with the IP address and port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Server (Program B) is listening on {HOST}:{PORT}...")

        # Wait for Client (Program A) to connect
        conn, addr = server.accept()
        with conn:
            print(f"Connected to {addr[0]}:{addr[1]}")

            # Receive the string from Client (Program A)
            data = conn.recv(BUFFER_SIZE)
            message = data.decode("utf-8")
            print(f"Received: {message}")

            # Convert to upper case
            reply = message.upper()
            conn.sendall(reply.encode("utf-8"))
            print(f"Sent back: {reply}")


if __name__ == "__main__":
    main()