class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku
        
#1.
def bubleshort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range (passnum):
            if val[i]>val[i+1]:
                temp = val[1]
                val[i] = val [i+1]
                val [i+1] = temp

#2.
A = [1,2,3,4,5]
B = [6,7,9,10]
C = []


def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

C.extend(A)
C.extend(B)
print (C)

#3.
from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[q]= A[q]
    A[q]= tmp
    
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil   

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print('insertion:%g detik' %(ak-aw));

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

Daftar = [m0.nim, m1.nim, m2.nim, m3.nim, m4.nim, m5.nim, m6.nim, m7.nim, m8.nim, m9.nim, m10.nim]
bubleshort(Daftar)
print(Daftar)
