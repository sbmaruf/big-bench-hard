import os
import json
import tqdm
import csv

files = sorted(os.listdir("./bbh/"))
cnt = 0
for _file in files:
	if _file == "README.md" or _file == "notebook.ipynb" or _file == ".ipynb_checkpoints" or _file == "csv":
		continue
	with open(f"gen/{_file}.csv", mode='w') as csv_file:
		writer = csv.writer(csv_file)
		data = json.load(open(os.path.join("./bbh", _file)))
		for dt in tqdm.tqdm(data['examples'], total = len(data['examples'])):
			out = gen(dt['input'])
			out = out.strip()
			out = out.replace("\n", " ")
			writer.writerow([dt['input'], dt['target'], out])
		csv_file.close()