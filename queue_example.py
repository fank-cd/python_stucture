# coding:utf-8
"""
from Queue import Queue
q = Queue(3)
q.put('11111')
print(q.qsize())
q.put('23333')
print(q.qsize())
q.put('23333')
print(q.qsize())
q.put('23333')
print(q.empty())
print(q.full())
print(q.qsize())
# print(q.get_nowait())
# print(q.get_nowait())
# print(q.get_nowait())

# print(q.get())
# print(q.get())
# print(q.get())

"""


import time
import random
from Queue import Queue
from collections import deque
from threading import Thread
# 创建队列，设置队列最大数限制为3个
queue = Queue(3)



# 生产者线程


class Pro_Thread(Thread):
    def run(self):
        # 原材料准备，等待被生产
        tasks = deque([1, 2, 3, 4, 5, 6, 7, 8])
        global queue
        while True:
            try:
                # 从原材料左边开始生产
                # print(type(tasks))
                task = tasks.popleft()
                queue.put(task)
                #print(queue.empty())
                print('%s,%d,%s,%d' % (u"生产".encode('utf-8'), task, "现在队列数:", queue.qsize()))

                # 休眠随机时间
                time.sleep(random.random())
            # 如果原材料被生产完，生产线程跳出循环
            except IndexError:
                print("原材料已被生产完毕")
                break

# 消费者线程


class Con_Thread(Thread):
    def run(self):
        global queue
        while True:
            if queue.not_empty:
                # 通过get(),这里已经将队列减去了1
                task = queue.get()
                time.sleep(2)
                # 这里可能队列数已经空了，但是消费者手里还有正在消费的队列
                # 发出完成的信号，不发的话，join会永远阻塞，程序不会停止
                queue.task_done()
                print('%s,%d,%s,%d' % ("消费", task, '现在队列数', queue.qsize()))
            else:
                break

# 入口方法，主线程


def main():
    Pro_1 = Pro_Thread()
    # 把生产线程列为守护线程，否则主线程结束之后不会销毁该线程，程序不会停止，影响实验结果
    Pro_1.setDaemon(True)
    # 启动线程
    Pro_1.start()

    for i in range(2):
        Con_i = Con_Thread()
        # 把两个消费者线程列为守护线程，否则主线程结束之后不会销毁该线程，程序不会停止，影响实验结果
        Con_i.setDaemon(True)
        # 启动线程
        Con_i.start()
    global queue
    # 这里休眠一秒钟，等到队列有值，否则队列创建时是空的，主线程直接就结束了，实验失败，造成误导
    time.sleep(1)
    # 接收信号，主线程在这里等待队列被处理完毕后再做下一步
    queue.join()
    # 给个标示，表示主线程已经结束
    print("主线程结束")


if __name__ == '__main__':
    main()

