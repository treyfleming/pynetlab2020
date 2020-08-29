from pprint import pprint
import textfsm

#Load the TextFSM Template
template_file = "2_show_int_status.tpl"
template = open(template_file)

#Load the raw data file
with open("2_show_int_status.txt", 'r') as f:
    raw_text_data = f.read()

#Parse the raw data through the TextFSM template
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

#Convert the TextFSM parsed data from nested lists to list of dicts
table_keys = re_table.header
final_list = []
for fsm_list in data:
    fsm_dict = dict(zip(table_keys, fsm_list))
    final_list.append(fsm_dict)

print()
pprint(final_list)
print()
