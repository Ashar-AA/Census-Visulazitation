# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache_data()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above.

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()



# Designing of web app.
st.title("Census income prediction")
# st.sidebar.slider("Menu")
if st.sidebar.checkbox("Display the raw data") :
	st.subheader("Full Dataset")
	st.dataframe(census_df)
	st.write(f"The number of rows and columns are :{census_df.shape}")


st.set_option('deprecation.showPyplotGlobalUse', False)



st.subheader("Visualisation type")
vis_type = st.sidebar.multiselect('Select the chart or plot ',('Pie Chart','Count Plot','Boxplot'))

if 'Pie Chart' in vis_type  :
	plt.figure(figsize = (10,10))
	st.subheader('Pie Chart for income distribution')
	pie_data1,pie_data2 = census_df['income'].value_counts(),census_df['gender'].value_counts()
	plt.pie(pie_data1,labels = pie_data1.index,autopct = '%1.2f%%',startangle = 30)
	st.pyplot()
	st.subheader('Pie Chart for gender distribution')
	plt.pie(pie_data2,labels = pie_data2.index,autopct = '%1.2f%%',startangle = 30)
	st.pyplot()
	# st.pyplot()

if 'Boxplot' in vis_type  :
	plt.figure(figsize = (10,10))
	st.subheader("Boxplot for hours-per-week and income distribution")
	sns.boxplot(x = census_df["hours-per-week"],hue = census_df["income"],data = census_df)
	plt.ylabel("income")
	st.pyplot()
	st.subheader("Boxplot for hours-per-week and gender distribution")
	sns.boxplot(x = census_df["hours-per-week"],hue =census_df["gender"] ,data = census_df)
	plt.ylabel("Gender")
	st.pyplot()

if 'Count Plot' in vis_type:
	plt.figure(figsize = (10,10))
	st.subheader("countplot for unique workclass and income distribution ")
	sns.countplot(x = census_df['workclass'],hue = 'income',data = census_df)
	# sns.countplot(x = census_df['income'],data = census_df)
	plt.legend()
	st.pyplot()