# simple Polynomial Regression in R

# Loading dataset
df <- read.csv("Position_Salaries.csv")
head(df)

df = df[2:3]

# spliting the data
# library(caTools)
# split <- sample.split(df$Salary, SplitRatio = 0.8)
# train.set <- subset(df, split == TRUE)
# test.set <- subset(df, split == FALSE)

# Linear Regression
reg <- lm( Salary ~ . , data = df)
summary(reg)

# Poly Regression
df$Leve2 = df$Level^2

poly.reg <- lm( Salary ~ . , data = df)
summary(reg)

require(ggplot2)
ggplot()+
  geom_point(aes(x = df$Level, y = df$Salary),
             colour = 'blue')+
  geom_line(aes(x = df$Level, y = predict(poly.reg, newdata = df)),
            colour = 'red')