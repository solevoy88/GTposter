from telethon import TelegramClient
import asyncio
import sys
import random


print(sys.executable)
print('-------------------------------------------------')
print(' ██████╗   ████████╗')
print('██╔════╝   ╚══██╔══╝')
print('██║  ███╗     ██║   ')
print('██║   ██║     ██║   ')
print('╚██████╔╝     ██║   ')
print(' ╚═════╝      ╚═╝   ')
print('-------------------------------------------------')
print('Мануал по использованию данного утилити')
print('https://www.youtube.com/watch?v=yEFrtp8_oIM')
print('-------------------------------------------------')


greetings = ['write your text']
offers = [
    '''
write your text                                                                                                                                                         
    '''
]
endings = [
    'write your text',
    'write your text',
]


accounts = []
print("Введите данные по одному аккаунту в формате api_id:api_hash:phone. Пустая строка - конец ввода.")
while True:
    line = input("Аккаунт: ").strip()
    if not line:
        break
    try:
        api_id_str, api_hash, phone = line.split(":")
        api_id = int(api_id_str)
    except Exception:
        print("Неверный формат. Правильно: api_id:api_hash:phone")
        continue

    channels_input = input(f"Введите каналы для {phone} через запятую (без @): ")
    channels = [c.strip() for c in channels_input.split(',') if c.strip()]

    accounts.append({
        'api_id': api_id,
        'api_hash': api_hash,
        'phone': phone,
        'channels': channels
    })

if not accounts:
    print("Аккаунты не найдены")
    sys.exit(5)


async def run_account(account):
    session_name = f'session_{account["phone"]}'
    client = TelegramClient(session_name, account['api_id'], account['api_hash'])

    try:
        print(f"[{account['phone']}] Запуск клиента...")
        await client.start(phone=account['phone'])
        print(f"[{account['phone']}] Клиент запущен. Сессия: {session_name}.session")

        while True:
            for username in account['channels']:
                bon = f"{random.choice(greetings)} {random.choice(offers)} {random.choice(endings)} #{random.randint(1, 9999)}"
                try:
                    await client.send_message(username, bon)
                    print(f"[{account['phone']}] сообщение отправлено в @{username}")
                except Exception as e:
                    print(f"[{account['phone']}] Ошибка при отправке в @{username}: {e}")
                    await asyncio.sleep(random.randint(2,5))

                await asyncio.sleep(random.randint(10, 15 ))

    except Exception as e:
        print(f"[{account['phone']}] Фатальная ошибка клиента: {e}")
    finally:
        try:
            await client.disconnect()
        except Exception:
            pass
        print(f"[{account['phone']}] Клиент отключён")

# --- Главная функция ---
async def main():
    tasks = []
    for acc in accounts:
        tasks.append(asyncio.create_task(run_account(acc)))
    await asyncio.gather(*tasks)

# --- Запуск ---
if __name__ == "__main__":
    asyncio.run(main())
