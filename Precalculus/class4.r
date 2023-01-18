
students <- read.csv('C:\\Users\\cag10\\Downloads\\precalc.csv',header = TRUE,
                  sep = ",", quote = "\"", dec = ".", 
                  fill = TRUE, comment.char = "", 
                  as.is = TRUE)
students <- students[!is.na(students$BAT)& !is.na(students$HS_GPA), ]
students$Passed <- ifelse(students$Grade >= 2, 1 , 0)


reg <- glm(Passed~SAT+HS_GPA+BAT, data=students,family=binomial)
students$Prediction <- predict(reg,type="response")



library("rpart")
library("rpart.plot")

ctrl <- rpart.control(minsplit = 50, cp=0.015, xval = 10)

#the minimum number of observations that must exist in a node in order for a split to be attempted

reg_tree <- rpart(Passed~SAT+HS_GPA+BAT+Prediction,
                     data=students, method="class", control=ctrl)

prp(reg_tree, extra=1, varlen=0, left=FALSE,yesno = 2,main="Precalculus Passed")
summary(reg_tree)

## What could the policy be, based on this information?
## What if we remove BAT from the prediction?

reg2 <- glm(Passed~SAT+HS_GPA, data=students,family=binomial)
students$Prediction2 <- predict(reg2,type="response")

ctrl <- rpart.control(minsplit = 50, cp=0.015, xval = 10)

#the minimum number of observations that must exist in a node in order for a split to be attempted

reg_tree <- rpart(Passed~SAT+HS_GPA+Prediction2+BAT,
                  data=students, method="class", control=ctrl)

prp(reg_tree, extra=1, varlen=0, left=FALSE,yesno = 2,main="Precalculus Passed")
summary(reg_tree)

