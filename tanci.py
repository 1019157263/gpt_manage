import os,random
sw=[[5,5]]
#lc=[[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6]]
lc=[[5,i] for i in range(10)]
s=''
for x in range(500):
  w=len(lc)-1
  li = [(['○'] * 20) for i in range(20)]
  a=input('请输入wasd控制:')
  if a=='':
     a=s
  if a=='w':
      lc.append([lc[w][0]-1,lc[w][1]])
      del lc[0]
      s='w'
  if a=='s':
      lc.append([lc[w][0]+1,lc[w][1]])
      del lc[0]
      s='s'
  if a=='a':
     lc.append([lc[w][0],lc[w][1]-1])
     del lc[0]
     s='a'
  if a=='d':
     lc.append([lc[w][0],lc[w][1]+1])
     del lc[0]
     s='d'
  if lc[w] in sw:
        lc.insert(0,[lc[0][0],lc[0][1]-1])
        del sw[0]
        sw.append([random.randint(0,19),random.randint(0,19)])
  for i in lc:li[i[0]][i[1]]='●'
  for w in sw:li[w[0]][w[1]]='◆'
  os.system('clear')    
  for i in li:print(''.join(i))