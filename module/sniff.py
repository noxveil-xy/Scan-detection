#ИМПОРТ ----------------------------------------
from scapy.all import sniff, get_working_if, get_if_addr


#КЛАСС УСТРОЙСТВА -------------------------------
class DeviceData:
    def __init__(self):
        self.interface = get_working_if()
        self.work_ip = get_if_addr(self.interface)

    #ПОЛУЧАЕМ ИНТЕРФЕЙС -------------
    def message(self):
        print(self.interface)
        print(self.work_ip)



#КЛАСС СНИФЕР------------------------------------------
class Sniff(DeviceData):
    def __init__(self):
        super().__init__()
        self.filter_traf = "tcp[tcpflags] & tcp-syn !=0"


    #ЗАПУСК МОДУЛЯ -------------------------------------
    def run_sniff(self):
        sniff(
        iface=self.interface,
        filter=self.filter_traf,
        prn= lambda packet: print(packet.summary())
        )


# device = DeviceData()
# device.message()

sniffer = Sniff()

