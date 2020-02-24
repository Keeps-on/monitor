#!/bin/bash

# 查看CPU使用率
function cpu(){
	util=$(vmstat |awk '{if(NR==3)print $13+$14}')
	iowait=$(vmstat |awk '{if(NR==3)print $16}')
	echo "CPU-使用率: ${util}%,等待磁盘IO响应使用率:${iowait}%"
}

cpu
