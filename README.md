# CovidTwitter_data
Analyze Covid 19 sentiment of Twitter users with a focus on vaccination hesitancy. Read full report [here](https://github.com/malajvan/CovidTwitter_data/blob/main/Final%20Report.pdf).


## Background
Twitter has become an important outlet for people to share news and express their feelings, concerns, interest, especially during the pandemic, where social media platforms become the main outlet for people due to lockdown restrictions. We conducted English tweets content analysis, develop the 5 most notable topics discussed and analyze people's sentiment through these tweets, with a focus on vaccine and vaccine hesitancy. We managed to make many interesting conclusions from the collected data, painting a general picture of the general public's sentiment towards topics related to Covid

## Data 
We used the Tweepy library to query 1000 English tweets in a 72-hour window (Nov 27 to Nov 30, 2021). We then conducted keyword analysis to identify and characterize the 5 topics and manually code the sentiment value (negative/neutral/positive) for each tweet. 

## Methods
We developed the 5 topics by examining the first 200 tweets. We then used [tf-idf](https://monkeylearn.com/blog/what-is-tf-idf/) scoring to compute and find the top 10 most notable words for each topic and infer the sentiment and characterize the topics. In the process, we used [Tweepy](https://docs.tweepy.org/en/stable/) Python library to gather tweets. More details are in the Final Report above.


## Discussions
We concluded that vaccination and vaccine mandates were the most widely discussed topics. There was also a notable discussion on vaccine effectiveness, which is the most divisive topic out of all. A more detailed discussion is in the report.

## Authors

1.Hong Van Pham :
[Email](mailto:vanhongpham01@gmail.com), [Linkedin](https://www.linkedin.com/in/vanhpham/), [Facebook](https://www.facebook.com/hiiamvan)

2.Xiyue Zhang

3.Yujia Luo


## References
We consulted the following articles:

1.Kwok S, Vadde S, Wang G. 2021.
Tweet Topics and Sentiments Relating to COVID-19 Vaccination Among Australian Twitter Users: Machine Learning Analysis. https://www.jmir.org/2021/5/e26953
DOI: 10.2196/26953. Accessed: 2021-11-30.

2.Chandrasekaran R, Mehta V, Valkunde T, Moustakas E. 2021. Topics, Trends, and Sentiments of Tweets About the COVID-19 Pandemic: Temporal Infoveillance Study. https://www.jmir.org/2020/10/e22624
DOI: 10.2196/22624. Accessed: 2021-11-30.
