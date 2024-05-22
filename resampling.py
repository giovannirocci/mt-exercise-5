# Sub-sample  parallel training data to 100k sentence pairs to make training manageable


import random
import argparse


def subsample(input_source, input_target, output_source, output_target, num_samples=100000):
    with open(input_source, 'r', encoding='utf-8') as f:
        source = f.readlines()
    with open(input_target, 'r', encoding='utf-8') as f:
        target = f.readlines()

    indices = random.sample(range(len(source)), k=num_samples)

    with open(output_source, 'w', encoding='utf-8') as f:
        for i in indices:
            f.write(source[i])
    with open(output_target, 'w', encoding='utf-8') as f:
        for i in indices:
            f.write(target[i])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-is', '--input_source', type=str, help='Path to source language unprocessed file')
    parser.add_argument('-it', '--input_target', type=str, help='Path to target language unprocessed file')
    parser.add_argument('-os', '--output_source', type=str, help='Path to output source language file')
    parser.add_argument('-ot', '--output_target', type=str, help='Path to output target language file')
    parser.add_argument('-n', '--num_samples', type=int, default=100000, help='Number of samples to extract')
    args = parser.parse_args()

    subsample(args.input_source, args.input_target, args.output_source, args.output_target, args.num_samples)


if __name__ == '__main__':
    main()