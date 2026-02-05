#!/usr/bin/bash

input_file="$1"
sed -i 's/\r$//' "$input_file"

#for file in *.fasta
#do sed -i 's/\r$//' "$file"
#done

#for file in *.txt
#do sed -i 's/\r$//' "$file"
#done

