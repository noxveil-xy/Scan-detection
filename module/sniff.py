#ИМПОРТ ----------------------------------------
from scapy.all import sniff, get_working_if, get_if_addr
from module.files import clear_buffer, save_in_buffer


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
        self.filter_traf = "tcp[tcpflags] & tcp-ack !=0"


    def save_packets(self, packet):
        value_dump = str(packet)
        save_in_buffer(value_dump)
        print(packet.summary())


    #ЗАПУСК МОДУЛЯ -------------------------------------
    def run_sniff(self):

        clear_buffer()

        sniff(
        iface=self.interface,
        filter=self.filter_traf,
        prn=self.save_packets)





# device = DeviceData()
# device.message()

sniffer = Sniff()

