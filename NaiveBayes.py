from copy import deepcopy

class NaiveBayes:
    def __init__(self):
        self.label = []
        self.feature = []
        self.ftr_map = {}
        self.label_map = {}

    def get_feature_map(self):
        return deepcopy(self.ftr_map)

    def get_label_map(self):
        return deepcopy(self.label_map)


    def fit(self, feature_list, label_list):
        #insert data into class attribut
        for unit in feature_list:
            self.feature.append(unit)

        for unit in label_list:
            self.label.append(unit)

        #create map for feature data
        for i in range(len(self.feature)):
            for j in range(len(self.feature[i])):
                if j not in self.ftr_map:
                    self.ftr_map[j] ={}
                
                isi = self.feature[i][j]
                label = self.label[i]
                if isi not in self.ftr_map[j]:
                    self.ftr_map[j][isi] = {}

                if label not in self.ftr_map[j][isi]:
                    self.ftr_map[j][isi][label] = 1
                else:
                    self.ftr_map[j][isi][label] += 1


        #create map for label data
        for row in self.label:
            if row in self.label_map:
                self.label_map[row] += 1
            else:
                self.label_map[row] = 1



    def predict(self, feature_unit):
        p_max = [0]
        result = '-'
        for label in self.label_map:
            p_current = [1]
            for i in range(len(feature_unit)):
                pengali = [0]
                if feature_unit[i] not in self.ftr_map[i]:
                    pengali[0] = 0
                elif label not in self.ftr_map[i][feature_unit[i]]:
                    pengali[0] = 0
                else:
                    pengali[0] = self.ftr_map[i][feature_unit[i]][label] / self.label_map[label]
                p_current[0] = p_current[0] * pengali[0]

            p_current[0] *= self.label_map[label] / len(self.label)

            if p_current[0] > p_max[0]:
                p_max[0] = p_current[0]
                result = label
        return result

    def score(self, x_test, y_test):
        right_result = [0]
        for i in range(len(x_test)):
            label_predict = self.predict(x_test[i])
            if label_predict == y_test[i]:
                right_result[0] += 1
        return right_result[0] / len(x_test)

nb = NaiveBayes()

data_feature = [
        ["sunny", "hot", "high", "true"],
        ["sunny", "hot", "high", "false"],
        ["overcast", "hot", "high", "false"]
        ]

data_label = [
        "no",
        "no",
        "yes"
        ]

#nb.fit(data_feature, data_label)
#feature_map = nb.get_feature_map()
#label_map = nb.get_label_map()
#
#
#print(feature_map)
#print(label_map)
#
#print(nb.predict(data_feature[0]))




