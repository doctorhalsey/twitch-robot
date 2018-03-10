import mqtt
import twitch

m = mqtt.Mqtt()
t = twitch.Twitch()

valid_msg = ["up", "down", "left", "right"]

username = "user"
key = "key"
t.twitch_connect(username, key)

while True:
    new_messages = t.twitch_recieve_messages()

    if not new_messages:
        continue
    else:
        for message in new_messages:
            msg = message['message'].lower()
            username = message['username'].lower()
            print(username + ": " + msg)

            if msg in valid_msg:   
                m.publish(msg)
            else:
                m.publish("invalid msg")
        