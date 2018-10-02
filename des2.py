def function(pt,keyStringArray):
 dec = int(pt, 16); #convert hexadecimal to integer
 left=[]
 right=[]
 pt=bin(dec);    #convert integer to binary
 pt=pt[2:].zfill(64)  # make the decimal to 64 bits
 pt=list(pt) #convert into list
 ip=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
 ip1=[0]*64 #initialize ip1 list with 64 
 j=0
 for i in range(0,len(ip)): #applying initial permutation
  ip1[j]=pt[ip[i]-1]
  j=j+1
 L0=[]
 R0=[]
 for i in range(0,32): #separate left half
  L0.append(ip1[i]) 
 for i in range(32,64): #separate right half
  R0.append(ip1[i]) 
 print()
 ep=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
 for k in range(0,16):
  ep1=[0]*48   #declare 48 bit expanded permutation empty list
  j=0
  for i in range(0,len(ep)):
   ep1[j]=R0[ep[i]-1]    #apply expanded permutation to get 48 bit o/p
   j=j+1
  ep1 = ''.join(ep1)   #converting into string
  y = int(keyStringArray[k], 2)^int(ep1,2)  #xor operation b/w key and ep1
  xor=(bin(y)[2:].zfill(48))  # make it as 48 bit string
  xor=list(xor); #convert it into list
  sBoxes=[]
  sp=[xor[i:i+6] for i in range(0, len(xor), 6)]  #bunch the xor list into 6 bit each
  for i in range(0,8):
   if(i==0):
    m1=sBox1(sp[i],s1) #pass the 6 bit bunch to sbox
    n1='{0:04b}'.format(m1)  # make the output as 4 bit data
    sBoxes.append(n1)
   elif(i==1):
    m1=sBox1(sp[i],s2)
    n1='{0:04b}'.format(m1)  
    sBoxes.append(n1)
   elif(i==2):
    m1=sBox1(sp[i],s3)
    n1='{0:04b}'.format(m1)  
    sBoxes.append(n1)
   elif(i==3):
    m1=sBox1(sp[i],s4)
    n1='{0:04b}'.format(m1)  
    sBoxes.append(n1)
   elif(i==4):
    m1=sBox1(sp[i],s5)
    n1='{0:04b}'.format(m1)  
    sBoxes.append(n1)
   elif(i==5):
    m1=sBox1(sp[i],s6)
    n1='{0:04b}'.format(m1)  
    sBoxes.append(n1)
   elif(i==6):
    m1=sBox1(sp[i],s7)
    n1='{0:04b}'.format(m1)  
    sBoxes.append(n1)
   elif(i==7):
    m1=sBox1(sp[i],s8)
    n1='{0:04b}'.format(m1)  
    sBoxes.append(n1)
  s=''.join(sBoxes) #convert sboxes list to string
  s=list(s) #convert string s to list
  p=[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
  p1=[0]*32 #declare a 32 bit sized list
  j=0
  for i in range(0,len(p)):
   p1[j]=s[p[i]-1]       #pass it through p
   j=j+1
  p1=''.join(p1)
  L0=''.join(L0)
  y1 = int(p1, 2)^int(L0,2)
  xor1=(bin(y1)[2:].zfill(32))
  xor1=list(xor1);
  L0=R0
  R0=xor1 
 c=R0+L0
 c1=''.join(c)
 ipInverse=[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
 ipI=[0]*64
 j=0
 for i in range(0,len(ipInverse)):
  ipI[j]=c[ipInverse[i]-1]
  j=j+1
 ipI=''.join(ipI)
 #print(ipI)
 hCipher=hex(int(ipI, 2))
 return hCipher

def sBox1(l,s):
 t1=[]
 t1.append(l[0])
 t1.append(l[5])
 row = ''.join(t1)
 t2=[]
 t2.append(l[1])
 t2.append(l[2])
 t2.append(l[3])
 t2.append(l[4])
 col = ''.join(t2)
 r=int(row,2)
 c=int(col,2)
 return s[r][c]
s1=[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
s2=[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
s3=[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
s4=[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
s5=[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
s6=[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
s7=[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
s8=[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
pc1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4];
pc11=[0]*56
lsk0=[]
rsk0=[]
print()
print("*************************************KEY GENERATION*****************************************")
print()
key=input("Enter key in hexa decimal format:");
dec = int(key, 16);
key=bin(dec);
key=key[2:].zfill(64)
x1=list(key);
j=0
for i in range(0,len(pc1)):
 pc11[j]=x1[pc1[i]-1]
 j=j+1
for i in range(0,28):
 lsk0.append(pc11[i]) 
for i in range(28,56):
 rsk0.append(pc11[i])
for i in range(1,17):
 if(i==1):
  lsk1=lsk0[1::] + lsk0[:1:]
  rsk1=rsk0[1::] + rsk0[:1:]
 elif(i==2):
  lsk2=lsk1[1::] + lsk1[:1:]
  rsk2=rsk1[1::] + rsk1[:1:]
 elif(i==3):
  lsk3=lsk2[1::] + lsk2[:1:]
  lsk3=lsk3[1::] + lsk3[:1:]
  rsk3=rsk2[1::] + rsk2[:1:]
  rsk3=rsk3[1::] + rsk3[:1:]
 elif(i==4):
  lsk4=lsk3[1::] + lsk3[:1:]
  lsk4=lsk4[1::] + lsk4[:1:]
  rsk4=rsk3[1::] + rsk3[:1:]
  rsk4=rsk4[1::] + rsk4[:1:]
 elif(i==5):
  lsk5=lsk4[1::] + lsk4[:1:]
  lsk5=lsk5[1::] + lsk5[:1:]
  rsk5=rsk4[1::] + rsk4[:1:]
  rsk5=rsk5[1::] + rsk5[:1:]
 elif(i==6):
  lsk6=lsk5[1::] + lsk5[:1:]
  lsk6=lsk6[1::] + lsk6[:1:]
  rsk6=rsk5[1::] + rsk5[:1:]
  rsk6=rsk6[1::] + rsk6[:1:]
 elif(i==7):
  lsk7=lsk6[1::] + lsk6[:1:]
  lsk7=lsk7[1::] + lsk7[:1:]
  rsk7=rsk6[1::] + rsk6[:1:]
  rsk7=rsk7[1::] + rsk7[:1:]
 elif(i==8):
  lsk8=lsk7[1::] + lsk7[:1:]
  lsk8=lsk8[1::] + lsk8[:1:]
  rsk8=rsk7[1::] + rsk7[:1:]
  rsk8=rsk8[1::] + rsk8[:1:]
 elif(i==9):
  lsk9=lsk8[1::] + lsk8[:1:]
  rsk9=rsk8[1::] + rsk8[:1:]
 elif(i==10):
  lsk10=lsk9[1::] + lsk9[:1:]
  lsk10=lsk10[1::] + lsk10[:1:]
  rsk10=rsk9[1::] + rsk9[:1:]
  rsk10=rsk10[1::] + rsk10[:1:]
 elif(i==11):
  lsk11=lsk10[1::] + lsk10[:1:]
  lsk11=lsk11[1::] + lsk11[:1:]
  rsk11=rsk10[1::] + rsk10[:1:]
  rsk11=rsk11[1::] + rsk11[:1:]
 elif(i==12):
  lsk12=lsk11[1::] + lsk11[:1:]
  lsk12=lsk12[1::] + lsk12[:1:]
  rsk12=rsk11[1::] + rsk11[:1:]
  rsk12=rsk12[1::] + rsk12[:1:]
 elif(i==13):
  lsk13=lsk12[1::] + lsk12[:1:]
  lsk13=lsk13[1::] + lsk13[:1:]
  rsk13=rsk12[1::] + rsk12[:1:]
  rsk13=rsk13[1::] + rsk13[:1:]
 elif(i==14):
  lsk14=lsk13[1::] + lsk13[:1:]
  lsk14=lsk14[1::] + lsk14[:1:]
  rsk14=rsk13[1::] + rsk13[:1:]
  rsk14=rsk14[1::] + rsk14[:1:]
 elif(i==15):
  lsk15=lsk14[1::] + lsk14[:1:]
  lsk15=lsk15[1::] + lsk15[:1:]
  rsk15=rsk14[1::] + rsk14[:1:]
  rsk15=rsk15[1::] + rsk15[:1:]
 elif(i==16):
  lsk16=lsk15[1::] + lsk15[:1:]
  rsk16=rsk15[1::] + rsk15[:1:]
pc2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
pca=lsk1+rsk1
key1=[0]*48
key2=[0]*48
key3=[0]*48
key4=[0]*48
key5=[0]*48
key6=[0]*48
key7=[0]*48
key8=[0]*48
key9=[0]*48
key10=[0]*48
key11=[0]*48
key12=[0]*48
key13=[0]*48
key14=[0]*48
key15=[0]*48
key16=[0]*48
j=0
for i in range(0,len(pc2)):
 key1[j]=pca[pc2[i]-1]
 j=j+1
k1 = ''.join(key1)
h1=hex(int(k1, 2))
pca=lsk2+rsk2
j=0
for i in range(0,len(pc2)):
 key2[j]=pca[pc2[i]-1]
 j=j+1
k2 = ''.join(key2)
h2=hex(int(k2, 2))
pca=lsk3+rsk3
j=0
for i in range(0,len(pc2)):
 key3[j]=pca[pc2[i]-1]
 j=j+1
k3 = ''.join(key3)
h3=hex(int(k3, 2))
pca=lsk4+rsk4
j=0
for i in range(0,len(pc2)):
 key4[j]=pca[pc2[i]-1]
 j=j+1
k4 = ''.join(key4)
h4=hex(int(k4, 2))
pca=lsk5+rsk5
j=0
for i in range(0,len(pc2)):
 key5[j]=pca[pc2[i]-1]
 j=j+1
k5 = ''.join(key5)
h5=hex(int(k5, 2))
pca=lsk6+rsk6
j=0
for i in range(0,len(pc2)):
 key6[j]=pca[pc2[i]-1]
 j=j+1
k6 = ''.join(key6)
h6=hex(int(k6, 2))
pca=lsk7+rsk7
j=0
for i in range(0,len(pc2)):
 key7[j]=pca[pc2[i]-1]
 j=j+1
k7 = ''.join(key7)
h7=hex(int(k7, 2))
pca=lsk8+rsk8
j=0
for i in range(0,len(pc2)):
 key8[j]=pca[pc2[i]-1]
 j=j+1
k8 = ''.join(key8)
h8=hex(int(k8, 2))
pca=lsk9+rsk9
j=0
for i in range(0,len(pc2)):
 key9[j]=pca[pc2[i]-1]
 j=j+1
k9 = ''.join(key9)
h9=hex(int(k9, 2))
pca=lsk10+rsk10
j=0
for i in range(0,len(pc2)):
 key10[j]=pca[pc2[i]-1]
 j=j+1
k10 = ''.join(key10)
h10=hex(int(k10, 2))
pca=lsk11+rsk11
j=0
for i in range(0,len(pc2)):
 key11[j]=pca[pc2[i]-1]
 j=j+1
k11 = ''.join(key11)
h11=hex(int(k11, 2))
pca=lsk12+rsk12
j=0
for i in range(0,len(pc2)):
 key12[j]=pca[pc2[i]-1]
 j=j+1
k12 = ''.join(key12)
h12=hex(int(k12, 2))
pca=lsk13+rsk13
j=0
for i in range(0,len(pc2)):
 key13[j]=pca[pc2[i]-1]
 j=j+1
k13 = ''.join(key13)
h13=hex(int(k13, 2))
pca=lsk14+rsk14
j=0
for i in range(0,len(pc2)):
 key14[j]=pca[pc2[i]-1]
 j=j+1
k14 = ''.join(key14)
h14=hex(int(k14, 2))
pca=lsk15+rsk15
j=0
for i in range(0,len(pc2)):
 key15[j]=pca[pc2[i]-1]
 j=j+1
k15 = ''.join(key15)
h15=hex(int(k15, 2))
pca=lsk16+rsk16
j=0
for i in range(0,len(pc2)):
 key16[j]=pca[pc2[i]-1]
 j=j+1
k16 = ''.join(key16)
h16=hex(int(k16, 2))
print("The 16 keys that are generated are:")
print("Key 1:",h1)
print("Key 2:",h2)
print("Key 3:",h3)
print("Key 4:",h4)
print("Key 5:",h5)
print("Key 6:",h6)
print("Key 7:",h7)
print("Key 8:",h8)
print("Key 9:",h9)
print("Key 10:",h10)
print("Key 11:",h11)
print("Key 12:",h12)
print("Key 13:",h13)
print("Key 14",h14)
print("Key 15:",h15)
print("Key 16:",h16)
keyStringArray=[k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16]
print()
print("************************************ENCRYPTION PART*************************************")
print()
pt=input("Enter plain Text in hexadecimal format 16 bit:")
ct=function(pt,keyStringArray)
print("The cipher Text is:",ct)
print()
print("************************************DECRYPTION PART*************************************")
print()
keyStringArray.reverse()
dt=function(ct,keyStringArray)
print("The plainText is",dt)
