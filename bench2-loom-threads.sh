#!/bin/bash

source build.sh

echo -e "$GREEN ...RUN LOOM Server... $RESET"
run_loom loom/Bench2Threads.java "8888 $1"