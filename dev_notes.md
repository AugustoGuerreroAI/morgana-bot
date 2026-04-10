### 04-08-2026

Today I decided to look into discord.py, let’s see what I find.

I already have a pretty solid base in Python, so now what I need to do is actually use it and build something that’s fun and interesting for me. So I’m gonna start by reading the discord.py docs and see what it’s all about!!!

---

First of all, I want to learn a bit more about `venv`
**I ran this in my terminal:**
`python -m venv venv`

* `python` calls Python
* `-m` means "module", so I’m telling Python to find this tool in its internal libraries and run it
* `venv` is the name of the internal module
* `venv` (the second one) is the folder name

Since I’m on Windows, I activate it like this:
`.\venv\Scripts\Activate.ps1`

Once I’m inside the venv, I install `discord.py`:

```
PS C:\Users\yoake\OneDrive\Documents\Projectos\discord_bot_python> .\venv\Scripts\Activate.ps1
(venv) PS C:\Users\yoake\OneDrive\Documents\Projectos\discord_bot_python> pip install discord.py
```

`pip freeze > requirements.txt`
This is used to capture the exact dependencies you have at that moment in Python. With `>`, I redirect that output into a `.txt` file so later installing everything is easier.

---

I imported `dot-env` so I can load what’s inside `.env` into the system and then use `os.getenv()` to grab it.

```python
from dotenv import load_dotenv
import os
# This loads the .env into the system, and with os we can access it
load_dotenv()
x = os.getenv("DISCORD_TOKEN")
```

---

**Interesting** concept here. To explain it better, I’ll show the current code:

```python
from dotenv import load_dotenv
import os
import discord
# This loads the .env into the system, and with os we can access it
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
cliente = discord.Client(intents=intents)

@cliente.event
async def on_ready():
    print(f'We have logged as {cliente.user}')

@cliente.event
async def on_message(message):
    if message.author == cliente.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

cliente.run(TOKEN)
```

The decorator `@cliente.event` basically means a **decorator**. It’s not exactly a macro, but more like a way to wrap a function so you can change or extend its behavior without modifying its internal code.

### The anatomy of a decorator 🧬

* **The `@` symbol:** Python syntax to apply a decorator
* **`cliente`:** The bot instance you created before
* **`.event`:** The specific method that registers functions to respond to events from the Discord API


