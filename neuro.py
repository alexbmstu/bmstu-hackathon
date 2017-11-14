# ������ ����������� �������
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

def constructPerceptron (name, numNeurons):
    """���������� ����������� ����

    ���������:
    name -- ��� ����, ������
    numNeurons -- ����� �������� � ������ ����, ������ �� ����� �����

    """
    # ������ ����
    net = FeedForwardNetwork(name)
    # ������ ���� � ��������� �� � ����
    prevLayer = None
    newLayer = None
    for i, val in enumerate(numNeurons):
        # ���� ���� �������, �� ��������
        if (i == 0): 
            newLayer = LinearLayer(val, 'input')
            net.addInputModule(newLayer)
            prevLayer = newLayer
        # ���� ���� ��������, �� ��������    
        elif (i == len(numNeurons) - 1):
            newLayer = LinearLayer(val, 'output')
            net.addOutputModule(newLayer)
        # ����� - ���� ����������   
        else:
            newLayer = SigmoidLayer(val, 'hidden_' + str(i))
            net.addModule(newLayer)    
        # ���� ���� �� �������, ������ ����� ����� ����� � ���������� ������
        if (i > 0):
            conn = FullConnection(prevLayer, newLayer, 'conn_' + str(i))
            net.addConnection(conn)
            prevLayer = newLayer
    # ������� ���� � ���������, ������������ � ���������� ���������        
    net.sortModules()
    # ������
    return net

def constructDataset (name, learnData):
    """���������� ��������� ������� � ������� PyBrain

    ���������:
    name -- ��� ������ ������, ������
    learnData -- ������ ��� ��������: ������ �������� ���� "������� �������� - �������� ������"

    """
    # ��������� ����������� ������� ������
    dimIn = len(learnData[0][0])
    dimOut = len (learnData[0][1])
    ds = SupervisedDataSet(dimIn, dimOut)
    for d in learnData:
        ds.addSample(d[0], d[1])
    return ds

def trainNetwork (net, trainData):
    """���������� ����, ��������� 1 ����� ��������, � ������ ������

    ���������:
    net - ��������� ����, PyBrain network
    trainData -- ��������� ����� ������, PyBrain dataset

    """
    # ������� ��� �������� � ��������
    trainer = BackpropTrainer(net, trainData)
    # ��������� ������� �� 1 ����� � ���������� ������ ������ 
    coef = trainer.train()
    return (net, coef)

def saveNetwork (net, name):
    """������� ��������� ���� � ����

    ���������:
    net - ��������� ����, PyBrain network
    name -- ��� �����, ������

    """
    NetworkWriter.writeToFile(net, name)

def importNetwork (name):
    """���������� ��������������� �� ����� ��������� ����

    ���������:
    name - ��� �����, ������

    """
    return NetworkReader.readFrom(name)     
        
