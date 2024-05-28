# MT Exercise 5: Byte Pair Encoding, Beam Search
This repository is a starting point for the 5th and final exercise. As before, fork this repo to your own account and the clone it into your prefered directory.

## Student names & IDs

- Name: **Giovanni Rocci**
- Matriculation number: **22-729-156**

- Name: **Siro Rosenau**
- Matriculation number: **22-711-840**

## Requirements

- This only works on a Unix-like system, with bash available.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

## Steps

Clone your fork of this repository in the desired place:

    git clone https://github.com/[your-name]/mt-exercise-5

Create a new virtualenv that uses Python 3.10. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software as described in the exercise pdf.

Download data:

    ./download_iwslt_2017_data.sh
    
Before executing any further steps, you need to make the modifications described in the exercise pdf.

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Evaluate a trained model with

    ./scripts/evaluate.sh


## Changes made

- Created a shell script to download joeyNMT hotfix
- For each model trained we wrote a 'config' file
- We created `resampling.py` to randomly sample 100k senteces from training data
- We saved the sampled sentences into `train.100k.it-en.it` and `train.100k.it-en.en`
- We followed the steps in "Best practice" from the GitHub repository: https://github.com/rsennrich/subword-nmt#best-practice-advice-for-byte-pair-encoding-in-nmt to get `codes.bpe` and the two single language vocabs
- We created `vocab_merge.py` to build a single vocabulary for both languages (of the specified size) and create a `merged_vocab.txt` file
- We created `beam_evaluate.sh` to output the translations with different beam size, evaluate their BLEU score and save the results in the `results.log` file
- We created `plot_beam_results.py` to plot the BLEU score and the time taken for each different beam size

### General Changes

Because of Ubuntu we had to delete empty lines and use `python3` instead of `python` in the shell scripts to be able to run them.