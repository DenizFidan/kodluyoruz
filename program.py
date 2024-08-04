points = [(1,2),(2,5),(7,3),(2,3),(12,11),(99,12), (1.1,2.1)]
distances =[]

def euclideanDistance (p1,p2):
  return ((((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))**(1/2))

kni=1
"""karşılaştıtılacak nokta indeksi bunu bir nevi counter gibi kullandım.
Amaç da listedeki ilk noktayı kendisinden sonraki noktalarla karşılaştırsın diye.
İkinci noktaya geçimce kni değeri o an baktığı noktanın indeksine göre 1 artıyor ve
bu sefer 2. noktayı tekrardan 1 ile karşılaştırmıyor çünkü bunu
zaten saha önce yaptık. böylece 1. nokta 2,3,4,5... ile
2. nokta 3,4,5.... ile 3. nokta 4,5,6... diye tüm noktalar birbirleri ile
karşılaştırılıyor
"""

for i in range(len(points)):
  kni=i+1 #karşılaştırılacak nokta indeksi
  while (kni<len(points)):
    x=points[i]
    y=points[kni]
    kni+=1
    distances.append(euclideanDistance(x,y))
    #test print(euclideanDistance (x,y))
    #test print (x,y)

print ("Verilen noktaların arasındaki en kısa mesafe ", (sorted(distances)[0]), " birimdir.")
