#!/bin/bash
scripts=$(dirname "$0")
base=$scripts/..
data=$base/data
configs=$base/configs
src=it-en.it
trg=it-en.en
num_threads=4
device=0
# measure time
SECONDS=0
model_name=transformer_bpe_level_config
mkdir -p $base/beams_results
echo "###############################################################################"
echo "model_name $model_name"
# Read the beam size from the YAML configuration file
beam_size=$(yq '.testing.beam_size' $configs/$model_name.yaml)
CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python3 -m joeynmt translate $configs/$model_name.yaml < $data/test.$src > $base/beams_results/test.$beam_size.$trg
bleu_score=$(cat $base/beams_results/test.$beam_size.$trg | sacrebleu $data/test.$trg)
echo "BLEU score: $bleu_score"
echo "time taken: $SECONDS seconds"
# Append output to results file
output_file=$base/beams_results/results.log
{
  echo "###############################################################################"
  echo "model_name $model_name"
  echo "Beam size: $beam_size"
  echo "BLEU score: $bleu_score"
  echo "time taken: $SECONDS seconds"
  echo ""
} >> $output_file
