def MergeSort(table):
  a,b=0,0
  if len(table) > 1:
    half = len(table)//2
    a,b=MergeSort(table[:half]),MergeSort(table[half:])
  else:
    return table
  out = []
  while len(a)>0 and len(b)>0:
    if a[0] > b[0]:
      out.append(b[0])
      del b[0]
    else:
      out.append(a[0])
      del a[0]
  return out + a + b


s=[]
with open("WordLists/words.txt","r") as file:
  s=MergeSort(file.readlines())

with open("WordLists/wordsSorted.txt","w") as file:
  file.writelines(s)