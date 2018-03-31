from copy import deepcopy

class priority_queue:
    def __init__(self):
        self.mList = [[-999,-999]]

    def getList(self):
        return deepcopy(self.mList)

    def swap(self, idx1, idx2):
        temp = self.mList[idx1][:]
        self.mList[idx1] = self.mList[idx2][:]
        self.mList[idx2] = temp[:]

    def heapify(self, n):
        while n > 1:
            if self.mList[n][0] < self.mList[n//2][0]:
                self.swap(n, n//2)
            n = n//2
    
    def heapify_root(self):
        self.mList[1] = [999999999, 1]
        current_idx = 1
        finish = False
        while not finish:
            if 2*current_idx+1 < len(self.mList):
                if self.mList[2*current_idx + 1][0] > self.mList[2*current_idx][0]:
                    self.swap(current_idx, 2*current_idx)
                    current_idx = 2*current_idx
                else:
                    self.swap(current_idx, 2*current_idx+1)
                    current_idx = 2*current_idx+1
            elif 2*current_idx < len(self.mList):
                self.swap(current_idx, 2*current_idx)
                current_idx = 2*current_idx
            else:
                self.mList.pop(len(self.mList)-1)
                finish = True


    def insert(self, unitx):
        self.mList.append(unitx[:])
        last_idx = len(self.mList) - 1

        self.heapify(last_idx)

    def getFrontPop(self):
        if len(self.mList) > 1:
            result = self.mList[1][:]
            self.heapify_root()                
            return result
        return [-999, -999]

class KNN:
    def __init__(self, k = 3):
        self.feature = []
        self.label = []
        self.k = k

    def fit(self, xlist, ylist):
        for unit_x in xlist:
            self.feature.append(unit_x)
        
        for unit_y in ylist:
            self.label.append(unit_y)

    def distance(self, list1, list2):
        summ = [0]
        for i in range(len(list1)):
            summ[0] += (list1[i]-list2[i]) * (list1[i]-list2[i])
        return summ[0]

    def predict(self, listx):
        pqueue = priority_queue()
        for i in range(len(self.feature)):
            dist = self.distance(listx, self.feature[i])
            pqueue.insert([dist,i])

        label_map = {}
        for i in range(self.k):
            front = pqueue.getFrontPop()
            idx = front[1]
            mLabel = self.label[idx]
            if mLabel in label_map:
                label_map[mLabel] += 1
            else:
                label_map[mLabel] = 1

        key_max = [-1]
        for key in label_map:
            if key_max[0] == -1:
                key_max[0] = key
            else:
                if label_map[key_max[0]] < label_map[key]:
                    key_max[0] = key
        return key_max


x = [[-1,-1], [-2,-3], [4,4], [9,5], [3,8]]
y = [2, 2, 1, 1, 1]
knn = KNN(3)
knn.fit(x, y)
result = knn.predict([-2,-2])
print(result)

