#!/bin/bash

export LC_ALL=C;

sort -t',' -k1 -k2 -k3 $*;