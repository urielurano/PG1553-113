from array import array
import os
import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt
from sys import *
from pylab import *
from math import *
from matplotlib.path import Path
import matplotlib.patches as patches


rt.gROOT.Reset()

rt.gStyle.SetFillColor(0)
rt.gStyle.SetPadLeftMargin(.20)
rt.gStyle.SetPadBottomMargin(.20)
rt.gStyle.SetCanvasColor(10)
rt.gStyle.SetFrameFillColor(0);
rt.gStyle.SetCanvasBorderMode(0);

rt.gStyle.SetOptFit(111111)
mg = rt.TMultiGraph()

saves = {}
NP = 0
NP1 = 0
canvas = -1


########################################################################################
##############            Fisrt Module                  ################################
########################################################################################

def sync(As,alpha, Em_s, Ec_s):

    '''Make a dat file with the fitted points '''

    outspec = open("syn.dat","w")
    Acs=As
    alp=alpha
    Ems=Em_s
    Ecs=Ec_s
    for ii in arange(-6.0, 6, 1.5):
        
        Ega0=pow(10,ii)
        Egamma=Ega0
        C1=0
        C2=0
        C3=0
        C4=0
        if(Egamma < Ems):
            C1=Acs*pow(Egamma/Ems,4.0/3.0)
        if(Ems <= Egamma and  Egamma < Ecs ):
            C2=Acs*pow(Egamma/Ems,-(alp-3.0)/2.0)
        if(5e4>Egamma >=Ecs):
            C3=Acs*pow(Ecs/Ems,-(alp-3.0)/2)*pow(Egamma/Ecs,-(alp-2.0)/2.0)
        #if(Egamma>4e1):
            #C4= Acs*pow(Ecs/Ems,-(alp-3.0)/2)*pow(Egamma/Ecs,-(alp-2.0)/2.0)
            #Ega0=4e1
            
        C=C1+C2+C3+C4

        outspec.write("%E %E\n" %(Ega0,C))
    outspec.close()


def comp(Ac,alpha,Em_c,Ec_c):

    '''Make a dat file with the fitted points '''

    outspec = open("comp.dat","w")
    Acc=Ac
    alp=alpha
    Emc=Em_c
    Ecc=Ec_c
    for ii in arange(3, 13, 2.7):
        Ega0=pow(10,ii)
        Egamma=Ega0
        C1=0
        C2=0
        C3=0
        C4=0
        if(Egamma < Emc):
            C1=Acc*pow(Egamma/Emc,4.0/3.0)
        if(Emc <= Egamma and  Egamma < Ecc ):
            C2=Acc*pow(Egamma/Emc,-(alp-3.0)/2.0)
        if(1e11 > Egamma >=Ecc):
            C3=Acc*pow(Ecc/Emc,-(alp-3.0)/2)*pow(Egamma/Ecc,-(alp-2.0)/2.0)
        if(Egamma > 0.15e11):
            C4=Acc*pow(Ecc/Emc,-(alp-3.0)/2)*pow(Egamma/Ecc,-(alp-2.0)/2.0)*exp(-Egamma/0.9e12)
            Ega0 = 0.15e11+0.23*Egamma

        C=C1+C2+C3+C4

        outspec.write("%E %E\n" %(Ega0,C))

    outspec.close()

def comp_pgamma(param1, param2):

    '''Make a dat file with the fitted points '''

    outspec = open("comp_pgamma.dat","w")
    Apg=param1
    alpg=param2
    Epg=1e11
    E_min = 0.06e12
    Epg0 = 0.1e12
    E_max = 1e12
    for ii in arange(10.9, 13, 0.05):
        Ega0=pow(10,ii)
        Egamma=Ega0
        C1=0
        C2=0
        C3=0
        if(Egamma < Epg):
            C1=Apg*pow(Epg/Epg0,-1.0)*pow(Egamma/Epg0,3.0-alpg)
        if(Egamma >= Epg and Egamma < E_max):
            C2=Apg*pow(Egamma/Epg0,2.0-alpg)
        if(Egamma >= E_max):
            C3=Apg*pow(Egamma/Epg0,0.5-alpg)

        C=C1+C2+C3

        outspec.write("%E %E\n" %(Ega0,C))

    outspec.close()



##########################################################################################
####################### Second Module of the program #####################################
##########################################################################################

def make_SplinePlot():

    ''' Make the spline of the plot '''


    try:

            X,Y, X_izq, X_der, Y_arr, Y_aba = loadtxt('swiftbatavg1.dat', unpack = True)
            X1,Y1, X1_izq, X1_der, Y1_arr, Y1_aba = loadtxt('rxtasmavg1.dat', unpack = True)
            X2,Y2, X2_izq, X2_der, Y2_arr, Y2_aba = loadtxt('kvaminmax1.dat', unpack = True)
            X3,Y3, X3_izq, X3_der, Y3_arr, Y3_aba = loadtxt('ebl1.dat', unpack = True)
            X4,Y4, X4_izq, X4_der, Y4_arr, Y4_aba = loadtxt('lat1.dat', unpack = True)
            X5,Y5, X5_izq, X5_der, Y5_arr, Y5_aba = loadtxt('MAGIC1.dat', unpack = True)
            X6,Y6, X6_izq, X6_der, Y6_arr, Y6_aba = loadtxt('ned1.dat', unpack = True)
            X7,Y7, X7_izq, X7_der, Y7_arr, Y7_aba = loadtxt('suzaku1.dat', unpack = True)
            X8,Y8, X8_izq, X8_der, Y8_arr, Y8_aba = loadtxt('swiftuvot1.dat', unpack = True)
            X9,Y9, X9_izq, X9_der, Y9_arr, Y9_aba = loadtxt('swiftxrthi1.dat', unpack = True)
            X10,Y10, X10_izq, X10_der, Y10_arr, Y10_aba = loadtxt('swiftxrtmed1.dat', unpack = True)

            
            XS, YS = loadtxt('syn.dat', unpack = True)
            XC, YC = loadtxt('comp.dat', unpack = True)
            XG, YG = loadtxt('comp_pgamma.dat', unpack = True)
            
            verts = []
            codes = [Path.MOVETO]
            for elem in range(0, len(XS)):
                verts.append((XS[elem], YS[elem]*2))
            for elem in range(0,(len(XS)-1)):
                codes.append(Path.CURVE4)
                
            path = Path(verts, codes)

            vertsC = []
            codesC = [Path.MOVETO]
            for elem in range(0, len(XC)):
                vertsC.append((XC[elem], YC[elem]*3))
            for elem in range(0, (len(XC)-1)):
                codesC.append(Path.CURVE4)

            pathC = Path(vertsC, codesC)

            vertsG = []
            codesG = [Path.MOVETO]
            for elem in range(0, len(XG)):
                vertsG.append((XG[elem], YG[elem]*2.7))
            for elem in range(0, (len(XG)-1)):
                codesG.append(Path.CURVE4)

            pathG = Path(vertsG, codesG)


            fig = plt.figure()
            ax = fig.add_subplot(111)
            patchS = patches.PathPatch(path, facecolor='none', lw=2)
            patchC = patches.PathPatch(pathC, facecolor='none', lw=2)
            patchG = patches.PathPatch(pathG, facecolor='none', lw=2)
            ax.add_patch(patchS)
            ax.add_patch(patchC)
            ax.add_patch(patchG)

                        
            ax.errorbar(X,Y, Y_arr, Y_aba, linestyle="none", marker="o", color="green", markersize=4.0, capsize=3.0, label = '1')
            ax.errorbar(X1,Y1, Y1_arr, Y1_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '2')
            ax.errorbar(X2,Y2, Y2_arr, Y2_aba, linestyle="none", marker="o", color="red", markersize=4.0, capsize=3.0, label = '3')
            ax.errorbar(X3,Y3, Y3_arr, Y3_aba, linestyle="none", marker="o", color="yellow", markersize=4.0, capsize=3.0, label = '4')
            ax.errorbar(X4,Y4, Y4_arr, Y4_aba, linestyle="none", marker="o", color="black", markersize=4.0, capsize=3.0, label = '5')
            ax.errorbar(X5,Y5, Y5_arr, Y5_aba, linestyle="none", marker="o", color="orange", markersize=4.0, capsize=3.0, label = '6')
            ax.errorbar(X6,Y6, Y6_arr, Y6_aba, linestyle="none", marker="x", color="blue", markersize=4.0, capsize=3.0, label = '2')
            ax.errorbar(X7,Y7, Y7_arr, Y7_aba, linestyle="none", marker="x", color="red", markersize=4.0, capsize=3.0, label = '3')
            ax.errorbar(X8,Y8, Y8_arr, Y8_aba, linestyle="none", marker="x", color="yellow", markersize=4.0, capsize=3.0, label = '4')
            ax.errorbar(X9,Y9, Y9_arr, Y9_aba, linestyle="none", marker="x", color="black", markersize=4.0, capsize=3.0, label = '5')
            ax.errorbar(X10,Y10, Y10_arr, Y10_aba, linestyle="none", marker="x", color="orange", markersize=4.0, capsize=3.0, label = '6')
            
            
            a=plt.gca()
            a.set_yscale('log')
            a.set_xscale('log')
            plt.ylabel(r'epsilon', size=12)
            #plt.xlim(1e-6,1e14)
            #plt.ylim(1e-9,1e-3)
            plt.show()
            
    except:
        raise
    


##########################################################################################
######################## Third Module of the program #####################################
##########################################################################################


def makeFit(files):

    '''Read the .dat files to make the fit of the points'''
    
    global saves
    global NP1

    try:
        x1 = []
        y1 = []
        xizq = []
        xder = []
        yarr = []
        yaba = []
        mt = []
        separados = []
        
        path = '/home/uluviano/PG1553-113/'
        #path = '/home/antonio/pks0447-439/'

        i = 0;
        while(i < len(files)):
            pathFile = path + files[i]
            rfile = open(pathFile, 'r')
            if rfile:
                for line in rfile:
                    a, b, c, d, e, f = [float(t) for t in line.split()]
                    x1.append(a)
                    y1.append(b)
                    xizq.append(c)
                    xder.append(d)
                    yarr.append(e)
                    yaba.append(f)
            i = i+1
        ##Now we make the arrays of the points
        X = np.array(x1, float)
        Y = np.array(y1, float)
        Xizq = np.array(xizq, float)
        Xder = np.array(xder, float)
        Yarr = np.array(yarr, float)
        Yaba = np.array(yaba, float)
        
        ##Make the plots from root
        
        graph = rt.TGraphErrors(len(x1), X, Y, Xizq, Yarr)
        graph.SetMarkerSize(0.7)
        graph.SetMarkerStyle(4)
        graph.SetMarkerColor(4)
        
        mg.Add(graph)
        mg.Draw('APE')                                                                                                 
        saves['graph'] = graph
        rt.gPad.SetLogx()
        rt.gPad.SetLogy()
        rt.gPad.Update()

        mg.GetXaxis().SetTitle('Energy (eV)')
        mg.GetYaxis().SetTitle('vFv (erg cm^{-2} s^{-1})')

#########################################################
######################FIT SYNCHROTRON####################
#########################################################

        fun4 = rt.TF1("fun4"," [0]*((x/[2])^(4/3)*(x>1e-6)*(x<[2])+((x/[2])**((3-[1])/2)*(x>=[2])*(x<[3])) + (([3]/[2])**((3-[1])/2))*((x/[3])**((2-[1])/2))*(x>=[3])*(x<2e4))",  1e-6,2e4)
        rt.fun4.SetParameter(1,2.5);
        rt.fun4.SetParLimits(1,2.5,3.5);
        rt.fun4.SetParameter(2,1e-4);
        rt.fun4.SetParLimits(2,1e-5,1e-3);
        rt.fun4.SetParameter(3,1);
        rt.fun4.SetParLimits(3,1e-1,5);
        rt.fun4.SetParameter(4,100);
        
        graph.Fit('fun4',"Q")                                                                                                                                                                  
        rt.fun4.Draw('L same') 

        a_s = rt.fun4.GetParameter(0)
        alfa = rt.fun4.GetParameter(1)
        em_s = rt.fun4.GetParameter(2)
        ec_s = rt.fun4.GetParameter(3)
        
        print a_s, alfa, em_s, ec_s, "\n"

#########################################################
######################FIT INVERSE COMPTON################
#########################################################

        fun2 = rt.TF1("fun2"," [0]*((x/[1])^(4/3)*(x>1e4)*(x<[1])+((x/[1])**((3-[3])/2)*(x>=[1])*(x<[2])) + (([2]/[1])**((3-[3])/2))*((x/[2])**((2-[3])/2))*(x>=[2])*(x<3e11) )",1e+4,3e+11)
        rt.fun2.SetParameter(0,6.32041e-05)
        rt.fun2.SetParLimits(0,1e-18,1e-3)
        rt.fun2.SetParameter(1,1e+6)
        rt.fun2.SetParLimits(1,1e+3,1e+7)
        rt.fun2.SetParameter(2,5e+10)
        rt.fun2.SetParLimits(2,1e+9,1e+11)
        rt.fun2.SetParameter(3, alfa)
        rt.fun2.SetParLimits(3,alfa, alfa)
        
        rt.fun2.SetLineColor(2)
        rt.fun2.SetLineWidth(2)
        graph.Fit('fun2',"Q")
        rt.fun2.Draw('L same')

        a_c = rt.fun2.GetParameter(0)
        em_c = rt.fun2.GetParameter(1)
        ec_c = rt.fun2.GetParameter(2)


        print a_c, alfa, em_c, ec_c, "\n"

#########################################################
######################FIT P-GAMMA########################
#########################################################

        fun3 =  rt.TF1("fun3"," [0]*((0.1e12/0.1e12)^(-1)*(x/0.1e12)**(3-[1])*(x>=0.06e12)*(x<0.1e12)+((x/0.1e12)**(2-[1])*(x>=0.1e12)*(x<5e13)))",1E11,7E14) #Interaction pgamma
        rt.fun3.SetParameter(0,3.696e-6)
        rt.fun3.SetParameter(1,4.245)
        graph.Fit('fun3',"Q")
        rt.fun3.Draw('L same')

	alfa_pg = rt.fun3.GetParameter(0)
        a_pg = rt.fun3.GetParameter(1)

        print alfa_pg, a_pg

	sync(a_s, alfa, em_s, ec_s)
	comp(a_c, alfa, em_c, ec_c)
        comp_pgamma(alfa_pg, a_pg)

        
    except:
        raise
        print 'Check the param of the code'
        

def _showMathPlotlib():
    ''' Make the plot on matplotlib  '''

    X,Y, X_izq, X_der, Y_arr, Y_aba = loadtxt('swiftbatavg1.dat', unpack = True)
    X1,Y1, X1_izq, X1_der, Y1_arr, Y1_aba = loadtxt('rxtasmavg1.dat', unpack = True)
    X2,Y2, X2_izq, X2_der, Y2_arr, Y2_aba = loadtxt('kvaminmax1.dat', unpack = True)
    X3,Y3, X3_izq, X3_der, Y3_arr, Y3_aba = loadtxt('ebl1.dat', unpack = True)
    X4,Y4, X4_izq, X4_der, Y4_arr, Y4_aba = loadtxt('lat1.dat', unpack = True)
    X5,Y5, X5_izq, X5_der, Y5_arr, Y5_aba = loadtxt('MAGIC1.dat', unpack = True)
    X6,Y6, X6_izq, X6_der, Y6_arr, Y6_aba = loadtxt('ned1.dat', unpack = True)
    X7,Y7, X7_izq, X7_der, Y7_arr, Y7_aba = loadtxt('suzaku1.dat', unpack = True)
    X8,Y8, X8_izq, X8_der, Y8_arr, Y8_aba = loadtxt('swiftuvot1.dat', unpack = True)
    X9,Y9, X9_izq, X9_der, Y9_arr, Y9_aba = loadtxt('swiftxrthi1.dat', unpack = True)
    X10,Y10, X10_izq, X10_der, Y10_arr, Y10_aba = loadtxt('swiftxrtmed1.dat', unpack = True)






    XS, YS = loadtxt('syn.dat', unpack = True)
    XC, YC = loadtxt('comp.dat', unpack = True)
    XG, YG = loadtxt('comp_pgamma.dat', unpack = True)
    

    plt.figure('Experiments')
    
    plt.errorbar(X,Y, Y_arr, Y_aba, linestyle="none", marker="o", color="green", markersize=4.0, capsize=3.0, label = '1')
    plt.errorbar(X1,Y1, Y1_arr, Y1_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '2')
    plt.errorbar(X2,Y2, Y2_arr, Y2_aba, linestyle="none", marker="o", color="red", markersize=4.0, capsize=3.0, label = '3')
    plt.errorbar(X3,Y3, Y3_arr, Y3_aba, linestyle="none", marker="o", color="yellow", markersize=4.0, capsize=3.0, label = '4')
    plt.errorbar(X4,Y4, Y4_arr, Y4_aba, linestyle="none", marker="o", color="black", markersize=4.0, capsize=3.0, label = '5')
    plt.errorbar(X5,Y5, Y5_arr, Y5_aba, linestyle="none", marker="o", color="orange", markersize=4.0, capsize=3.0, label = '6')
    plt.errorbar(X6,Y6, Y6_arr, Y6_aba, linestyle="none", marker="x", color="blue", markersize=4.0, capsize=3.0, label = '2')
    plt.errorbar(X7,Y7, Y7_arr, Y7_aba, linestyle="none", marker="x", color="red", markersize=4.0, capsize=3.0, label = '3')
    plt.errorbar(X8,Y8, Y8_arr, Y8_aba, linestyle="none", marker="x", color="yellow", markersize=4.0, capsize=3.0, label = '4')
    plt.errorbar(X9,Y9, Y9_arr, Y9_aba, linestyle="none", marker="x", color="black", markersize=4.0, capsize=3.0, label = '5')
    plt.errorbar(X10,Y10, Y10_arr, Y10_aba, linestyle="none", marker="x", color="orange", markersize=4.0, capsize=3.0, label = '6')
    plt.plot(XS,YS)
    plt.plot(XC,YC, color = 'blue')
    plt.plot(XG,YG, color = 'red')

    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    #plt.xlim(1e-6,1e14)
    #plt.ylim(1e-9,1e-3)
    plt.show()








files = [ 'swiftbatavg1.dat', 'rxtasmavg1.dat', 'kvaminmax1.dat', 'ebl1.dat', 'lat1.dat', 'MAGIC1.dat', 'ned1.dat', 'suzaku1.dat', 'swiftuvot1.dat', 'swiftxrthi1.dat', 'swiftxrtmed1.dat' ]

makeFit(files)
_showMathPlotlib()
make_SplinePlot()


###DataFiles######
#swiftbatavg1.dat
#rxtasmavg1.dat
#kvaminmax1.dat
#ebl1.dat
#lat1.dat
#MAGIC1.dat
#ned1.dat
#suzaku1.dat
#swiftuvot1.dat
#swiftxrthi1.dat
#swiftxrtmed1.dat
#################
