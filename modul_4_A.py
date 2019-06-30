class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku

m0 = Mahasiswa('Mamat', 11, 'Karanganyar', 260000)
m1 = Mahasiswa('Salman', 3, 'Karanganyar', 220000)
m2 = Mahasiswa('Alfarisi', 12, 'Surakarta', 27000)
m3 = Mahasiswa('Ahmad', 41, 'Boyolali', 260000)
m4 = Mahasiswa('Agus', 31, 'Sukoharjo', 240000)
m5 = Mahasiswa('Bagus', 23, 'Klaten', 235000)
m6 = Mahasiswa('Dani', 25, 'Wonogiri', 225000)
m7 = Mahasiswa('Rossi', 33, 'Klaten', 235000)
m8 = Mahasiswa('Pedrosa', 54, 'Karanganyar', 270000)
m9 = Mahasiswa('Ozil', 19, 'Purwodadi', 260000)
m10 = Mahasiswa('Benzema', 52, 'Klaten', 220000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
#1.
def CariIndexKota(kumpulan, k):
   ko = []
   for i in kumpulan :
      if i.kota == k :
         ko.append(kumpulan.index(i))
   return ko
#2.
def UangSakuTerkecil(kumpulan) :
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
    return terkecil
#3.
def DaftarSakuTerkecil(kumpulan) :
    kecil = []
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
            kecil.append(kumpulan.index(i))
    return kecil
#4.
def DaftarSakuKecil(kumpulan):
    kecil = []
    for i in kumpulan :
        if i.uangsaku < 250000 :
            kecil.append(kumpulan.index(i))



class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self): 
        self.head = None
        
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
        
    def pushAk(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    
    def insert(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            prev.next = node
            node.next = current
        return self.head

    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
#5.
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku

m0 = Mahasiswa('Mamat', 11, 'Karanganyar', 260000)
m1 = Mahasiswa('Salman', 3, 'Karanganyar', 220000)
m2 = Mahasiswa('Alfarisi', 12, 'Surakarta', 27000)
m3 = Mahasiswa('Ahmad', 41, 'Boyolali', 260000)
m4 = Mahasiswa('Agus', 31, 'Sukoharjo', 240000)
m5 = Mahasiswa('Bagus', 23, 'Klaten', 235000)
m6 = Mahasiswa('Dani', 25, 'Wonogiri', 225000)
m7 = Mahasiswa('Rossi', 33, 'Klaten', 235000)
m8 = Mahasiswa('Pedrosa', 54, 'Karanganyar', 270000)
m9 = Mahasiswa('Ozil', 19, 'Purwodadi', 260000)
m10 = Mahasiswa('Benzema', 52, 'Klaten', 220000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
def CariIndexKota(kumpulan, k):
   ko = []
   for i in kumpulan :
      if i.kota == k :
         ko.append(kumpulan.index(i))
   return ko

def UangSakuTerkecil(kumpulan) :
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
    return terkecil

def DaftarSakuTerkecil(kumpulan) :
    kecil = []
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
            kecil.append(kumpulan.index(i))
    return kecil

def DaftarSakuKecil(kumpulan):
    kecil = []
    for i in kumpulan :
        if i.uangsaku < 250000 :
            kecil.append(kumpulan.index(i))
    return kecil

#6.
def binary_search(kumpulan, target):
    jml = []
    kiri = 0
    kanan = len(kumpulan) - 1

    while kiri <= kanan :
        mid = (kiri + kanan) // 2
        if kumpulan[mid] == target :
            jml.append(kumpulan.index(target))
            return jml
        elif target < kumpulan[mid]:
            kanan = mid - 1
        else :
            kiri = mid + 1
    return False

d = [1, 2, 3, 3, 4, 5, 5, 5, 5, 133, 134, 157, 157, 189, 200, 230, 235,345]

#7.
class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku

m0 = Mahasiswa('Mamat', 11, 'Karanganyar', 260000)
m1 = Mahasiswa('Salman', 3, 'Karanganyar', 220000)
m2 = Mahasiswa('Alfarisi', 12, 'Surakarta', 27000)
m3 = Mahasiswa('Ahmad', 41, 'Boyolali', 260000)
m4 = Mahasiswa('Agus', 31, 'Sukoharjo', 240000)
m5 = Mahasiswa('Bagus', 23, 'Klaten', 235000)
m6 = Mahasiswa('Dani', 25, 'Wonogiri', 225000)
m7 = Mahasiswa('Rossi', 33, 'Klaten', 235000)
m8 = Mahasiswa('Pedrosa', 54, 'Karanganyar', 270000)
m9 = Mahasiswa('Ozil', 19, 'Purwodadi', 260000)
m10 = Mahasiswa('Benzema', 52, 'Klaten', 220000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]


def CariIndexKota(kumpulan, k):
   ko = []
   for i in kumpulan :
      if i.kota == k :
         ko.append(kumpulan.index(i))
   return ko

def UangSakuTerkecil(kumpulan) :
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
    return terkecil

def DaftarSakuTerkecil(kumpulan) :
    return kecil
#8.
def binery_search(kumpulan, target) :
    kiri = 0
    kanan = len(kumpulan) - 1

    while kiri <= kanan :
        tengah = (kiri + kanan) // 2

        if kumpulan[tengah] == target :
            return tengah

        elif kumpulan[tengah] < target :
            kiri = tengah + 1

        else :
            kanan = tengah - 1

    return -1

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
