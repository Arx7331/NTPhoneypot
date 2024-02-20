import socket
from telegram import Bot
import asyncio
from datetime import datetime
token = 'your telegram bot token'
chatid = 'chat id'

def check(data):
    payload = b'\x17\x00\x03\x2a\x00\x00\x00\x00'
    return data == payload

async def telegram(message):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chatid, text=message)

async def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server = ('', 123)
    sock.bind(server)
    
    print("Listening on port 123...")
    
    try:
        while True:
            data, address = sock.recvfrom(4096)
            if check(data):
                message = f"Received NTP amplification packet from {address[0]}:{address[1]}\nData: {data.hex()}\n{str(datetime.now())}"
                print(message)
                await telegram(message)
    finally:
        sock.close()

if __name__ == "__main__":
    asyncio.run(main())
