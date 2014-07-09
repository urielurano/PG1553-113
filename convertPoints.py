######################################################
######################################################
#### In this program we can get the points of the ####
#### plot and make the chage of basis to get the  ####
#### points and make the fit.                     ####
######################################################
######################################################

def convert_points(filesArray):

 x1,y1,xizq,xder,yarr,yaba=[],[],[],[],[],[]
 name = ''

    #walk along the array of file paths
    for x in range(0,len(filesArray)):
        try:
            #We now try to
            pathFile = filesArray[x]
            name = pathFile
            rfile = open(pathFile, 'r')
            if rfile:
                for line in rfile:
                    a, b, c, d, e, f = [float(t) for t in line.split()]
                    x1.append(pow(10,a))
                    y1.append(pow(10,b))
                    xizq.append(pow(10,a)-pow(10,c))
                    xder.append(pow(10,d)-pow(10,a))
                    yarr.append(pow(10,e)-pow(10,b))
                    yaba.append(pow(10,b)-pow(10,f))
                

            final_array = open(name+'_base_modif.dat','w')

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
