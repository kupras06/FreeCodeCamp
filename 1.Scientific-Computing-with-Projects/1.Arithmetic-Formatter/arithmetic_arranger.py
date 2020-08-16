def arithmetic_arranger(problems,KEY = False):
  if len(problems) > 5:
      return "Error: Too many problems."
  key = KEY
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  st = ''
  sp = '    '
  for i in problems:
    if not ('+' in i or '-' in i):
      return "Error: Operator must be '+' or '-'."
    p = i.split()
    if not (p[0].isnumeric() and p[2].isnumeric()):
      return "Error: Numbers must only contain digits."
    if len(p[0])>4 or len(p[2])>4:
      return "Error: Numbers cannot be more than four digits."
    l = max(len(p[0]),len(p[2]))
    print(p)
    line1+= ' '*((l-len(p[0]))+2)+p[0]+sp
    line2+= p[1]+' '+' '*((l-len(p[2])))+p[2]+sp
    line3 += '-'*(l+2)+sp
    val = str(eval(i))
    line4+=' '*((l-len(val))+2)+val+sp
  st+=line1.rstrip()+'\n'
  st+=line2.rstrip()+'\n'
  st+=line3.rstrip()
  print(st)
  if key:
    st+='\n'+line4.rstrip()
  #print(st)
  #print(repr(st))
  return st