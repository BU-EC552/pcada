import json
import re
from dna_features_viewer import GraphicFeature, GraphicRecord, CircularGraphicRecord
import Bio
from Bio.Seq import Seq
import sys

filename = sys.argv[1]

with open(filename) as f:
    data = json.load(f)

sol = data['solutions']
frag = sol[0]['fragments']
seq = Seq(data['seq'])

#lists to store inputs for dna_features_viewer
start_list = []
end_list = []
strand_list =[]
label_list=[]
color_list = ["#DFFF00", "#6495ED", "#FFBF00", "#40E0D0", "#FF7F50", "#9FE2BF", "#DE3163", "#CCCCFF", "#800080", "#008080", "#00FF00", "#00FFFF", "#000080"]

for i in range(len(frag)):
    fragment = frag[i]
    substring = Seq(fragment['seq'])
    start_list.append(seq.find(substring[:40]))
    end_index = seq.find(substring[:40])+len(substring)
    if end_index < len(seq):
        end_list.append(end_index)
    else:
        end_list.append(end_index-len(seq))
    strand_list.append("+1")
    description = "type: " + fragment['type']+", cost: " + str(fragment['cost'])
    if fragment['type'] == "pcr":
        description += ", url: "
        description += fragment['url']
    label_list.append(description)

for i in range(len(start_list)):
    if start_list[i] > end_list[i]:
        start_list[i] = start_list[i] - len(seq)

features1 = [GraphicFeature(start = start_list[i], end = end_list[i], strand = +1, color = color_list[i], label = label_list[i]) for i in range(len(frag))]

record = CircularGraphicRecord(sequence_length = len(seq), features = features1)

record.plot(figure_width=10)
ax, _ = record.plot(figure_width=5)
ax.figure.savefig(filename + "_vis.png", bbox_inches="tight")
