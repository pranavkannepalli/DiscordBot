# DiscordBot

A Discord slash-command bot for managing to-do lists stored in Firebase.

**What it is**

A learning project for writing a Discord bot and connecting it to a Firebase Realtime Database. Each channel gets associated with a to-do "group" token, and from there you can list, add, remove, and count tasks (including nested subtasks). It shares its backend data with the `to_do_firebase` project. A small Flask webserver runs alongside the bot to keep it alive on always-on hosts.

**Commands**

- `/authwithtoken <token>` — associate the current channel with a group token
- `/todos` — list the open todos for the channel's group
- `/addtodo <description>` — add a todo
- `/removetodo <id>` — remove a todo by id
- `/numtodos` — report how many todos have been created in the group

**Run it**

```bash
pip install -r requirements.txt
```

Set a `DISCORD_TOKEN` in a `.env` file (loaded via python-dotenv), then:

```bash
python main.py
```

**Stack**

Python, discord.py 2.3, Firebase (pyrebase4), Flask keep-alive webserver.
