#!/bin/bash
CONFIG="xmcgan/configs/coco_xmc.py"
EXP_NAME=$1
WORKDIR="/home1/pindikan/CSCI566-Project/code_base/experiments/$EXP_NAME"  # CHANGEME

CUDA_VISIBLE_DEVICES="0" python -m xmcgan.main \
  --config="$CONFIG" \
  --mode="generate" \
  --workdir="$WORKDIR" \
