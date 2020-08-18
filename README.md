# Naive-Bayes-Classifier
Comparing the performance of Naive Bayes Classifier using different smoothing techniques and word features 

## Instructions to Run the Code

### Laplace Smoothing
* Open the Laplace Smoothing Directory

* Run the nbtrain.py from the command prompt as follows:
```
python nbtrain.py <training-directory> <model-file>
e.g.
python nbtrain.py C:\Users\dines\Desktop\CS6200+\NaiveBayes\textcat\train model_file_ls.txt
```
Doing so will generate a text model file which will be later passed to nbtest.py for further classification.

* Run the nbtest.py from the command prompt as follows:
```
python nbtest.py <model-file> <test-directory> <predictions-file>
e.g. 
python nbtest.py model_file_ls.txt C:\Users\dines\Desktop\CS6200+\NaiveBayes\textcat\test predict_test_ls.txt 
```

### Jelinek-Mercer Smoothing
* Open the Jelinek-Mercer Smoothing Directory

* Run the nbtrain_jms.py from the command prompt as follows:
```
python nbtrain_jms.py <training-directory> <model-file>
e.g. 
python nbtrain_jms.py C:\Users\dines\Desktop\CS6200+\NaiveBayes\textcat\train model_file_jms.txt
```
Doing so will generate a text model file which will be later passed to nbtest.py for further classification.

* Run the nbtest.py from the command prompt as follows:
```
python nbtest.py <model-file> <test-directory> <predictions-file>
e.g. 
python nbtest.py model_file_jms.txt C:\Users\dines\Desktop\CS6200+\NaiveBayes\textcat\test predict_test_jms.txt 
```
### Dirichlet Smoothing
* Open the Dirichlet Smoothing Directory

* Run the nbtrain_ds.py from the command prompt as follows:
```
python nbtrain_ds.py <training-directory> <model-file>
e.g. 
python nbtrain_ds.py C:\Users\dines\Desktop\CS6200+\NaiveBayes\textcat\train model_file_ds.txt
```
Doing so will generate a text model file which will be later passed to nbtest.py for further classification.

* Run the nbtest.py from the command prompt as follows:
```
python nbtest.py <model-file> <test-directory> <predictions-file>
e.g. 
python nbtest.py model_file_ls.txt C:\Users\dines\Desktop\CS6200+\NaiveBayes\textcat\test predict_test_ls.txt 
```

### Bigram Feature
* Open the Bigram Directory

* Run the nbtrain_bg.py from the command prompt as follows:
```
python nbtrain_bg.py <training-directory> <model-file>
e.g. 
python nbtrain_bg.py C:\Users\dines\Desktop\CS6200+\NaiveBayes\textcat\train model_file_bg.txt
```
Doing so will generate a text model file which will be later passed to nbtest_bg.py for further classification.

* Run the nbtest_bg.py from the command prompt as follows:
```
python nbtest_bg.py <model-file> <test-directory> <predictions-file>
e.g. python nbtest.py model_file_ls.txt C:\Users\dines\Desktop\CS6200+\NaiveBayes\textcat\test predict_test_bg.txt 
```

## Results

### Laplace Smoothing (add-1 smoothing)
* Results for the Laplace smoothing are stored in the Laplace Smoothing directory.

* The results are arranged as follows:
	1> predict_dev_pos_ls.txt - predictions file for the dev data (postive reviews)
	2> predict_dev_neg_ls.txt - predictions file for the dev data (negative reviews)
	3> predict_test_ls.txt - predictions file for the test data
	4> top_20_neg_to_pos_logratio.txt - List of the 20 terms with the highest (log) ratio of negative to positive weight.
	5> top_20_pos_to_neg_logratio.txt - List of the 20 terms with the highest (log) ratio of positive to negative weight.

* Upon analysis of the results of predictions file on dev data, the following was determined:
	1> 75 % of positive reviews in the dev data were correctly classified
	2> 80 % of negative reviews in the dev data were correctly classified

### Jelinek-Mercer Smoothing
* Results for this smoothing are stored in the Jelinek Mercer Smoothing directory.

* The results are arranged as follows:
	1> predict_dev_pos_jms.txt - predictions file for the dev data (postive reviews)
	2> predict_dev_neg_jms.txt - predictions file for the dev data (negative reviews)
	3> predict_test_jms.txt - predictions file for the test data

* Upon analysis of the results of predictions file on dev data, the following was determined:
	1> 75 % of positive reviews in the dev data were correctly classified
	2> 80 % of negative reviews in the dev data were correctly classified

### Dirichlet Smoothing
* Results for this smoothing are stored in the Dirichlet Smoothing directory.

* The results are arranged as follows:
	1> predict_dev_pos_ds.txt - predictions file for the dev data (postive reviews)
	2> predict_dev_neg_ds.txt - predictions file for the dev data (negative reviews)
	3> predict_test_ds.txt - predictions file for the test data

* Upon analysis of the results of predictions file on dev data, the following was determined:
	1> 69 % of positive reviews in the dev data were correctly classified
	2> 80 % of negative reviews in the dev data were correctly classified

### Bigram Feature
* Results for this feature are stored in the Bigram directory.

* The results are arranged as follows:
	1> predict_dev_pos_bg.txt - predictions file for the dev data (postive reviews)
	2> predict_dev_neg_bg.txt - predictions file for the dev data (negative reviews)

* Upon analysis of the results of predictions file on dev data, the following was determined:
	1> 80 % of positive reviews in the dev data were correctly classified
	2> 84 % of negative reviews in the dev data were correctly classified

## Requirements
Python 3.6+ is required to run this program.

The following additional modules have to be installed to ensure the working of the program:
* json
* glob

## Conclusion
Thus, from the above data it becomes clear that Laplace and Jelinek-Mercer Smoothing have similar performance
with respect to classification accuracy and they outperform Dirichlet Smoothing when used with unigram features.
However, using bigram features with Laplace Smoothing had the best accuracy among them all. 
