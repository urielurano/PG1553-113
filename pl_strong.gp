
set term postscript eps enhanced solid color lw 3.0 font 'Arial-Bold'

#################################################
#################################################
# RESONANCE for Three flavor Neutrino Oscillation
##################################################
#################################################



##########################################################################################
##################################        mu = 0       ###################################
##########################################################################################


set key right bottom 
set title "PG1553+133"
set xlabel "Log {/Symbol n}"
set ylabel "Log {/Symbol n} F_{/Symbol n}"
set format y "%g"
set format x "10^{%L}"

#"10^{%L}" 

set output "xx.eps"
plot "rxtasmavg.dat" u 1:2  title "RXT/ASM" w point, "MAGIC.dat" u 1:2  title "MAGIC" w point, "ebl.dat" u 1:2  title "EBL" w point, "kvaminmax.dat" u 1:2  title "KVA" w point, "lat.dat" u 1:2  title "LAT" w point, "ned.dat" u 1:2  title "NED" w point, "suzaku.dat" u 1:2  title "Suzaku" w point, "swiftbatavg.dat" u 1:2  title "SWIFT/BAT" w point, "swiftuvot.dat" u 1:2  title "SWIFT/UVOT" w point, "swiftxrthi.dat" u 1:2  title "SWIFT/XRT-hi" w point,"swiftxrtmed.dat" u 1:2  title "SWIFT/XRT-med" w point
