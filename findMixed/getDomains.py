import re
f = open('top10k', 'r')
to_write  = ''
for line in f.readlines():
  #print 'check line', line
  regex = r'.*'
  #match = re.match(regex, line)
  match = re.search(r'.*,(.*)', line)
  if match:
    #print 'groups', match.group(1)
    to_write = to_write + match.group(1) + '\n'

f.close()
f = open('top10k.out', 'w')
f.write(to_write)
f.close()
