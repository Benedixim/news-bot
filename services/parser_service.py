import time

from parser.manager import ParserManager

import traceback


class ParserService:

    def __init__(self):

        self.manager = ParserManager()

    def parse_once(self):

        self.manager.run()

    def run(self):

        while True:

            try:

                self.parse_once()

            #except Exception as e:

            #    print(e)

            

            except Exception:
                traceback.print_exc()

            print("Следующий парсинг через 10 минут...")

            time.sleep(600)


if __name__ == "__main__":

    ParserService().run()