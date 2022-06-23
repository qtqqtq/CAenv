#元胞自动机的模型
#统计上下左右的方格，奇数生长，偶数死亡

class CAmodel:
    def __init__(self,size):
        self.size=size
        self.matrix=[[0]*size for _ in range(size)]

    def next_state(self):
        next_matrix=[[0]*self.size for _ in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                correct_x=x+1
                correct_y=y+1
                if x==self.size-1:
                    correct_x=0
                if y==self.size-1:
                    correct_y=0
                near=[self.matrix[x-1][y-1],self.matrix[x-1][y],self.matrix[x][y-1],self.matrix[correct_x][y],self.matrix[x][correct_y],self.matrix[correct_x][y-1],self.matrix[x-1][correct_y],self.matrix[correct_x][correct_y]].count(1)
                if near<2 or near>3:
                    next_matrix[x][y]=0
                elif near==2:next_matrix[x][y]=self.matrix[x][y]
                elif near==3:next_matrix[x][y]=1
        self.matrix=next_matrix

    def print_list(self):
        for i in self.matrix:
            print(i)
        print('')

if __name__=='__main__':
    model=CAmodel(5)
    model.matrix[0][2]=1
    model.matrix[1][0]=1
    model.matrix[1][2]=1
    model.matrix[2][1]=1
    model.matrix[2][2]=1
    for _ in range(20):
        model.print_list()
        model.next_state()