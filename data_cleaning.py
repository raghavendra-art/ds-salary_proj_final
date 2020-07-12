# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:31:58 2020

@author: admin
"""


import pandas as pd
df = pd.read_csv('C:/Users/admin/Documents/ds_salary_proj-master/glassdoor_jobs.csv')



#Salary parsing
#company name text only
# state field
#age of company
# parsing of job description


df['hourly'] = df['Salary Estimate'].apply(lambda x:1 if 'per hour' in x.lower() else 0)
df['employer provided'] = df['Salary Estimate'].apply(lambda x:1 if 'employer provided salary:' in x.lower() else 0)


df= df[df['Salary Estimate'] != '-1']

Salary = df['Salary Estimate'].apply(lambda x:x.split('(')[0])
minus_kd = Salary.apply(lambda x:x.replace('K','').replace('$',''))


minus_hr = minus_kd.apply(lambda x:x.lower().replace('per hour','').replace('employer provided salary:',''))
df['min_salary'] = minus_hr.apply(lambda x:(x.split('-')[0]))
df['min_salary'] = df['min_salary'].astype(int)

df['max_salary'] = minus_hr.apply(lambda x:(x.split('-')[1]))
df['max_salary'] = df['max_salary'].astype(int)
df['average_salary'] = df['min_salary'] + df['max_salary'] / 2


#company name text only

df['company_text'] = df.apply(lambda x:x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)

df['job_state'] = df['Location'].apply(lambda x:x.split(',')[1])

df['same_state'] =df.apply(lambda x:1 if x['Location'] == x['Headquarters'] else 0,axis=1)

#age of company
# if age available then - 2020 else keep it as negative 1
df['age'] = df['Founded'].apply(lambda x:x if x<1 else 2020-x)

#Job description

print(df['Job Description'][0])

#python
df['python_yn'] = df['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)
#r studio
df['r_yn'] = df['Job Description'].apply(lambda x:1 if 'r studio' in x.lower() else 0)
#spark
df['python_yn'] = df['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)
#aws
df['python_yn'] = df['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)
#excel
df['python_yn'] = df['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)