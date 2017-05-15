from tqdm import tqdm

lines = []
count = 1

for line in tqdm(open('../../../../datasets/stackoverflow/stackoverflow.vw', 'r')):
	if count in [1, 2, 1463019, 1463020, 2926037, 2926038]:
		lines.append(line)
	count = count + 1
for l in lines[0:2]:
	print(l)
print('==================================================================================')
for l in lines[2:4]:
	print(l)
print('==================================================================================')
for l in lines[4:6]:
	print(l)