# Quyidagi parametr va metodlardan foydalanib, Shareholder nomli class yarating.
#  Dastur classdan tashqari to’g’ridan to’gri aksiyadorning ismi va kompaniyadagi 
#  ulushini bilishga yo’l qo’ymasin.
# Shareholder atributlari: name, shareholding
# Shareholder metodlari: get_info(), set_name(), set_shareholding()

class Shareholder:
    def __init__(self, name, shareholding):
        self.name = name
        self.shareholding = shareholding

    def get_info(self):
        print(f"Aksiyador nomi: {self.name}")
        print(f"Kompaniyadagi aksiyadorlik: {self.shareholding}%")

    def set_name(self, new_name):
        self.name = new_name

    def set_shareholding(self, new_shareholding):
        self.shareholding = new_shareholding

if __name__ == "__main__":
    shareholder = Shareholder("Surayyo", 30)
    shareholder.get_info()

    shareholder.set_name("Surayyo")
    
    shareholder.set_shareholding(25)
    
    shareholder.get_info()
