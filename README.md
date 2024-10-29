# Medical-Data-Visualizer
Medical Data Visualizer project for Freecodecamp certificate

Data description
The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

Instructions
By each number in the medical_data_visualizer.py file, add the code from the associated instruction number below.

Import the data from medical_examination.csv and assign it to the df variable
Create the overweight column in the df variable
Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
Draw the Categorical Plot in the draw_cat_plot function
Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import : sns.catplot()
Get the figure for the output and store it in the fig variable
Do not modify the next two lines
Draw the Heat Map in the draw_heat_map function
Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
height is more than the 97.5th percentile
weight is less than the 2.5th percentile
weight is more than the 97.5th percentile
Calculate the correlation matrix and store it in the corr variable
Generate a mask for the upper triangle and store it in the mask variable
Set up the matplotlib figure
Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap()
Do not modify the next two lines
