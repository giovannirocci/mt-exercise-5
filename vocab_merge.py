# Script to open 2 vocabulary files, take the 2000 most frequent words and remove counts
# Then merge the two files and write the result to a new file

import argparse


def main():
    parser = argparse.ArgumentParser(description='Merge two vocab files')
    parser.add_argument('-v1', '--vocab1', type=str, help='Path to first vocab file')
    parser.add_argument('-v2', '--vocab2', type=str, help='Path to second vocab file')
    parser.add_argument('-o', '--output', type=str, help='Path to output file')
    parser.add_argument('-n', '--num_words', type=int, default=2000, help='Number of words that the resulting voc '
                                                                          'will have')
    args = parser.parse_args()

    def read_vocab(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.rstrip() for line in f if len(line.split()) > 1]

    vocab1 = read_vocab(args.vocab1)
    vocab2 = read_vocab(args.vocab2)

    counts = {}
    for word in vocab1 + vocab2:
        if word.split()[0] in counts:
            counts[word.split()[0]] += int(word.split()[1])
        else:
            counts[word.split()[0]] = int(word.split()[1])

    vocab = sorted(counts, key=counts.get, reverse=True)

    with open(args.output, 'w', encoding='utf-8') as f:
        for word in vocab[:args.num_words]:
            f.write(word.split()[0] + '\n')  # Write only the word, without the count


if __name__ == '__main__':
    main()
