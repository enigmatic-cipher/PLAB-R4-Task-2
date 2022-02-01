"""
Given a string as input. Create a new string in which every occurrence of digit is replaced by '#' and every capital letter is doubled.
Input-> "Top20"
Output-> TTop##
"""

st = "Top20"
ln = len(st)
nw_st = ""
for i in range(0,ln):
  ch = st[i]
  if(ch>="A" and ch<="Z"):
    nw_st = nw_st + ch + ch
  elif(ch>="0" and ch<="9"):
    nw_st = nw_st + "#"
  else:
    nw_st = nw_st + ch
print(nw_st)
