import colorama

colorama.init()


class Logger:
    SUCCESS_COLOR = colorama.Fore.GREEN
    WARN_COLOR = colorama.Fore.YELLOW
    ERROR_COLOR = colorama.Fore.RED
    INFO_COLOR = colorama.Fore.BLUE
    RESET_COLOR = colorama.Style.RESET_ALL

    @staticmethod
    def error(message: str, prefix: bool = True) -> None:
        pre = "ERROR: " if prefix else ""
        print(f"{Logger.ERROR_COLOR}{pre}{message}{Logger.RESET_COLOR}")

    @staticmethod
    def warn(message: str, prefix: bool = False) -> None:
        pre = "WARNING: " if prefix else ""
        print(f"{Logger.WARN_COLOR}{pre}{message}{Logger.RESET_COLOR}")

    @staticmethod
    def info(message: str, prefix: bool = False) -> None:
        pre = "INFO: " if prefix else ""
        print(f"{Logger.INFO_COLOR}{pre}{message}{Logger.RESET_COLOR}")

    @staticmethod
    def success(message: str, prefix: bool = False) -> None:
        pre = "SUCCESS: " if prefix else ""
        print(f"{Logger.SUCCESS_COLOR}{pre}{message}{Logger.RESET_COLOR}")
