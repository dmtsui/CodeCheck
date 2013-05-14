import pickle
import json

part1 = pickle.load(open('part1.pkl'))
part2 = pickle.load(open('part2.pkl'))

part1.update(part2)

output = open('cbc.pkl','w')
pickle.dump(part1,output)
output.close()	

cbc = json.dumps(part1)

out = open('cbc.json','w')
out.write(cbc)