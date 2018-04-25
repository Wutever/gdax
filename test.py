import gdax
import matplotlib.pyplot as plt
import datetime
import numpy as np
public_client = gdax.PublicClient()  
rate_openl=[]
rate_volumel=[]
for i in range (1,28,3):
   starttim=datetime.datetime(2017, 10, i, 0, 0)
   starttime=starttim.isoformat()
   print (starttime)
   k=10
   j=i+3
   if (i+3>31):
       k=11
       j=i+3-31
   endtim=datetime.datetime(2017, k, j, 0, 0)
   endtime=endtim.isoformat()
   print(endtime)
   rate=public_client.get_product_historic_rates('BTC-USD',start=starttime,end=endtime,granularity=1800)
   rate_open_temp=np.flip((np.asarray(rate)[:,3]),0)
   rate_volume_temp=np.flip((np.asarray(rate)[:,5]),0)
   rate_openl.append(rate_open_temp.tolist())
   rate_volumel.append(rate_volume_temp.tolist())
   #print(rate_openl)
   rate_open=np.asarray(sum(rate_openl,[]))
   rate_volume=np.asarray(sum(rate_volumel,[]))
   length = np.shape(rate_volume) [0]
   
   #print (length)
   training_data=np.zeros((length-11,20))
   training_labels=np.zeros(length-11)

for i in range (0,length-11):
   for j in range (0,10):
       training_data[i][j]=rate_open[i+j]
       training_data[i][j+10]=rate_volume[i+j]
   real_rate=rate_open[i+11]/rate_open[i+9]
  # print (rate_open[i+11])
   #print (rate_open[i+9])
   if (real_rate-1)>0.005:
       training_labels[i]=0
   elif (real_rate-1)<0.005and(real_rate-1)>0.0025:
       training_labels[i]=1
   elif (real_rate-1)<0.0025and(real_rate-1)>-0.0025:
       training_labels[i]=2
   elif (real_rate-1)<-0.0025and(real_rate-1)>-0.005:
       training_labels[i]=3
   elif (real_rate-1)<-0.005    :
       training_labels[i]=4
