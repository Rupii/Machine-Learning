# Data preprocessing

#importing data

df <- read.csv("Data.csv")
head(df)


#imputing the missing values
df$Age = ifelse(is.na(df$Age), 
                 ave(df$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                 df$Age)

df$Salary = ifelse(is.na(df$Salary), 
                ave(df$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                df$Salary)

# Categorical variables

df$Country <- factor(df$Country,
                     levels = c('France', 'Spain', 'GErmany'),
                     labels = c(1, 2, 3))

df$Purchased <- factor(df$Purchased)


# spliting into train test
install.packages('caTools')
require(caTools)
set.seed(101)
# unlike in python we need to do some manual work in R
split = sample.split(df$Purchased, SplitRatio = 0.8)
train_set = subset(df, split == TRUE) 
test_set = subset(df, split == FALSE)

# feature scaling
train_set[,2:3] = scale(train_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])
