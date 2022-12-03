import pandas as pd
import numpy as np
from operator import itemgetter

exam_data = {
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
}
label = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#data = [[exam_data[sub_data] for key in sub_data]]
exam = pd.DataFrame(exam_data, index = label) #creating your own creating index
print(exam[["name","score"]])
