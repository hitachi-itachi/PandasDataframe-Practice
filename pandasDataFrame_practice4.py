import pandas as pd
import numpy as np

exam_data = {
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
}


exam = pd.DataFrame(exam_data, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) #creating your own creating index


print(exam.iloc[:3]) #using purely just integer