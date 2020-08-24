import urllib.request as ur
import tqdm


# 进度条类
class TqdmUpTo(tqdm.tqdm):
    # Provides `update_to(n)` which uses `tqdm.update(delta_n)`.

    last_block = 0

    def update_to(self, block_num=1, block_size=1, total_size=None):
        if total_size is not None:
            self.total = total_size
        self.update((block_num - self.last_block) * block_size)
        self.last_block = block_num


def main():
    link = "https://ak.hypergryph.com/downloads/android_lastest"
    local = 'Arknights.zip'
    try:
        with TqdmUpTo(unit='B', unit_scale=True, unit_divisor=1024, miniters=0, desc="Arknights",
                      dynamic_ncols=False, ncols=80) as t:  # 继承至tqdm父类的初始化参数
            ur.urlretrieve(link, filename=local, reporthook=t.update_to, data=None)
        input("按任意键继续...")
    except KeyboardInterrupt:
        t.close()
        raise
    t.close()
 
    """
    "B"在原单位后加B，KB、GB...
    ncols是一行显示的字符，太短会造成换行
    dynamic_ncols动态换行，始终在当前窗口显示所有内容
    miniters最小迭代频率，0实时更新
    """


if __name__ == '__main__':
    main()
