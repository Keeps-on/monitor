#!/bin/bash

# 编写内存使用情况,获取当前内存的总大小,以使用,剩余

function memory(){

    total=$(free -m |awk '{if(NR==2)printf "%.1f",$2/1024}')
    used=$(free -m |awk '{if(NR==2)printf "%.1f",($2-$NF)/1024}')
    available=$(free -m |awk '{if(NR==2)printf "%.1f",$NF/1024}')
    echo "内存-总大小:${total}G,已使用:${used}G,剩余:${available}G"

}

memory

