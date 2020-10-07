__author__ = 'Emre'


vize1 = input('Matematik Vize Notunuz : ')
final1 = input('Matematik Final Notunuz : ')
quiz1 = input('Matematik Quiz notunuz: ')
mat_harfnotu_kat_sayisi = 0.0
ortalama1=(float(vize1)*0.3)+(float(final1)*0.5)+(float(quiz1)*0.2)
print("Matematik Ortalama :{0} ".format(ortalama1))


if(ortalama1<45):
      mat_harfnotu_kat_sayisi = 0.0
      print("FF")
elif(ortalama1<50):
      mat_harfnotu_kat_sayisi = 0.0
      print("FD")
elif(ortalama1<55):
      mat_harfnotu_kat_sayisi = 1.0
      print("DD")
elif(ortalama1<60):
      mat_harfnotu_kat_sayisi = 1.5
      print("DC")
elif(ortalama1<70):
      mat_harfnotu_kat_sayisi = 2.0
      print("CC")
elif(ortalama1<80):
      mat_harfnotu_kat_sayisi = 2.5
      print("CB")
elif(ortalama1<85):
      mat_harfnotu_kat_sayisi = 3.0
      print("BB")
elif(ortalama1<90):
      mat_harfnotu_kat_sayisi = 3.5
      print("BA")
else:
      mat_harfnotu_kat_sayisi = 4.0
      print("AA")

vize2 = input('Fizik Vize Notunuz : ')
final2 = input('Fizik Final Notunuz : ')
quiz2 = input('Fizik Quiz notunuz: ')
fiz_harfnotu_kat_sayisi = 0.0
ortalama2=(float(vize2)*0.3)+(float(final2)*0.5)+(float(quiz2)*0.2)
print("Fizik Ortalama :{0} ".format(ortalama2))


if(ortalama2<45):
      fiz_harfnotu_kat_sayisi = 0.0
      print("FF")
elif(ortalama2<50):
      fiz_harfnotu_kat_sayisi = 0.0
      print("FD")
elif(ortalama2<55):
      fiz_harfnotu_kat_sayisi = 1.0
      print("DD")
elif(ortalama2<60):
      fiz_harfnotu_kat_sayisi = 1.5
      print("DC")
elif(ortalama2<70):
      fiz_harfnotu_kat_sayisi = 2.0
      print("CC")
elif(ortalama2<80):
      fiz_harfnotu_kat_sayisi = 2.5
      print("CB")
elif(ortalama2<85):
      fiz_harfnotu_kat_sayisi = 3.0
      print("BB")
elif(ortalama2<90):
      fiz_harfnotu_kat_sayisi = 3.5
      print("BA")
else:
      fiz_harfnotu_kat_sayisi = 4.0
      print("AA")

vize3 = input('Kimya Vize Notunuz : ')
final3 = input('Kimya Final Notunuz : ')
quiz3 = input('Kimya Quiz notunuz: ')
kim_harfnotu_kat_sayisi = 0.0
ortalama3=(float(vize3)*0.3)+(float(final3)*0.5)+(float(quiz3)*0.2)
print("Kimya Ortalama :{0} ".format(ortalama3))


if(ortalama3<45):
      kim_harfnotu_kat_sayisi = 0.0
      print("FF")
elif(ortalama3<50):
      kim_harfnotu_kat_sayisi = 0.0
      print("FD")
elif(ortalama3<55):
      kim_harfnotu_kat_sayisi = 1.0
      print("DD")
elif(ortalama3<60):
      kim_harfnotu_kat_sayisi = 1.5
      print("DC")
elif(ortalama3<70):
      kim_harfnotu_kat_sayisi = 2.0
      print("CC")
elif(ortalama3<80):
      kim_harfnotu_kat_sayisi = 2.5
      print("CB")
elif(ortalama3<85):
      kim_harfnotu_kat_sayisi = 3.0
      print("BB")
elif(ortalama3<90):
      kim_harfnotu_kat_sayisi = 3.5
      print("BA")
else:
      kim_harfnotu_kat_sayisi = 4.0
      print("AA")


vize4 = input('Edebiyat Vize Notunuz : ')
final4 = input('Edebiyat Final Notunuz : ')
quiz4 = input('Edebiyat Quiz notunuz: ')
edeb_harnotu_kat_sayisi = 0.0
ortalama4=(float(vize4)*0.3)+(float(final4)*0.5)+(float(quiz4)*0.2)
print("Edebiyat Ortalama :{0} ".format(ortalama4))


if(ortalama4<45):
      edeb_harnotu_kat_sayisi = 0.0
      print("FF")
elif(ortalama4<50):
      edeb_harnotu_kat_sayisi = 0.0
      print("FD")
elif(ortalama4<55):
      edeb_harnotu_kat_sayisi = 1.0
      print("DD")
elif(ortalama4<60):
      edeb_harnotu_kat_sayisi = 1.5
      print("DC")
elif(ortalama4<70):
      edeb_harnotu_kat_sayisi = 2.0
      print("CC")
elif(ortalama4<80):
      edeb_harnotu_kat_sayisi = 2.5
      print("CB")
elif(ortalama4<85):
      edeb_harnotu_kat_sayisi = 3.0
      print("BB")
elif(ortalama4<90):
      edeb_harnotu_kat_sayisi = 3.5
      print("BA")
else:
      edeb_harnotu_kat_sayisi = 4.0
      print("AA")

mat_kredi = 5
kimya_kredi = 4
fizik_kredi = 4
edeb_kredi = 3


mat_puan = mat_kredi * mat_harfnotu_kat_sayisi
fizik_puan = fizik_kredi * fiz_harfnotu_kat_sayisi
kimya_puan = kimya_kredi * kim_harfnotu_kat_sayisi
edeb_puan = edeb_kredi * edeb_harnotu_kat_sayisi

toplam_puan = (mat_puan + fizik_puan + kimya_puan + edeb_puan) / (mat_kredi + kimya_kredi + fizik_kredi + edeb_kredi)

print("DONEM NOT ORTALAMASI : {0}".format(toplam_puan))