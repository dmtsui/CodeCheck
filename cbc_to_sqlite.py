import re
import pickle

cbc = pickle.load(open('cbc.pkl'))

new_cbc = {}

#cbc[CHAPTER]['sections'][TOP_SECTIONS]['sections'][SUB_SECTIONS]  	['name']
									 # ['figures'][SUB_SECTIONS]	['contents']
									 # ['tables'][SUB_SECTIONS]

def conv(input_d, output_d, types):
	for chp in input_d.keys():	
		for top_section in input_d[chp]['sections'].keys():
			for sub_section in input_d[chp]['sections'][top_section][types].keys():
				print("cbc["+chp+"]['sections']["+top_section+"]["+types+"]["+sub_section+"]")				
				output_d[sub_section] = {'chapter':{'name':input_d[chp]['name'],
													'number':chp},
										 'section':{'name': input_d[chp]['sections'][top_section]['name'],
										 			'number':unicode(top_section)},
										 'content': input_d[chp]['sections'][top_section][types][sub_section]['content'],
										 'name': input_d[chp]['sections'][top_section][types][sub_section]['name'],
										 'number': input_d[chp]['sections'][top_section][types][sub_section],
										 'type':types[:-1]}	


conv(cbc,new_cbc,'sections')
conv(cbc,new_cbc,"figures")
conv(cbc,new_cbc,"tables")	


output = open('cbc_sql.pkl','w')
pickle.dump(new_cbc,output)
output.close()								