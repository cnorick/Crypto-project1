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

echo $k $i $v $o

