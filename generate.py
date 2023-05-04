import json
import os
import csv
import time
import tqdm


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
            writer.writerow([dt['input'], dt['target'], out])
            # input(":")
        csv_file.close()


