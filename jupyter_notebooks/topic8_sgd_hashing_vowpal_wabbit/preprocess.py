from sys import argv
from os.path import isfile,exists
from tqdm import tqdm

tag_to_label = {
	"javascript" : 1,
	"java" : 2,
	"python" : 3,
	"ruby" : 4,
	"php" : 5,
	"c++" : 6,
	"c#" : 7,
	"go" : 8,
	"scala" : 9,
	"swift" : 10
}

if len(argv) < 3:
	print('Not enough arguments')
	exit()

if isfile(argv[1]):
	input_file = argv[1]
else:
	print('Input file doesn\'t exist')
	exit()

if not exists(argv[2]):
	output_file = argv[2]
else:
	print('Output file already exists')
	exit()

lines_selected = 0
lines_corrupted = 0

output = open(output_file, 'w')

for line in tqdm(open(input_file, 'r')):
	line_splitted = line.strip().split('\t')
	if len(line_splitted) == 2:
		line_tags = [tag for tag in line_splitted[1].split() if tag in tag_to_label]
		if len(line_tags) == 1:
			lines_selected = lines_selected + 1
			output.write('%d | %s\n' % (tag_to_label[line_tags[0]], line_splitted[0].replace('|', '').replace(':', '')))
	else:
		lines_corrupted = lines_corrupted + 1
output.close()

print('Lines selected: %d' % lines_selected)
print('Lines corrupted: %d' % lines_corrupted)