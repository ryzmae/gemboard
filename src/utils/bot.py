__version__ = "1.0.0"
__time__ = 15

import os
import asyncio

import discord

from discord.ext import commands
from colorama import init, Fore, Style
from dotenv import load_dotenv

from .util import timestamp
from .logger import Logger

load_dotenv()

init(autoreset=True)

class Gemboard(discord.AutoShardedBot):
    def __init__(
        self,
        token: str = os.getenv("TOKEN"),
        intents: discord.Intents = discord.Intents.all(),
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            description=kwargs.get("description", "A Discord bot made with PyCord"),
            intents=intents,
            *args,
            **kwargs,
        )

        self._token = token
        self.logger = Logger()

        self.add_listener(self.ready, "on_ready")
        self.add_listener(self._error, "on_application_command_error")

        self.no_emoji = "<:no:1091798422421512274>"

    async def ready(self) -> None:
        self.logger.info(f"Logged in as {self.user} ({self.user.id})")

        await self.change_presence(
            activity=discord.Game(
                name="Starting..."
            ),
            status=discord.Status.do_not_disturb
        )

        await asyncio.sleep(__time__)

        await self.change_presence(
            activity=discord.Streaming(
                name=f"{__version__} - Cluster #0", url="https://twitch.tv/#"
            )
        )

    async def _error(
        self, ctx: discord.ApplicationContext, error: discord.DiscordException
    ) -> None:
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.respond(
                f">>> {self.no_emoji} i am missing the following permissions {', '.join(error.missing_permissions)}",
            )
            return

        if isinstance(error, commands.MissingPermissions):
            await ctx.respond(
                f">>> {self.no_emoji} you are missing the following permissions {', '.join(error.missing_permissions)}",
            )
            return

        if isinstance(error, commands.CommandOnCooldown):
            sec = round(ctx.command.get_cooldown_retry_after(ctx))

            await ctx.respond(
                f">>> {self.no_emoji} you are on cooldown, try again in {timestamp(sec)}",
            )
            return

        else:
            await ctx.respond(
                f">>> {self.no_emoji} something went wrong, please try again later",
            )
            self.logger.error(error)
            return

    def loadCommands(self, dir: str, sub: bool) -> None:
        if sub:
            for sub in os.listdir(dir):
                if os.path.isdir(f"{dir}/{sub}"):
                    self._load_Commands(f"{dir}/{sub}")

        else:
            self._load_Commands(dir)

    def _load_Commands(self, dir: str) -> None:
        for file in os.listdir(dir):
            if file.endswith(".py"):
                full_path = os.path.join(dir, file[:-3]).replace("/", ".")
                self.load_extension(full_path)
                self.logger.info(f"Loaded {full_path}")

    def run(self) -> None:
        super().run(self._token)
