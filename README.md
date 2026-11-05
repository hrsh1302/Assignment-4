# Assignment 4
## Purpose

Two small Python programs that use sockets to communicate with each other over a network. 
Program A (the client) sends a string typed by the user to Program B (the server), which converts 
it to upper case and sends it back.

## Features

- **Client/server communication:** the two programs talk over a TCP socket using Python's built-in
`socket` module.
- **User input:** Program A prompts the user to type any string.
- **Upper case conversion:** Program B converts the received string to all upper case and returns it.
- **Hard-coded address:** both programs use `127.0.0.1` (localhost) on port `45000`, 
a port above 40000 that is unlikely to be in use.
- **Connection check:** if Program B is not running, Program A shows a message instead of crashing.

## How It Works

- **Program B (`ProgramB_Server.py`)** creates a TCP socket, binds it to `127.0.0.1:45000`,
and waits for a connection with `listen()` and `accept()`.

- **Program A (`ProgramA_Client.py`)** asks the user for a string, 
then connects to the same address and port with `connect()`.

- The exchange happens in order:
   - **Send:** Program A encodes the string to bytes and sends it with `sendall()`.
   - **Receive:** Program B reads the bytes with `recv()` and decodes them back into a string.
   - **Convert:** Program B calls `.upper()` on the string.
   - **Reply:** Program B sends the upper case string back, and Program A prints it to the console.

### How to Run
Run `ProgramB_Server.py` first and then run `ProgramA_Client.py` in a second window to type a string.

## Output

### Server waiting for a connection
- When Program B starts, it waits for Program A to connect.
![Server listening](img(1).png)

### Client sending a string
- Program A sends `hello there` and prints the upper case reply.
![Client output](img(2).png)

### Server receiving and replying
- Program B shows the connection, the string it received, and the string it sent back.
![Server output](img(3).png)