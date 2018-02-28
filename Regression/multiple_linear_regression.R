# Muliple Linear Regression

df <- read.csv('50_Startups.csv')
head(df)

# preprocessing
df$State <- factor(df$State,
                   levels = c('New York', 'California', 'Florida'),
                   labels = c(1, 2, 3))

# train test split
library(caTools)
split <- sample.split(df$State, SplitRatio = 0.8)
train.set <- subset(df, split == TRUE)
test.set <- subset(df, split == FALSE)

# Multiple linear Regression
reg <- lm(Profit ~ ., data = train.set)
summary(reg)

# pred 
y_pred = predict(reg, test.set)
