import glob
import queue
import threading
import shutil
import os
import sys

fileQueue = queue.Queue()


class ThreadedCopy:
    totalFiles = 0
    copyCount = 0
    lock = threading.Lock()

    def __init__(self, src_path):
        fileList = glob.glob("\\".join([src_path, "char_*.png"]), recursive=True)
        self.destPath = "\\".join([src_path, "workspace"])

        if not os.path.exists(self.destPath):
            os.mkdir(self.destPath)

        self.totalFiles = len(fileList)

        print(str(self.totalFiles) + " files to copy.")
        self.threadWorkerCopy(fileList)

    def CopyWorker(self):
        while True:
            fileName = fileQueue.get()
            shutil.copy(fileName, self.destPath)
            fileQueue.task_done()
            with self.lock:
                self.copyCount += 1
                percent = (self.copyCount * 100) / self.totalFiles
                print(str(percent) + " percent copied.", end='r')

    def threadWorkerCopy(self, fileNameList):
        for i in range(16):
            t = threading.Thread(target=self.CopyWorker)
            t.daemon = True
            t.start()
        for fileName in fileNameList:
            fileQueue.put(fileName)
        fileQueue.join()


if __name__ == '__main__':
    try:
        Texture2D_path = sys.argv[1]
    except IndexError:
        # Texture2D_path = input("请输入Texture2D文件夹路径: ")
        Texture2D_path = r"C:\Users\SKNP\Documents\GitHub\Arknights\Texture2D"
    src_path = Texture2D_path
    if not os.path.exists(src_path):
        raise ValueError
    ThreadedCopy(src_path)
