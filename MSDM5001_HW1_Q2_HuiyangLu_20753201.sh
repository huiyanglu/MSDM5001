#!/bin/sh

for i in $(seq 1 100)
do
  echo "make directory ddm$i"
  mkdir ddm$i
  cd ddm$i

  timer_end="1970-01-01 00:00:00"
  start_n=`date +%s%N`
  end_n=`date +%s%N -d "${timer_end}"`
  # echo $start_n
  # echo $end_n

  x1=$(( $start_n - $end_n ))
  x2=$(($x1))
  echo $x2
  echo "nanoseconds since 1970-01-01 00:00:00 UTC: 
< $x2 nanoseconds >" >>time_till_now.txt
  cd /home/parallels/Desktop

done
