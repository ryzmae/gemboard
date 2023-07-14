import logging
import os
import datetime

from colorama import init, Fore, Style

strings = {
    "info": " Info",
    "error": "Error",
    "debug": "Debug",
    "warn": " Warn"
}

class Logger:
    def __init__(
            self,
            file: str = "logs/logging.log",
            prefix: str = "BOT"
    ) -> None:
        self.file = file
        self.prefix = prefix
        init(
            autoreset=True
        )

        if not os.path.exists("logs"):
            os.mkdir("logs")

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(file)
        file_handler.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
    
    def _space(self) -> str:
        return f"{Fore.MAGENTA}{Style.BRIGHT}::{Fore.RESET}{Style.RESET_ALL} "

    def _with_date(self) -> str:
        Time = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")

        return f"{Fore.LIGHTBLACK_EX}{Style.BRIGHT}{Time}{Fore.RESET}{Style.RESET_ALL} "

    def _with_prefix(self) -> str:
        return f"{Fore.YELLOW}{Style.BRIGHT}{self.prefix}{Fore.RESET}{Style.RESET_ALL} "
    
    def info(self, message: str) -> str:
        self.logger.info(f"{message}")
        return print(f"{Style.BRIGHT}{Fore.GREEN}✔ {self._with_date()}{self._with_prefix()}{self._space()}{Style.BRIGHT}{Fore.CYAN} {strings['info']} || {Fore.BLUE}{message}")
    
    def error(self, message: str) -> str:
        self.logger.error(f"{message}")
        return print(f"{Fore.RED}{Style.BRIGHT}✘ {self._with_date()}{self._with_prefix()}{self._space()}{Style.BRIGHT}{Fore.LIGHTRED_EX} {strings['error']} || {Fore.RED}{message}")
    
    def debug(self, message: str) -> str:
        self.logger.debug(f"{message}")
        return print(f"{Style.BRIGHT}{Fore.GREEN}✔ {self._with_date()}{self._with_prefix()}{self._space()}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX} {strings['debug']} || {Fore.YELLOW}{message}")
    
    def warn(self, message: str) -> str:
        self.logger.warning(f"{message}")
        return print(f"{Fore.RED}{Style.BRIGHT}⚠ {self._with_date()}{self._with_prefix()}{self._space()}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} {strings['warn']} || {Fore.MAGENTA}{message}")