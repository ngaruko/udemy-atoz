# Data Preprocessing

# Importing the dataset
dataset = read.csv('Data.csv')

# Taking care of missing data
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