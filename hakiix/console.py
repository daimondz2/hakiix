import os
from datetime import datetime, timezone, timedelta

class LocalColors:
    reset = "\033[0m"
    bold = "\033[1m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    bright_red = "\033[91m"
    bright_green = "\033[92m"
    bright_yellow = "\033[93m"
    bright_blue = "\033[94m"
    bright_magenta = "\033[95m"
    bright_cyan = "\033[96m"
    bright_white = "\033[97m"
    neon_green = "\033[38;5;46m"
    neon_red = "\033[38;5;196m"
    neon_blue = "\033[38;5;51m"
    neon_yellow = "\033[38;5;226m"
    neon_purple = "\033[38;5;129m"
    neon_cyan = "\033[38;5;50m"

class Logger:
    def time_now(self):
        now = datetime.now(timezone(timedelta(hours=7)))
        return now.strftime("%H:%M:%S")

    def suc(self, message):
        prefix = f"{LocalColors.neon_green}{LocalColors.bold}[ SUCC ]{LocalColors.reset}"
        print(f"{prefix} {LocalColors.white}{self.time_now()} | {message}{LocalColors.reset}")

    def err(self, message):
        prefix = f"{LocalColors.neon_red}{LocalColors.bold}[ ERRO ]{LocalColors.reset}"
        print(f"{prefix} {LocalColors.white}{self.time_now()} | {message}{LocalColors.reset}")

    def fail(self, message):
        prefix = f"{LocalColors.neon_red}{LocalColors.bold}[ FAIL ]{LocalColors.reset}"
        print(f"{prefix} {LocalColors.white}{self.time_now()} | {message}{LocalColors.reset}")
    
    def info(self, message):
        prefix = f"{LocalColors.neon_blue}{LocalColors.bold}[ INFO ]{LocalColors.reset}"
        print(f"{prefix} {LocalColors.white}{self.time_now()} | {message}{LocalColors.reset}")

    def dbg(self, message):
        prefix = f"{LocalColors.neon_purple}{LocalColors.bold}[ DEBG ]{LocalColors.reset}"
        print(f"{prefix} {LocalColors.white}{self.time_now()} | {message}{LocalColors.reset}")

    def warn(self, message):
        prefix = f"{LocalColors.neon_yellow}{LocalColors.bold}[ WARN ]{LocalColors.reset}"
        print(f"{prefix} {LocalColors.white}{self.time_now()} | {message}{LocalColors.reset}")

    def token(self, token):
        prefix = f"{LocalColors.neon_cyan}{LocalColors.bold}[ TOKN ]{LocalColors.reset}"
        display = token[:25] + ("..." if len(token) > 25 else "")
        print(f"{prefix} {LocalColors.white}{self.time_now()} | {display}{LocalColors.reset}")

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

log = Logger()
console = log

log_info = log.info
log_warn = log.warn
log_success = log.suc
log_error = log.err
log_dbg = log.dbg
log_token = log.token
