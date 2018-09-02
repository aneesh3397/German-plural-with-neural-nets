import sys
import numpy as np
from sklearn.neural_network import MLPClassifier

def show_result(pred):
    
    inflections = ['-s','-n','-e','-e+umlaut','null','umlaut','-er+umlaut','No marking','Double marking']
    
    results_rand = np.zeros((9), dtype=np.int)
    results_proto = np.zeros((9), dtype=np.int)
    
    for i in range(pred.shape[0]):
        sum = pred[i].sum()
        if(i>=70):#test example is randomly generated
          if sum == 1:
            results_rand[np.argmax(pred[i])]+=1
          elif sum < 1:
            results_rand[7]+=1
          elif sum > 1:
            results_rand[8] += 1
            
        if(i<70):#test example resembles prototype
          if sum == 1:
            results_proto[np.argmax(pred[i])]+=1
          elif sum < 1:
            results_proto[7]+=1
          elif sum > 1:
            results_proto[8] += 1
    
    print("Results on test examples generated from prototypes:",'\n')
    
    for i in range(len(results_proto)):
      print(inflections[i],': ',results_proto[i])
      
    print('\n')
      
    print("Results on randomly generated test examples:",'\n')
    
    for i in range(len(results_rand)):
      print(inflections[i],': ',results_rand[i],)
      

    
    
def main(argv):
    inputfn = argv[1]
    outputfn = argv[2]
    testfn = argv[3]

    # create array structures for each of the input files
    inputs = np.loadtxt(inputfn)
    outputs = np.loadtxt(outputfn)
    test = np.loadtxt(testfn)
    
    net = MLPClassifier(hidden_layer_sizes=(10,), solver='sgd', activation='logistic', 
        learning_rate_init=.1, max_iter=10000, verbose=False, early_stopping=False,
        tol = .00000001 , momentum = 0, warm_start=True) 
    
    #training the network:
    net.fit(inputs, outputs)
    
    #make predictions on test data:
    predictions = net.predict(test)
    
    #function to print results:
    show_result(predictions)
    
if __name__ == "__main__":
    main(sys.argv)