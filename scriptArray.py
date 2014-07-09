
def makeArray(filesArray):

    x1,y1,xizq,xder,yarr,yaba=[],[],[],[],[],[]

    for x in range(0,len(filesArray)):
        try:
            pathFile = filesArray[x]
            rfile = open(pathFile, 'r')
            if rfile:
                print rfile
                for line in rfile:
                    a, b, c, d, e, f = [float(t) for t in line.split()]
                    x1.append(a)
                    y1.append(b)
                    xizq.append(c)
                    xder.append(d)
                    yarr.append(e)
                    yaba.append(f)
                

            final_array = open('puntos_experimentos.dat','w')

            for elem in range(0,len(x1)):
                final_array.write(str(x1[elem])+'\t')
                final_array.write(str(y1[elem])+'\t')
                final_array.write(str(xizq[elem])+'\t')
                final_array.write(str(xder[elem])+'\t')
                final_array.write(str(yarr[elem])+'\t')
                final_array.write(str(yaba[elem])+'\t')
                final_array.write('\n')
            final_array.close()
        except:
            print "Revisa la ruta de tus archivos"
	    raise

listaDeArchivos = [ 'MAGIC.dat', 'ebl.dat', 'kvaminmax.dat', 'lat.dat', 'ned.dat', 'rxtasmavg.dat', 'suzaku.dat', 'swiftbatavg.dat', 'swiftuvot.dat', 'swiftxrthi.dat', 'swiftxrtmed.dat' ]

makeArray(listaDeArchivos)

