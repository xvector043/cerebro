# cerebro
Dsg data submission
for predicting snow depth,first using X.describe() to check the missing data and 
1.these missing values  may be removed
2.mean values of the row should be entered in the missing  values
but both the above ways give almost same accuracy.
using some simple models in the first like decisiontreeregression,randomtreeregression ,these gives us a MAE of about 8
then before shifting to other models first thing to notice that we hae implimented the model on the whole train data but one way to increae the accuracy is to divide the train data into train data and  test data .putting train size as 0.6  and test size as 0.4 ,random state =2 gives the best accuracy of all possible.
since more is the data ,more is the accuracy .so , whole train columns is entered as feature name taking consideration to remove date  as it cannot be converted into float
imputation is used to remove the missing values
using support vector regression gives a better accuracy ,MAE =12
to further increase the accuracy ,Xgboost  may be used.
