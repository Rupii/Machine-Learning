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

print(df)
