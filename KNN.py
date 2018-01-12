import numpy as np
import operator

def createDataSet():
    group = np.array([
        [1.0,1.1],
        [1.0,1.0],
        [0.,0.],
        [0.,0.1]
    ])
    labels=['A','A','B','B']
    return group,labels

def classfy0(inX, dataset, labels,k):
    """

    :param inX:输入的测试样本，是一个[x,y]样式的
    :param dataset: 训练样本集
    :param labels: 训练样本标签
    :param k: 是top k最相近的
    :return:
    """
    dataSetSize = dataset.shape[0]
    diffMat = np.tile(inX, (dataSetSize,1)) - dataset
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance ** 0.5

    sortedDistIndicies = distance.argsort()

    # 存放最终的分类结果以及相应的投票数
    classCount = {}
    # 投票过程 就是统计前k个最近的样本所属类别包含的样本总数
    for i in  range(k):
        voteTlabel = labels[sortedDistIndicies[i]]
        classCount[voteTlabel] = classCount.get(voteTlabel, 0) + 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


if __name__ == "__main__":
    # 导入数据
    dataset,labels = createDataSet()
    inX = [0.1, 1.6]
    # 简单分类
    className = classfy0(inX, dataset,labels,3)
    print('the class of test sample is %s' %className)




