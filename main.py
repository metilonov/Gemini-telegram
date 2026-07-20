from imports import *

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()
client = genai.Client(api_key=GEMINI_API_KEY)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Бот запущен. Напишите сообщение.")

@dp.message(F.text)
async def chat(message: Message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message.text
        )
        await message.answer(response.text)
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
