# Data Preprocessing Template
library(caTools)
# Importing the dataset
dataset = read.csv('Data.csv')


#Splitting the dataset into the Training set and Test set using caTools

set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling
#only scaling col 2 and 3 (1 and 4 are factors not numeric)
# training_set[, 2:3] = scale(training_set[, 2:3] )
# test_set[, 2:3]  = scale(training_set[, 2:3] )

