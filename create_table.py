# $$
# \begin{array}{|c|c|c|c|c|c|c|c|c|c|c|}
# \hline \multirow[b]{2}{*}{\text { BIG-Bench Hard Task }} & \multicolumn{2}{|c|}{\text { Srivastava et al. (2022) }} & \multicolumn{2}{|c|}{\text { Human-Rater }} & \multicolumn{2}{|c|}{\text { InstructGPT }} & \multicolumn{2}{|c|}{\text { Codex }} & \multicolumn{2}{|c|}{\text { PaLM 540B }} \\
# \hline & \text { Random } & \text { SOTA } & \text { Avg. } & \text { Max } & \mathrm{AO} & \text { CoT } & \mathrm{AO} & \mathrm{CoT} & \mathrm{AO} & \text { CoT } \\
# \hline \text { Boolean Expressions }^\lambda & 50.0 & 68.5 & 79.4 & 100 & 90.0 & 87.6 & 88.4 & 92.8 & 83.2 & 80.0 \\
# \hline \text { Causal Judgement } & 50.0 & 62.1 & 69.6 & 100 & 57.8 & 56.1 & 63.6 & 54.0 & 61.0 & 59.4 \\
# \hline \text { Date Understanding } & 17.2 & 75.1 & 76.8 & 100 & 55.6 & 81.6 & 63.6 & 87.2 & 53.6 & 79.2 \\
# \hline \text { Disambiguation QA } & 33.2 & 51.6 & 66.6 & 93.3 & 66.4 & 70.8 & 67.2 & 76.0 & 60.8 & 67.6 \\
# \hline \text { Dyck Languages }{ }^\lambda & 1.2 & 28.5 & 47.8 & 100 & 42.0 & 32.0 & 46.8 & 56.8 & 28.4 & 28.0 \\
# \hline \text { Formal Fallacies } & 25.0 & 52.2 & 90.8 & 100 & 52.4 & 58.4 & 52.4 & 50.4 & 53.6 & 51.2 \\
# \hline \text { Geometric Shapes }^\lambda & 11.6 & 36.5 & 54.0 & 100 & 35.2 & 56.0 & 32.0 & 54.4 & 37.6 & 43.6 \\
# \hline \text { Hyperbaton } & 50.0 & 67.1 & 74.7 & 100 & 67.2 & 72.4 & 60.4 & 66.4 & 70.8 & 90.4 \\
# \hline \text { Logical Deduction }^\lambda(a v g) & 22.5 & 36.5 & 40.3 & 88.9 & 34.5 & 58.9 & 37.1 & 60.4 & 42.7 & 56.9 \\
# \hline \text { Movie Recommendation } & 25.0 & 52.2 & 60.7 & 90.0 & 72.0 & 78.8 & 84.8 & 90.4 & 87.2 & 92.0 \\
# \hline \text { Multi-Step Arithmetic }{ }^\lambda \text { [Two] } & 0 & 5.7 & 9.7 & 25.0 & 1.2 & 53.2 & 1.2 & 47.6 & 1.6 & 19.6 \\
# \hline \text { Navigate }^\lambda & 50.0 & 56.0 & 81.9 & 100 & 68.0 & 88.8 & 50.4 & 96.4 & 62.4 & 79.6 \\
# \hline \text { Object Counting }^\lambda & 0 & 42.6 & 86.1 & 100 & 44.0 & 77.2 & 45.2 & 93.2 & 51.2 & 83.2 \\
# \hline \text { Penguins in a Table } & 0 & 53.0 & 78.0 & 100 & 47.3 & 81.5 & 66.4 & 79.5 & 44.5 & 65.1 \\
# \hline \text { Reasoning about Colored Objects } & 11.9 & 69.3 & 75.4 & 100 & 47.6 & 78.4 & 67.6 & 91.6 & 38.0 & 74.4 \\
# \hline \text { Ruin Names } & 25.0 & 72.8 & 77.7 & 100 & 65.6 & 62.8 & 75.2 & 68.4 & 76.0 & 61.6 \\
# \hline \text { Salient Translation Error Detection } & 16.7 & 31.9 & 36.7 & 80.0 & 61.6 & 62.4 & 62.0 & 60.8 & 48.8 & 54.0 \\
# \hline \text { Snarks } & 50.0 & 71.3 & 76.7 & 100 & 65.2 & 60.7 & 61.2 & 59.6 & 78.1 & 61.8 \\
# \hline \text { Sports Understanding } & 50.0 & 68.1 & 70.8 & 100 & 71.6 & 92.0 & 72.8 & 97.6 & 80.4 & \text { 98.0 } \\
# \hline \text { Temporal Sequences }{ }^\lambda & 25.0 & 52.2 & 90.8 & 100 & 33.6 & 67.2 & 77.6 & 96.8 & 39.6 & 78.8 \\
# \hline \text { Tracking Shuffled Objects }{ }^\lambda \text { (avg) } & 22.5 & 24.1 & 64.7 & 100 & 25.1 & 61.1 & 24.1 & 84.5 & 19.6 & 52.9 \\
# \hline \text { Web of } \operatorname{Lies}^\lambda & 50.0 & 59.6 & 81.3 & 100 & 51.6 & 92.0 & 51.6 & 95.2 & 51.2 & 100 \\
# \hline \text { Word Sorting }{ }^\lambda & 0 & 33.1 & 62.6 & 100 & 36.8 & 44.4 & 50.4 & 40.4 & 32.0 & 21.6 \\
# \hline \text { NLP Task (avg) } & 29.5 & 60.5 & 71.2 & 96.9 & 60.9 & 71.3 & 66.4 & 73.5 & 62.7 & 71.2 \\
# \hline \text { Algorithmic } \operatorname{Task}^\lambda \text { (avg) } & 21.2 & 40.3 & 63.5 & 92.2 & 42.0 & 65.3 & 45.9 & \mathbf{7 4 . 4} & 40.9 & 58.6 \\
# \hline \text { All Tasks }(a v g) & 25.7 & 52.1 & 67.7 & 94.4 & 51.8 & 68.4 & 56.6 & \text { 73.9 } & 52.3 & 63.3 \\
# \hline
# \end{array}
# $$

import json

result_zero_shot = {
"big_bench_sports_understanding.json":		71.2,
"big_bench_boolean_expressions.json":		75.6,
"big_bench_formal_fallacies.json":		54,
"big_bench_causal_judgement.json":		60.97,
"big_bench_ruin_names.json":		57.2,
"big_bench_salient_translation_error_detection.json":		42.4,
"big_bench_disambiguation_qa.json":		59.6,
"big_bench_snarks.json":		82,
"big_bench_hyperbaton.json":		77.2,
"big_bench_geometric_shapes.json":		20,
"big_bench_movie_recommendation.json":		65.6,
"big_bench_navigate.json":		41.6,
"big_bench_penguins_in_a_table":		70.5,
"big_bench_reasoning_about_colored_objects.json":		60.8,
"big_bench_object_counting.json":		54.8,
"big_bench_temporal_sequences.json":		61.6,
"big_bench_multi-step arithmetic.json":		52.8,
"big_bench_date_understanding":71.2,
"big_bench_dyck_languages.json":		31.6,
"big_bench_word_sorting.json":75.2,
"big_bench_web_of_lies.json":		32.4,
"big_bench_tracking_shuffled_objects.json":		34.4,
"big_bench_logical_deduction.json":		44.1,
}



result = {
"big_bench_boolean_expressions.json":[	75.6,	88.8,	96],
"big_bench_hyperbaton.json":[	77.2,	70, 	80.8],
"big_bench_sports_understanding.json":[	71.2,	87.6,	94.4],
"big_bench_formal_fallacies.json":[	54,	52.8,	55.2],
"big_bench_causal_judgement.json":[	60.97,	64.1,	61.5],
"big_bench_ruin_names.json":[	57.2,	70,	51,.2],
"big_bench_salient_translation_error_detection.json":[	42.4,	45.2,	52.8],
"big_bench_disambiguation_qa.json":[	59.6,	64.4,	68.4],
"big_bench_snarks.json":[	82,	61.2,	57.8],
"big_bench_geometric_shapes.json":[	20,	42.4,	52.8],
"big_bench_movie_recommendation.json":[	65.6,	74.8,	79.6],
"big_bench_navigate.json":[	41.6,	63.2,	94],
"big_bench_penguins_in_a_table.json":[	70.5,	43.8,	74.7],
"big_bench_reasoning_about_colored_objects.json":[	60.8,	57.2,	86.4],
"big_bench_object_counting.json":[	54.8,	46.4,	96.8],
"big_bench_temporal_sequences.json":[	61.6,	26,	59,.2],
"big_bench_multi-step arithmetic.json":[	48.8,	2.8,	64],
"big_bench_date_understanding.json":[	71.2,	48.4,	79.2],
"big_bench_dyck_languages.json":[	31.6,	6,	23,.2],
"big_bench_web_of_lies.json":[	32.4,	0.4,	98.4],
"big_bench_word_sorting.json":[	75.2,	68.8,	55.6],
"big_bench_tracking_shuffled_objects.json":[	34.4,	22.9,	59.7],
"big_bench_logical_deduction.json":[	44.1,	40.7,	63.5],
}

res_list = sorted([ (k.replace("big_bench_", "").replace(".json", "").replace("_", " "), v) for k, v in result.items()])
print(res_list)

table = {
	'BIG-Bench Hard Task': [
		'{Boolean Expressions}$^{\lambda}$', 
		'Causal Judgement', 
		'Date Understanding', 
		'Disambiguation QA', 
		'{Dyck Languages}$^{\lambda}$', 
		'Formal Fallacies', 
		'{Geometric Shapes}$^{\lambda}$', 
		'Hyperbaton', 
		'{Logical Deduction}$^{\lambda}$ (avg)', 
		'Movie Recommendation', 
		'{Multi-Step Arithmetic}$^{\lambda}$  [Two]', 
		'Navigate$^{\lambda}$', 
		'{Object Counting}$^{\lambda}$', 
		'Penguins in a Table', 
		'Reasoning about Colored Objects', 
		'Ruin Names', 
		'Salient Translation Error Detection', 
		'Snarks', 'Sports Understanding', 
		'{Temporal Sequences}$^{\lambda}$', 
		'{Tracking Shuffled Objects}$^{\lambda}$ (avg)', 
		'{Web of Lies}$^{\lambda}$', 
		'{Word Sorting}$^{\lambda}$', 
		'NLP Task (avg)', 
		'{Algorithmic Task}$^{\lambda}$ (avg)', 
		'All Tasks (avg)'],
	'Srivastava et al. random': ['50.0', '50.0', '17.2', '33.2', '1.2', '25.0', '11.6', '50.0', '22.5', '25.0', '0', '50.0', '0', '0', '11.9', '25.0', '16.7', '50.0', '50.0', '25.0', '22.5', '50.0', '0', '29.5', '21.2', '25.7'],
	'Srivastava et al. SOTA': ['68.5', '62.1', '75.1', '51.6', '28.5', '52.2', '36.5', '67.1', '36.5', '52.2', '5.7', '56.0', '42.6', '53.0', '69.3', '72.8', '31.9', '71.3', '68.1', '52.2', '24.1', '59.6', '33.1', '60.5', '40.3', '52.1'],
	'Human-Rater Avg.': ['79.4', '69.6', '76.8', '66.6', '47.8', '90.8', '54.0', '74.7', '40.3', '60.7', '9.7', '81.9', '86.1', '78.0', '75.4', '77.7', '36.7', '76.7', '70.8', '90.8', '64.7', '81.3', '62.6', '71.2', '63.5', '67.7'],
	'Human-Rater Max': ['100', '100', '100', '93.3', '100', '100', '100', '100', '88.9', '90.0', '25.0', '100', '100', '100', '100', '100', '80.0', '100', '100', '100', '100', '100', '100', '96.9', '92.2', '94.4'],
	'InstructGPT AO': ['90.0', '57.8', '55.6', '66.4', '42.0', '52.4', '35.2', '67.2', '34.5', '72.0', '1.2', '68.0', '44.0', '47.3', '47.6', '65.6', '61.6', '65.2', '71.6', '33.6', '25.1', '51.6', '36.8', '60.9', '42.0', '51.8'],
	'InstructGPT CoT': ['87.6', '56.1', '81.6', '70.8', '32.0', '58.4', '56.0', '72.4', '58.9', '78.8', '53.2', '88.8', '77.2', '81.5', '78.4', '62.8', '62.4', '60.7', '92.0', '67.2', '61.1', '92.0', '44.4', '71.3', '65.3', '68.4'],
	'Codex AO': ['88.4', '63.6', '63.6', '67.2', '46.8', '52.4', '32.0', '60.4', '37.1', '84.8', '1.2', '50.4', '45.2', '66.4', '67.6', '75.2', '62.0', '61.2', '72.8', '77.6', '24.1', '51.6', '50.4', '66.4', '45.9', '56.6'],
	'Codex CoT': ['92.8', '54.0', '87.2', '76.0', '56.8', '50.4', '54.4', '66.4', '60.4', '90.4', '47.6', '96.4', '93.2', '79.5', '91.6', '68.4', '60.8', '59.6', '97.6', '96.8', '84.5', '95.2', '40.4', '73.5', '74.4', '73.9'],
	'PaLM 540B AO': ['83.2', '61.0', '53.6', '60.8', '28.4', '53.6', '37.6', '70.8', '42.7', '87.2', '1.6', '62.4', '51.2', '44.5', '38.0', '76.0', '48.8', '78.1', '80.4', '39.6', '19.6', '51.2', '32.0', '62.7', '40.9', '52.3'],
	'PaLM 540B CoT': ['80.0', '59.4', '79.2', '67.6', '28.0', '51.2', '43.6', '90.4', '56.9', '92.0', '19.6', '79.6', '83.2', '65.1', '74.4', '61.6', '54.0', '61.8', '98.0', '78.8', '52.9', '100', '21.6', '71.2', '58.6', '63.3']
}

merge_vars = [
	"logical deduction",
	"tracking shuffled objects",
]
Algo_task = [
	"Boolean Expressions", 
	"Dyck Languages", 
	"Geometric Shapes", 
	"Logical Deduction", 
	"Multi-Step Arithmetic", 
	"Navigate",
	"Object Counting",
	"Temporal Sequences", 
	"Tracking Shuffled Objects", 
	"Web of Lies", 
	"Word Sorting"
]

Algo_task = [task.lower() for task in Algo_task]

task_rows = [[], [], []]
tot, tot_cnt, algo_tot, nlp_tot, nlp_tot_cnt = [0,0,0], [0,0,0], [0,0,0], [0,0,0] , [0,0,0]
nlp_task_sum, alg_task_sum = {}, {}
for big_bench_task_name, (task, res) in zip(table['BIG-Bench Hard Task'], res_list):
	assert task in big_bench_task_name.lower(), f"{task} {big_bench_task_name.lower()}"
	for id in range(3):
		if task in big_bench_task_name.lower():
			task_rows[id].append(res[id])
			tot[id] += res[id]
			tot_cnt[id] += 1
		
	big_bench_task_name = big_bench_task_name.lower().replace("[two]", "").replace("$", "").replace("{\lambda}", "").replace("}", "").replace("{", "").replace("^", "").replace("(avg)", "").lower().strip()
	# print("ALGO", big_bench_task_name)
	if big_bench_task_name in Algo_task:
		# print("\tALGO", big_bench_task_name)
		for id in range(3):
			algo_tot[id]+= res[id]
	else:
		for id in range(3):
			nlp_tot[id] += res[id]
			nlp_tot_cnt[id] += 1

table['ZS'] = task_rows[0]
table['ZS'].append(round(algo_tot[0]/len(Algo_task),1))
table['ZS'].append(round(nlp_tot[0]/nlp_tot_cnt[0],1))
table['ZS'].append(round(tot[0]/tot_cnt[0],1))

table['FS-AO'] = task_rows[1]
table['FS-AO'].append(round(algo_tot[1]/len(Algo_task),1))
table['FS-AO'].append(round(nlp_tot[1]/nlp_tot_cnt[1],1))
table['FS-AO'].append(round(tot[1]/tot_cnt[1], 1))

table['FS-CoT'] = task_rows[2]
table['FS-CoT'].append(round(algo_tot[2]/len(Algo_task),1))
table['FS-CoT'].append(round(nlp_tot[2]/nlp_tot_cnt[2],1))
table['FS-CoT'].append(round(tot[2]/tot_cnt[2],1))


# for k, v in table.items():
# 	print(len(v))


def print_latex_table(data):
	header = list(data.keys())
	num_rows = len(data[header[0]])

	print("\\begin{table*}")
	print("    \\centering")
	print("    \\resizebox{\\textwidth}{!}{%")
	print("    \\begin{tabular}{lccccccccccccc}")
	print("        \\toprule")
	print("        Task & \\multicolumn{2}{c}{\\citet{srivastava2022imitation}} & \\multicolumn{2}{c}{Human-Rater} & \\multicolumn{2}{c}{InstructGPT} & \\multicolumn{2}{c}{Codex} & \\multicolumn{2}{c}{PaLM 540B} & \\multicolumn{3}{c}{ChatGPT}\\\\")
	print("        \cmidrule(lr){2-3}  \cmidrule(lr){4-5}  \cmidrule(lr){6-7} \cmidrule(lr){8-9} \cmidrule(lr){10-11} \cmidrule(lr){12-14}")
	print("         & Random & SOTA & Avg. & Max & AO & CoT & AO & CoT & AO & CoT &  ZS & FS-AO & FS-CoT\\\\")
	print("        \midrule")
	for i in range(num_rows):
		row = [data[col][i] for col in header]
		if row[0] == "NLP Task (avg)":
			print("\\midrule")
		print("        {} \\\\".format(" & ".join([str(r) for r in row])))
	
	print(" \\bottomrule")
	print("    \\end{tabular}")
	print("    }")
	print("\\end{table*}")
	


print_latex_table(table)