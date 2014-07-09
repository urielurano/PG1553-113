{
 gROOT->Reset();

 c1=new TCanvas ("c1", "",20,1,640,480);
 TMultiGraph *mg = new TMultiGraph();
 mg->SetTitle(";E(eV); E^{2}dN/dE (MeV cm^{-2} s^{-1})");
 c1->SetFillColor(10);
 c1->GetFrame()->SetFillColor(25);
 c1->GetFrame()->SetBorderSize(20);



 Int_t n2=14;//FERMI
 Int_t i;
 //The last four data points were taken from the "butterfly boxes".
 Float_t w2[n2]={
 
 10**(22.5484948111684-14.25),
 10**(23.2629292108290-14.25),
 10**(23.8820864757876-14.25),
 10**(24.6387748603941-14.25),
 10**(25.3777409572680-14.25),
 10**(25.7760491836338-14.25),
 10**(25.8199809758528-14.25),
 10**(25.9091618141659-14.25),
 10**(26.0463832923272-14.25),
 10**(26.1631918263924-14.25),
 10**(26.2912245934499-14.25),
 10**(26.4205694873217-14.25),
 10**(26.5780374033048-14.25),
 10**(26.8035217862359-14.25)
 };//x

 Float_t v2[n2]={
 10**(-10.82664518880743),
 10**(-10.73443464350436),
 10**(-10.55236293586296),
 10**(-10.56526501706040),
 10**(-10.73443464350436),
 10**(-10.92304810077968),
 10**(-11.24735746757389),
 10**(-11.62920007760944),
 10**(-11.44865994045433),
 10**(-11.80486367150232),
 10**(-12.39856113488181),
 10**(-12.82228177578978),
 10**(-13.16035130985058),
 10**(-12.20802854939893)
	 };

 Float_t ewl2[n2]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
                                              
 Float_t evl2[n2]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
                                              
 Float_t ewh2[n2]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
                                              
 Float_t evh2[n2]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
gr2=new TGraphAsymmErrors(n2,w2,v2,ewl2,ewh2,evl2,evh2);
 gr2->SetMarkerColor(1);
 gr2->SetMarkerStyle(4);
 gr2->SetMarkerSize(0.7);  
 gr2->SetLineColor(0); 
 gr2->SetLineStyle(1); 
 gPad->SetLogy();  
 gPad->SetLogx();





  //Int_t n4=3;//Magic
  //Int_t i;
  //Float_t w4[n4]={1e11, 1.9e11, 3.8e11};//x
  //Float_t v4[n4]={3.8e-6,6.8e-7,3.7e-7};//y
  //Float_t ewl4[n4]={0,0,0};
  //Float_t evl4[n4]={1.0e-6,4.8e-7,3.1e-7};
  //Float_t ewh4[n4]={0,0,0};
  //Float_t evh4[n4]={1.8e-6,4.8e-7,3.1e-7};
  //gr4=new TGraphAsymmErrors(n4,w4,v4,ewl4,ewh4,evl4,evh4);
  //gr4->SetMarkerColor();
  //gr4->SetMarkerStyle(8);
  //gr4->SetMarkerSize(0.7);
  //gr4->SetLineColor(1);
  //gPad->SetLogy();
  //gPad->SetLogx();



 Int_t n20=2;//end
 Int_t i;
 Float_t w20[n20]={9.484e14,1.796e13};
 Float_t v20[n20]={1.435e-9,1.996e-9};
 Float_t ewl20[n20]={0,0};
 Float_t evl20[n20]={0,0};
 Float_t ewh20[n20]={0,0};
 Float_t evh20[n20]={0,0};
 gr20=new TGraphAsymmErrors(n20,w20,v20,ewl20,ewh20,evl20,evh20);
 gr20->SetMarkerColor();
 gr20->SetMarkerStyle(8);
 gr20->SetMarkerSize(0.0001);  
 gr20->SetLineColor(3);
 gPad->SetLogy();  
 gPad->SetLogx();
 gr20->SetFillColor(2); 

 Int_t n21=2;//beginning
 Int_t i;
 Float_t w21[n21]={2.484e-9,5.796e-9};
 Float_t v21[n21]={1.435e-9,1.996e-9};
 Float_t ewl21[n21]={0,0};
 Float_t evl21[n21]={0,0};
 Float_t ewh21[n21]={0,0};
 Float_t evh21[n21]={0,0};
 gr21=new TGraphAsymmErrors(n21,w21,v21,ewl21,ewh21,evl21,evh21);
 gr21->SetMarkerColor();
 gr21->SetMarkerStyle(8);
 gr21->SetMarkerSize(0.0001);  
 gr21->SetLineColor(3);
 gPad->SetLogy();  
 gPad->SetLogx();
 gr21->SetFillColor(2); 






 mg->Add(gr2);
 mg->Add(gr20);
 mg->Add(gr21);
 
 mg->Draw("apz");




//############################Fit formulas###############
//################
//##############################################################
//

 fun4 = new TF1("fun4","[0]*((x/[1])^(4/3)*(x>1e3)*(x<[1])+((x/[1])**((3-[3])/2)*(x>=[1])*(x<[2])) + (([2]/[1])**((3-[3])/2))*((x/[2])**((2-[3])/2))*(x>=[2])*(x<3e14) )",1e+3,3e+10); //pgamma interaction
 // Se fija el valor inicial de las energías de normalización:
  fun4->SetParameter(0,6.32041e-07);
  //fun4->SetParLimits(0,1e+5,1e+7);
  fun4->SetParameter(1,1e+7);
  fun4->SetParLimits(1,1e+2,1e+9);
  fun4->SetParameter(2,5e+11);
  fun4->SetParLimits(2,1e+5,1e+13);
  fun4->SetParameter(3,2.5);
  fun4->SetParLimits(3,2.5,2.5);
 
//#################fit commands############
//####################################
//###############
//
//
//

 fun4->SetLineWidth(2);
 gr2->Fit("fun4","APL+"); 
 //gr4->Fit("fun3","APL+"); 
 }


