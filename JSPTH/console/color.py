

class Color:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    AQUAMARINE = "\033[36m"
    AQUA = "\033[36m"
    BLACK = "\033[30m"
    BROWN = "\033[33m"
    ORANGE = "\033[33m"
    PURPLE = "\033[35m"
    PINK = "\033[35m"
    HOT_PINK = "\033[35m"
    

    @staticmethod
    def color_text(text, color):
        return f"{color}{text}{Color.RESET}"
    
