from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()
api_id = int(os.getenv('api_id'))
api_hash = os.getenv('api_hash')
phone_number = os.getenv('phone_number')


async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            code = input('Enter the code: ')
            await client.sign_in(phone_number, code)

        async for dialog in client.iter_dialogs():
            if dialog.archived:
                print(f'{dialog.name} - {dialog.id} is archived')
                await client.delete_dialog(dialog.id)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
