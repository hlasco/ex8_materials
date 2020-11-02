#!/bin/bash

path='..'  # 'path/to/simdirectory'
if [ "$#" -ne 0 ]; then
  echo "Usage: ./process_rt.sh"
else
  for i in 0000{1..9} 000{10..14} #00{100..153} # change last number according to number of outputs you have
    do
      eval "./amr2map -inp ${path}/output_$i -typ 1 -out ${path}/dens_$i.map" # converts hydro outputs Fortran binary density maps
      echo "Processing snapshot $i"
      eval "python ./rt_dens_map.py -i $i -d $path" # converts density maps to png images
    done
  eval "convert -quality 100  ${path}/*.png ${path}/movie.mpeg" # converts pngs to movie, requires ffmpeg
  eval "chmod a+r ${path}/movie.mpeg"
fi
