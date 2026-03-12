import discord
import os
import asyncio
from google import genai

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client_ai = genai.Client(api_key=GEMINI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


async def ask_ai(prompt):
    loop = asyncio.get_running_loop()

    response = await loop.run_in_executor(
        None,
        lambda: client_ai.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
    )

    if response.text:
        return response.text
    return "AI không trả lời."


@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")


@bot.event
async def on_message(message):

    if message.author.bot:
        return

    try:
        async with message.channel.typing():

            reply = await ask_ai(message.content)

            # Discord giới hạn 4000 ký tự
            if len(reply) > 3900:
                reply = reply[:3900]

            await message.channel.send(reply)

    except Exception as e:
        print("AI ERROR:", e)
        await message.channel.send("⚠ AI lỗi.")


bot.run(DISCORD_TOKEN)
