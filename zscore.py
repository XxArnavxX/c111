import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random


df = pd.read_csv("./school2.csv")
data = df["Math_score"].tolist()

def randomset(counter):
    dataset = []
    for i in range(0, counter):
        index = random.randint(0, len(data)-1)
        value = data[index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean


meanlist = []
for i in range(0, 1000):
    setofnames = randomset(100)
    meanlist.append(setofnames)

   
mean = statistics.mean(meanlist)
print("mean of sampling distribution = ", mean)
std_deviation = statistics.stdev(meanlist)
print("standard deviation of sampling distribution = ", std_deviation)

fs, fe = mean - std_deviation, mean+std_deviation
ss , se = mean - (2*std_deviation), mean+(2*std_deviation)
ts, te = mean - (3*std_deviation), mean+(3*std_deviation)

df = pd.read_csv("sample1.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([meanlist], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "mean of student who had math class: "))
fig.add_trace(go.Scatter(x = [fs, fe], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 end: "))
fig.add_trace(go.Scatter(x = [ss, se], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2 end: "))
fig.add_trace(go.Scatter(x = [ts, te], y = [0, 0.17], mode = "lines", name = "Standard Deviation 3 end: "))
fig.show()

df = pd.read_csv("sample2.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("Mean of sample2:- ",mean_of_sample2)
fig = ff.create_distplot([meanlist], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "mean of student who had math class: "))
fig.add_trace(go.Scatter(x = [fs, fe], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 end: "))
fig.add_trace(go.Scatter(x = [ss, se], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2 end: "))
fig.add_trace(go.Scatter(x = [ts, te], y = [0, 0.17], mode = "lines", name = "Standard Deviation 3 end: "))
fig.show()

df = pd.read_csv("sample3.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("Mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([meanlist], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "mean of student who had math class: "))
fig.add_trace(go.Scatter(x = [fs, fe], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 end: "))
fig.add_trace(go.Scatter(x = [ss, se], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2 end: "))
fig.add_trace(go.Scatter(x = [ts, te], y = [0, 0.17], mode = "lines", name = "Standard Deviation 3 end: "))
fig.show()

zscore = (mean - mean_of_sample2)/std_deviation
print(zscore)