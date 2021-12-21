import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

#############################
#该示例为创建200个（-0.5，0.5）的点集x，点集x加噪声获得点集y，点集x通过深度学习网络来拟合点集y的过程
#############################

#创建-0.5到0.5的200个点
x_data = np.linspace(-0.5, 0.5, 200)[:,np.newaxis]
#噪声点
noise = np.random.normal(0, 0.02, x_data.shape)
y_data = np.square(x_data) + noise
#定义两个placeholder存放输入数据
x = tf.placeholder(tf.float32, [None,1])
y = tf.placeholder(tf.float32, [None,1])

#中间层
w1 = tf.Variable(tf.random_normal([1,10]))
biases1 = tf.Variable(tf.zeros([1,10]))
w_biases1 = tf.matmul(x, w1) + biases1
L1 = tf.nn.tanh(w_biases1)

#输出层
w2 = tf.Variable(tf.random_normal([10,1]))
biases2 = tf.Variable(tf.zeros([1,1]))
w_biases2 = tf.matmul(L1,w2) + biases2
prediction = tf.nn.tanh(w_biases2)
#损失函数为均值平方差
loss = tf.reduce_mean(tf.square(y-prediction))
#使用梯度下降法更新权重
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.Session() as sess:
    #变量初始化
    sess.run(tf.global_variables_initializer())
    #训练循环2000次
    for _ in range(2000):
        sess.run(train_step,feed_dict={x:x_data,y:y_data})

    #获得预测值
    prediction_value = sess.run(prediction,feed_dict={x:x_data})

    #画图
    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,prediction_value,'-r',lw=5)
    plt.show()

