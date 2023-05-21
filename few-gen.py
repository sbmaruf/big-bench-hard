import json
import os
import csv
import time
import tqdm
import multiprocessing
import functools
import concurrent

import openai
import json
openai.api_key = "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"


def gen(prompt):
    while True:
        try:
            c = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"{prompt}"},
                ],
            )
            break
        except:
            time.sleep(1)
            continue
    return c['choices'][0]['message']['content']


base_dirs = ["code-davinci-002-outputs/code-davinci-002-cot/", "code-davinci-002-outputs/code-davinci-002-direct/"]
out_dirs = ["few_gen_cot", "few_gen_direct"]

def process_file(base_dir, out_dir, file):
		_file_wo_ex = file.replace(".json", "")
		with open(f"{out_dir}/{_file_wo_ex}.csv", mode='w') as csv_file:
			writer = csv.writer(csv_file)
			if file.endswith("json"):
				file_path = os.path.join(base_dir, file)
				data = json.load(open(file_path))
				outputs = data['outputs']
				for dt in tqdm.tqdm(outputs, total=len(outputs), desc=_file_wo_ex):
					out = gen(dt['input'])
					dt['prediction'] = out
					writer.writerow([dt['input'], dt['prediction'], dt['target']])
			csv_file.close()

def main():

	if not os.path.exists("few_gen_cot"):
		os.makedirs("few_gen_cot", exist_ok=True)
	if not os.path.exists("few_gen_direct"):
		os.makedirs("few_gen_direct", exist_ok=True)

	with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
		futures = []
		for base_dir, out_dir in zip(base_dirs, out_dirs):
				files = os.listdir(base_dir)
				for file in files:
					future = executor.submit(process_file, base_dir, out_dir, file)
					futures.append(future)

		for future in concurrent.futures.as_completed(futures):
			try:
				future.result()
			except Exception as e:
				print(f"Error occurred: {e}")
                        

if __name__ == "__main__":
	main()