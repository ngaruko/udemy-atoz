# Data Preprocessing Template
library(caTools)
# Importing the dataset
dataset = read.csv('Data.csv')
dataset$Age = ifelse(is.na(dataset$Age),
                     #replace with mean if is a 'na'
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     #keep value if the value exists
                     dataset$Age)
#same for dataset$Salary
dataset$Salary = ifelse(is.na(dataset$Salary),
                     #replace with mean if is a 'na'
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     #keep value if the value exists
                     dataset$Salary)

# Encoding categorical data
dataset$Country = factor(dataset$Country,
                        levels = c('France', 'Spain', 'Germany'),
                          labels=c(1, 2, 3))

# Encoding categorical data  dataset$Purchased
dataset$Purchased = factor(dataset$Purchased,
                         levels = c('No', 'Yes'),
                         labels=c(0, 1))

#Splitting the dataset into the Training set and Test set using caTools

set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling
#only scaling col 2 and 3 (1 and 4 are factors not numeric)
training_set[, 2:3] = scale(training_set[, 2:3] )
test_set[, 2:3]  = scale(training_set[, 2:3] )

