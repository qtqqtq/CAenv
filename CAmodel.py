#元胞自动机的模型
#统计上下左右的方格，奇数生长，偶数死亡

class CAmodel:
    def __init__(self,size):
        self.size=size
        self.matrix=[[None]*size for _ in range(size)]

    def next_state(self):
        self.next_matrix=[[None]*self.size for _ in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                correct_x=x+1
                correct_y=y+1
                if x==self.size-1:
                    correct_x=0
                if y==self.size-1:
                    correct_y=0
                near=[self.matrix[x-1][y],self.matrix[x][y-1],self.matrix[correct_x][y],self.matrix[x][correct_y]].count(True)
                if near%2==0:
                    self.next_matrix[x][y]=None
                else:self.next_matrix[x][y]=True
        self.matrix=self.next_matrix

    def print_list(self):
        for i in self.matrix:
            print(i)
        print('')

if __name__=='__main__':
    model=CAmodel(5)
    model.matrix[0][0]=True
    model.matrix[4][0]=True
    for _ in range(10):
        model.next_state()
        model.print_list()