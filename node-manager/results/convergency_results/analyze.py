import os

current_directory = os.path.dirname(os.path.abspath(__file__))

with open(f'{current_directory}/n=2.txt', 'r') as f:
	total_lsu_size = 0
	for line in f:
		if 'lsu size' in line:
			total_lsu_size += int(line.split(':')[-1])
	print(total_lsu_size)