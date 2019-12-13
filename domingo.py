import datetime

class Calendario:

    def domingo(fi, ff):
        lista = []

        delta = datetime.timedelta(days=1)
        s = datetime.datetime.strptime(fi, '%d-%m-%Y').date()
        f = datetime.datetime.strptime(ff, '%d-%m-%Y').date()
        
        for i in range(((f+delta) - s).days):
            lista2=[]
            r = s + i * delta #calculo de fechas que estan dentro del rango
            pmes = r.year, r.month, r.day #separo cada fecha por elementos
            lista2.append(pmes) #agrego a la lista
            
            if r.weekday() == 6 and lista2[0][2]==1: #condicion donde el mes empiece por domingo
                lista.append(r) #agrego a la lista
           

        return print(len(lista))
        

    
fi = '01-01-1901'
ff = '31-12-2000'
f = Calendario.domingo(fi, ff)

