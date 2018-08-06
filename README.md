# K-MCI
This is an implementation of K-MCI algorithm in python based on a study by (Ganesh Krishnasamy,Ganesh Krishnasamy Raveendran Paramesran; Raveendran Paramesran;2014)

All datasets are from UCI Machine Learning Repository (Bache & Lichman, 2013). But Vowel dataset was removed from UCI machine learning repository so we downloaded from http://www.ntu.edu.sg/home/asjagath/ce434/vowel.html.<br>
<br>In article author mentioned we have 683 samples for Wisconsin Breast Cancer dataset. Actually there are 699 samples but 16 of samples have missing data so in this implementation we remove all missing data in preprocessing step.

# Issue 1 (Kmean iteration count not defined)
Notice: the default value in Kmean algorithm of sklearn library is 10.
Notice: In this article I found best value is 20 to 50. So I selected the maximum.
https://static.googleusercontent.com/media/research.google.com/vi//pubs/archive/42853.pdf

# Issue 2 (No talk about Standardization or Normalization)
Notice: If you look at the datasets, we know we have to use some standardization
Notice: Because there is no information about how to standard data, we select which give is higher fitness compare to article.
Notice: We used this standardization method 