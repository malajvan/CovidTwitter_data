import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

tweets= pd.read_csv("tweets1.csv").dropna().head(1000)
sentiment_total = tweets['sentiment'].value_counts(normalize=True) * 100
topic_engagement_total=(tweets['topic'].value_counts(normalize=True) * 100).rename('total')
print(sentiment_total)
vaccine_topic_engagement=(tweets.loc[tweets['topic']=="v"]['sentiment'].value_counts(normalize=True) * 100*0.30).rename('vaccine attitude')
cs_topic_engagement=(tweets.loc[tweets['topic']=="cs"]['sentiment'].value_counts(normalize=True) * 100*0.106).rename('cases')
ac_topic_engagement=(tweets.loc[tweets['topic']=="ac"]['sentiment'].value_counts(normalize=True) * 100*0.277).rename('covid attitude')
m_topic_engagement=(tweets.loc[tweets['topic']=="m"]['sentiment'].value_counts(normalize=True) * 100*0.169).rename('mandate')
s_topic_engagement=(tweets.loc[tweets['topic']=="s"]['sentiment'].value_counts(normalize=True) * 100*0.148).rename('social impact')


data=(pd.concat([vaccine_topic_engagement,cs_topic_engagement,ac_topic_engagement,m_topic_engagement,s_topic_engagement],axis=1))


data['sent']=data.index

data=(data.melt(id_vars=["sent"],var_name="topic",value_name="ratio"))
data=data.replace("p","positive")
data=data.replace("/","neutral")
data=data.replace("n","negative")
print(data)
fig = px.sunburst(data,
                  path=['topic',"sent"],
                  values='ratio',
                  title="Topic engagement and sentiment ratio",
                  width=750, height=750,
)
fig.update_traces(textinfo="label+percent parent")
fig.show()
