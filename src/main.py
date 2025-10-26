import os
import time
from instagrapi import Client 

IG_USERNAME = os.environ.get("IG_USERNAME")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
SESSION_FILE = "session.json"

custom_cmds = {}

def login() -> Client:
    cl = Client()
    if os.path.exists(SESSION_FILE):
        cl.load_settings(SESSION_FILE)
    cl.login(IG_USERNAME, IG_PASSWORD)
    cl.dump_settings(SESSION_FILE)
    return cl

def handle_message(cl: Client, thread, message_text: str):
    cmd_split = message_text.split(maxsplit=2)
    cmd = cmd_split[0].lower()
    match cmd:
        case "ping":
            cl.direct_send(text="Pong!", thread_ids=[thread.id])
        case "add":
            if len(cmd_split) >= 3:
                trigger = cmd_split[1].lower()
                response = cmd_split[2]
                custom_cmds[trigger] = response
                cl.direct_send(text=f"Added command '{trigger}'", thread_ids=[thread.id])
        case "delete":
            if len(cmd_split) >= 2:
                trigger = cmd_split[1].lower()
                if trigger in custom_cmds:
                    del custom_cmds[trigger]
                    cl.direct_send(text=f"Deleted command '{trigger}'", thread_ids=[thread.id])
                else:
                    cl.direct_send(text=f"Command '{trigger}' not found", thread_ids=[thread.id])
        case _:
            if cmd in custom_cmds:
                response = custom_cmds[cmd]
                cl.direct_send(text=response, thread_ids=[thread.id])
            else:
                cl.direct_message_seen(thread.id, thread.messages[0].id)


if __name__ == "__main__":
    cl = login()
    print("Logged in successfully.")
    while True:
        threads = cl.direct_threads()
        unread_threads = [thread for thread in threads if thread.read_state == 1]
        
        for thread in unread_threads:
            message_text = thread.messages[0].text
            if message_text:
                handle_message(cl, thread, message_text)
                print(f"Handled message: {message_text} from thread ID: {thread.id}")
        
        time.sleep(1)