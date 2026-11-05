# Program Name: Assignment2.py
# Course: IT3883/Section 85540
# # Student Name: Harash Banga
# Assignment Number: Lab4
# Due Date: 11/06/2026
# Purpose: This is the client side of a two-program socket exercise. It listens for a string
# sent by Program A, converts the received string to all upper case, and sends it back.

import socket

#All global variables need to match
HOST = "127.0.0.1"
PORT = 45000
BUFFER_SIZE = 1024


def main():
    message = input("Enter a string to send to the Server (Program B): ")

    # Create a TCP socket and connect to the Server (Program B)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
        except ConnectionRefusedError:
            print("Could not connect. Make sure Program B is running first.")
            return

        # Send the string to the Server (Program B)
        client.sendall(message.encode("utf-8"))

        # Print response
        data = client.recv(BUFFER_SIZE)
        print(f"Received from the Server (Program B): {data.decode('utf-8')}")


if __name__ == "__main__":
    main()