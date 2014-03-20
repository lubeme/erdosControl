import netGrowControl
import json

iters = 100
n=100
controlersPerEdgesPerIters={}
for k in xrange (0, iters):
    if k>0 and k%(iters/10)==0:
        print "iteracion:",k
    controlersPerEdgesPerIters[k]= netGen.net_grow_control(n)
with open('data.json', 'wb') as fp:
    json.dump(controlersPerEdgesPerIters, fp)
