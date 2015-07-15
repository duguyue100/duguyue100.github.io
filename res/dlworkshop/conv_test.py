"""" convnet test """

import os;
import gzip;
import cPickle as pickle;

import numpy as np;
import theano;
import theano.tensor as T;
from theano.tensor.nnet import conv;
from theano.tensor.signal import downsample;

n_epochs=100;
batch_size=100;

def relu(x):
    return x*(x>1e-13);

class ConvLayer(object):
    def __init__(self, filter_size, num_filters, num_channels, fm_size, batch_size, **kwargs):
        self.filter_size=filter_size;
        self.num_filters=num_filters;
        self.num_channels=num_channels;
        self.fm_size=fm_size;
        self.batch_size=batch_size;

        super(ConvLayer, self).__init__(**kwargs);
        
        self.initialize();

        self.params=[self.filters, self.bias];

    def initialize(self):
        filter_shape=(self.num_filters, self.num_channels)+(self.filter_size);
        self.filters=theano.shared(np.asarray(np.random.uniform(low=-0.0001,
                                                                high=0.0001,
                                                                size=filter_shape),
                                              dtype="float32"),
                                   borrow=True);
        self.bias=theano.shared(np.asarray(np.zeros((self.num_filters, )),
                                           dtype="float32"), borrow=True);
    
    def apply_lin(self, X):
        Y=conv.conv2d(input=X,
                      filters=self.filters,
                      image_shape=(self.batch_size, self.num_channels)+(self.fm_size),
                      filter_shape=(self.num_filters, self.num_channels)+(self.filter_size));
        Y+=self.bias.dimshuffle('x', 0, 'x', 'x');
        return Y;

class ReLUConvLayer(ConvLayer):
    def __init__(self, **kwargs):
        super(ReLUConvLayer, self).__init__(**kwargs);

    def apply(self, X):
        return relu(self.apply_lin(X));

class MaxPooling(object):
    def __init__(self, pool_size):
        self.pool_size=pool_size;

    def apply(self, X):
        return downsample.max_pool_2d(X, self.pool_size);

class Layer(object):
    def __init__(self, in_dim, out_dim, W=None, b=None, **kwargs):
        self.in_dim=in_dim;
        self.out_dim=out_dim;
        self.W=W;
        self.b=b;

        self.initialize();

        super(Layer, self).__init__(**kwargs);

        self.params=[self.W, self.b];

    def initialize(self):
        if self.W == None:
            self.W=theano.shared(np.asarray(np.random.uniform(low=-0.0001,
                                                              high=0.0001,
                                                              size=(self.in_dim, self.out_dim)),
                                 dtype="float32"),
                                 borrow=True);
        if self.b == None:
            self.b=theano.shared(np.asarray(np.zeros((self.out_dim, )),
                                            dtype="float32"), borrow=True);

    def apply_lin(self, X):
        return T.dot(X, self.W)+self.b;

class ReLULayer(Layer):
    def __init__(self, **kwargs):
        super(ReLULayer, self).__init__(**kwargs);

    def apply(self, X):
        return relu(self.apply_lin(X));              


class TanhLayer(Layer):
    def __init__(self, **kwargs):
        super(TanhLayer, self).__init__(**kwargs);

    def apply(self, X):
        return T.tanh(self.apply_lin(X));              
            
class SoftmaxLayer(Layer):
    def __init__(self, **kwargs):
        super(SoftmaxLayer, self).__init__(**kwargs);

    def apply(self, X):
        return T.nnet.softmax(self.apply_lin(X));

    def predict(self, X_out):
        return T.argmax(X_out, axis=1);

    def error(self, X_out, Y):
        return T.mean(T.neq(self.predict(X_out), Y));

# load dataset

def shared_dataset(data_xy):
    data_x, data_y=data_xy;

    shared_x=theano.shared(np.asarray(data_x, dtype="float32"),
                           borrow=True);
    shared_y=theano.shared(np.asarray(data_y, dtype="float32"),
                           borrow=True);

    return shared_x, T.cast(shared_y, "int32");

def load_mnist(dataset):
    f=gzip.open(dataset, 'rb');
    train_set, valid_set, test_set=pickle.load(f);
    f.close();

    train_set_x, train_set_y=shared_dataset(train_set);
    valid_set_x, valid_set_y=shared_dataset(valid_set);
    test_set_x, test_set_y=shared_dataset(test_set);

    return [(train_set_x, train_set_y), (valid_set_x, valid_set_y), (test_set_x, test_set_y)];


dataset=load_mnist("mnist.pkl.gz");

train_set_x, train_set_y=dataset[0];
valid_set_x, valid_set_y=dataset[1];
test_set_x, test_set_y=dataset[2];

n_train_batches=train_set_x.get_value(borrow=True).shape[0]/batch_size;
n_valid_batches=valid_set_x.get_value(borrow=True).shape[0]/batch_size;
n_test_batches=test_set_x.get_value(borrow=True).shape[0]/batch_size;

print n_train_batches
print n_valid_batches
print n_test_batches
    
print "dataset loaded"    

# build mode

X=T.matrix("data");
y=T.ivector("label");
idx=T.lscalar();

images=X.reshape((batch_size, 1, 28, 28));

### configure some layers

### build some convlayers

layer_0=ReLUConvLayer(filter_size=(7,7), num_filters=10, num_channels=1,
                      fm_size=(28, 28), batch_size=batch_size);
pool_0=MaxPooling((2,2));
layer_1=ReLUConvLayer(filter_size=(4,4), num_filters=10, num_channels=10,
                      fm_size=(11,11), batch_size=batch_size);
pool_1=MaxPooling((2,2));
layer_2=ReLULayer(in_dim=160, out_dim=100);
layer_3=SoftmaxLayer(in_dim=100, out_dim=10);

### compile some model

out=pool_1.apply(layer_1.apply(pool_0.apply(layer_0.apply(images))))
out=out.flatten(ndim=2);
out=layer_3.apply(layer_2.apply(out));

cost=T.nnet.categorical_crossentropy(out, y).mean();
params=layer_0.params+layer_1.params+layer_2.params+layer_3.params;

#### calculate the updates of each params

gparams=T.grad(cost, params);

from collections import OrderedDict;
updates=OrderedDict();
for param, gparam in zip(params, gparams):
    updates[param]=param-0.01*gparam;    

train=theano.function(inputs=[idx],
                      outputs=cost,
                      updates=updates,
                      givens={X: train_set_x[idx*batch_size: (idx+1)*batch_size],
                              y: train_set_y[idx*batch_size: (idx+1)*batch_size]});

test=theano.function(inputs=[idx],
                     outputs=layer_3.error(out, y),
                     givens={X: test_set_x[idx*batch_size: (idx+1)*batch_size],
                             y: test_set_y[idx*batch_size: (idx+1)*batch_size]});

print "the model is built :)"

# train the model

test_record=np.zeros((n_epochs, 1));

epoch=0;

while (epoch<n_epochs):
    epoch+=1;

    for minibatch_index in xrange(n_train_batches):
        mlp_train_cost=train(minibatch_index);

        iteration=(epoch-1)*n_train_batches+minibatch_index;
        
        if (iteration+1)%n_train_batches==0:
            print "MLP model";
            
            test_cost=[test(i) for i in xrange(n_test_batches)];
            test_record[epoch-1]=np.mean(test_cost);
            
            print "   epoch %i, test error %f %%" % (epoch, test_record[epoch-1]*100.);




















