import re
import matplotlib.pyplot as plt

# Load the log file
file_path = 'beams_results/results.log'

with open(file_path, 'r') as file:
    content = file.readlines()

# Initialize lists to hold the beam sizes, BLEU scores, and times
beam_sizes = []
bleu_scores = []
times = []

# Regular expressions to capture the required data
beam_size_re = re.compile(r'Beam size: (\d+)')
bleu_score_re = re.compile(r'"score": (\d+\.\d+)')
time_taken_re = re.compile(r'time taken: ([\d.]+) seconds', re.IGNORECASE)

current_beam_size = None

# Parse the log file
for line in content:
    beam_size_match = beam_size_re.search(line)
    bleu_score_match = bleu_score_re.search(line)
    time_taken_match = time_taken_re.search(line)

    if beam_size_match:
        current_beam_size = int(beam_size_match.group(1))
    elif bleu_score_match and current_beam_size is not None:
        bleu_score = float(bleu_score_match.group(1))
        beam_sizes.append(current_beam_size)
        bleu_scores.append(bleu_score)
    elif time_taken_match and current_beam_size is not None:
        time_taken = float(time_taken_match.group(1))
        times.append(time_taken)


# Plotting BLEU scores vs Beam sizes
plt.figure(figsize=(10, 6))
plt.plot(beam_sizes, bleu_scores, marker='o', linestyle='-', color='b')
plt.xlabel('Beam Size')
plt.ylabel('BLEU Score')
plt.title('BLEU Score vs Beam Size')
plt.grid(True)
plt.xticks(range(min(beam_sizes), max(beam_sizes) + 1))
plt.savefig('bleu_score_vs_beam_size.png')

# Plotting Time taken vs Beam sizes
plt.figure(figsize=(10, 6))
plt.plot(beam_sizes, times, marker='o', linestyle='-', color='r')
plt.xlabel('Beam Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken vs Beam Size')
plt.grid(True)
plt.xticks(range(min(beam_sizes), max(beam_sizes) + 1))
plt.savefig('time_taken_vs_beam_size.png')
