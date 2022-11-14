class Waktu:
    
   def __init__(self):
      self.jam = input("masukkan jam : ")
      self.menit = input("masukkan menit : ")
      self.detik = input("masukkan detik : ")

   def displayEmployee(self):
      print (self.jam,":",self.menit,":",self.detik)

waktu = Waktu()     
waktu.displayEmployee()