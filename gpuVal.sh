#!/bin/bash

num=$1
if [ ! -n "$1" ];then
   echo "please input check num like 'sh GPUVolatile.sh 100 '"
else
   echo " you want check $num minutes"
   >gpuVal.txt
   beginT=`date +%s`
   echo $beginT
   while true
   do
      beT=`date +%s`
      echo $beT
      echo $((beT-beginT))
      if [ $((beT-beginT)) -lt $((num*120)) ]
      then
          echo "-------------------------"
          date=`date '+%Y-%m-%d %H:%M:%S'`
          echo $date
          gpuVol=`nvidia-smi|awk -F' '  '{print $13}'| grep -v '^$'`
          echo $gpuVol
          echo $date $gpuVol >> gpuVal.txt
      else
          break
      fi
      sleep 0.5
   done
fi
