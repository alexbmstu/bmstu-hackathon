# Импорт необходимых модулей
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

def constructPerceptron (name, numNeurons):
    """Возвращает необученную сеть

    Аргументы:
    name -- имя сети, строка
    numNeurons -- число нейронов в каждом слое, список из целых чисел

    """
    # Создаём сеть
    net = FeedForwardNetwork(name)
    # Создаём слои и добавляем их в сеть
    prevLayer = None
    newLayer = None
    for i, val in enumerate(numNeurons):
        # Если слой входной, он линейный
        if (i == 0): 
            newLayer = LinearLayer(val, 'input')
            net.addInputModule(newLayer)
            prevLayer = newLayer
        # Если слой выходной, он линейный    
        elif (i == len(numNeurons) - 1):
            newLayer = LinearLayer(val, 'output')
            net.addOutputModule(newLayer)
        # Иначе - слой сигмоидный   
        else:
            newLayer = SigmoidLayer(val, 'hidden_' + str(i))
            net.addModule(newLayer)    
        # Если слой не входной, создаём связь между новым и предыдущим слоями
        if (i > 0):
            conn = FullConnection(prevLayer, newLayer, 'conn_' + str(i))
            net.addConnection(conn)
            prevLayer = newLayer
    # Готовим сеть к активации, упорядочивая её внутреннюю структуру        
    net.sortModules()
    # Готово
    return net

def constructDataset (name, learnData):
    """Возвращает обучающую выборку в формате PyBrain

    Аргументы:
    name -- имя набора данных, строка
    learnData -- данные для обучения: список кортежей типа "входные признаки - выходной вектор"

    """
    # Вычисляем размерность входных данных
    dimIn = len(learnData[0][0])
    dimOut = len (learnData[0][1])
    ds = SupervisedDataSet(dimIn, dimOut)
    for d in learnData:
        ds.addSample(d[0], d[1])
    return ds

def trainNetwork (net, trainData):
    """Возвращает сеть, прошедшую 1 эпоху обучения, и оценку ошибки

    Аргументы:
    net - нейронная сеть, PyBrain network
    trainData -- обучающий набор данных, PyBrain dataset

    """
    # Трейнер для обучения с учителем
    trainer = BackpropTrainer(net, trainData)
    # Запускаем трейнер на 1 эпоху и запоминаем оценку ошибки 
    coef = trainer.train()
    return (net, coef)

def saveNetwork (net, name):
    """Экспорт нейронной сети в файл

    Аргументы:
    net - нейронная сеть, PyBrain network
    name -- имя файла, строка

    """
    NetworkWriter.writeToFile(net, name)

def importNetwork (name):
    """Возвращает импортированную из файла нейронную сеть

    Аргументы:
    name - имя файла, строка

    """
    return NetworkReader.readFrom(name)     
        
