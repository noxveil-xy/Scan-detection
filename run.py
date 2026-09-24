from module.sniff import sniffer
from datetime import datetime
import scapy
import os


if __name__ == "__main__":
    
    try:
        print(f"\n[{datetime.now()}] [{os.getlogin()}] Захват трафика: \n")
        sniffer.run_sniff()

    except PermissionError:
        print("\nОшибка: недостаточно прав для захвата сетевого трафика..\n")
    except KeyboardInterrupt:
        print(f"\nЗавершение..\n")
    except Exception as err:
        print(f"\nПроизошла неожиданная ошибка: {err}\n")

