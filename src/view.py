import colorama
from colorama import Fore, Style, Back


class RidePrinter:
    COLOR_MAP = {
        5: Fore.MAGENTA,
        4: Fore.CYAN,
        3: Fore.BLUE,
        2: Fore.GREEN,
        1: Fore.YELLOW,
        0: Fore.RED
    }

    def __init__(self):
        colorama.init()
        self.curr_color_num = 0

    def print_rider_location(self, rider):
        """Print the current webpage of some WikiRider instance"""
        page_title = rider.html_source.find('title').text.split(' -')[0]
        next_color = self.COLOR_MAP[self.curr_color_num]
        dash_counter = min(rider.depth + 1, 25)
        self.curr_color_num = (self.curr_color_num + 1) % len(self.COLOR_MAP)
        print(Style.BRIGHT + Fore.WHITE + ("-" * dash_counter)
              + page_title + " - " + next_color + rider.next_url
              + Style.RESET_ALL)

    def print_end(self):
        print(Style.BRIGHT + Back.WHITE + Fore.BLACK +
              "You rode the wiki!" + Style.RESET_ALL)

    def print_start(self):
        print("\n" + Style.BRIGHT + Back.WHITE + Fore.BLACK +
              "Starting the track!" + Style.RESET_ALL)

    def print_banner(self):
        print(Style.BRIGHT + Fore.WHITE)
        print("              (_\\")
        print("             / \\")
        print("        `== / /\\=,_")
        print("   _-_-  ;--==\\\\  \\\\o")
        print("_-_-__   /____//__/__\\")
        print("   _-_-  `(0)     (0) ")
        print("\t-WikiRider" + Style.RESET_ALL)

    def print_help(self):
        print(Style.BRIGHT + Fore.WHITE + "\nUsage: " + Fore.YELLOW +
              "./wikirun.py <starting url> <depth>" + Style.RESET_ALL)

    def print_invalid_input_error(self):
        print(Style.BRIGHT + Fore.RED +
              "\nDepth must be a number!\nStarting URL must be a valid "
              "WikiPedia URL!\n(You might me missing https:// and special "
              "pages aren't allowed)!" + Style.RESET_ALL)

    def print_connection_error(self):
        print(Style.BRIGHT + Fore.RED +
              'Cannot connect to WikiPedia.' + Style.RESET_ALL)
