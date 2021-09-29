import math as go
class transposition:
  def makematrix(self,list_key,text):
    matrix_len = int(go.ceil(len(text)/len(list_key)))
    add_s = int((len(list_key)*matrix_len)-len(text))
    text.extend("$"*add_s)
    col = len(list_key)
    bef_mat = [text[i:i+col] for i in range(0,len(text),col)]
    return bef_mat
  def encryption(self,list_key,text,bef_mat):
    sort_key = list_key[:]
    sort_key.sort()
    encrypt = ""
    for i in sort_key:
      fetch = list_key.index(i)
      for j in range(len(bef_mat)):
        fetchword = bef_mat[j][fetch]
        encrypt += fetchword
    return encrypt
key = input("enter key :")
list_key = list(dict.fromkeys(key))
text = list(input("enter the text :").replace(" ",""))
cl_tc = transposition()
bef_mat = cl_tc.makematrix(list_key,text)
print(cl_tc.encryption(list_key,text,bef_mat))
