def on_log(client, userdata, level, buf):
    print("log: " + buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")
    else:
        print("Bad connection, returned code = ", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected, returned code = " + str(rc))


def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("Message received", m_decode)
