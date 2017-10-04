#!/bin/bash

# Parse cmd line args.
while getopts ":k:i:o:v:" opt; do
  case $opt in
    k)
      k=$OPTARG
      ;;
    i)
      i=$OPTARG
      ;;
    o)
      o=$OPTARG
      ;;
    v)
      v=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

if [ -z $k ]
  then
    echo 'key file not specified'
    exit 1
fi
if [ -z $i ]
  then
    echo 'input file not specified'
    exit 1
fi
if [ -z $o ]
  then
    echo 'output file not specified'
    exit 1
fi

python3.6 src/cbc.py e $i $o $k $v