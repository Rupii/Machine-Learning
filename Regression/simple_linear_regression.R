# simple Linear Regression in R

# Loading dataset
df <- read.csv("Salary_Data.csv")
head(df)

# spliting the data
library(caTools)
split <- sample.split(df$Salary, SplitRatio = 0.8)
train.set <- subset(df, split == TRUE)
test.set <- subset(df, split == FALSE)

# Linear Regression
reg <- lm( Salary ~ YearsExperience , data = df)
summary(reg)

# Predicting on test
pred <- predict(reg, test.set)

#Vizualization
require(ggplot2)
pl <- ggplot() +  
  geom_point(data = train.set, aes(YearsExperience, Salary), color = 'red') + 
  geom_line(aes(x = train.set$YearsExperience, y = predict(reg, train.set)), color = 'blue') 
