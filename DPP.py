import numpy as np
def fixed_point_map(feature,subset):
        dim=len(feature[1])
        number=len(feature[:,1])
        feature=feature.reshape(number,dim)
        eta=.25
        W = np.random.randint(1000,size=(dim,dim))
#         W=np.random.rand(dim,dim)
        Z = np.array([[0]*number]*number).astype(float)
        I = np.array([[0]*number]*number)
        for i in range(number):
            for j in range(number):
                if(i==j):
                    I[i][j]=1
                            
        subsetf=[]
        for i in subset:
            a=[]
            if(i[0]!=i[1]):
                for j in range(i[0],i[1]+1):
                    a.append(j)
                subsetf.append(a)
            
        L=np.matmul(np.matmul(feature,W),feature.transpose())
        
    
        for k in range (len(subsetf)):
            sub=subset[k]
            ly=[]
            for i in sub:
                a=[]
                for j in sub:
                    a.append(L[i][j])
                ly.append(a)
            try:  
                ly=np.array(ly)
                lyinv=np.linalg.inv(ly)
            
                b=[]
                for i in range (len(sub)):
                    for j in range (len(sub)):
                          b.append(lyinv[i][j])
                start=0
                stop=1

                for i in sub:
                    for j in sub:
                        for k in range(start,stop):
                            Z[i][j]=Z[i][j]+b[k]
                            start=start+1
                            stop=stop+1
                            break
                Z=Z/len(subset)
            except:
                print("dead end")
                print(k)
                
        L=L+np.matmul(eta*(L),((Z-np.matmul(np.linalg.inv(L+I),L))))
        return L
#         return b
feature=np.load("/home/her/DPP/featurefinal.npy")
subset=np.load("/home/her/DPP/subsetfinal.npy")
a=fixed_point_map(feature,subset)
