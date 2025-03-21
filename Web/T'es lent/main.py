import pwn

# pwn.context.log_level = "debug"
host = "ip172-18-0-61-cugup7ol2o90009sm4ug-4000.direct.labs.play-with-docker.com"
port = 4000

def startExploit():
    try:
        Online()
    except:
        pwn.error("C'était un accident ! UN BANAL ACCIDENT DE TRAPÈZE")
    finally:
        pwn.info("Ah ! C'était donc ça tout ce tintouin.")

def Online():
    pwn.info("C'est pas moi ! j'ai vu, je sais qui c'est, mais je ne dirais rien !")
    conn = pwn.remote(host, port)

    while conn.can_recv(timeout=1):
        received = conn.recvline()
        print(str(received))
        if received.startswith(b">>> "):
            verlan = received.strip()[:3:-1] + b"\n"
            conn.send(verlan)
        elif received.startswith(b"FCSC"):
            pwn.info("FLAG FOUND")
            pwn.info(str(received))
            return (received)

def main():
    startExploit()

if __name__ == "__main__":
    main()
