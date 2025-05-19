# Healthcare Appointment No-Show Analysis
# Step-by-step implementation with clean comments

# Step 1: Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the dataset
df = pd.read_csv('sample_data.csv')
print("Top 5 rows:")
print(df.head())

# Step 3: Check missing values and data types
print("\nMissing values:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)

# Step 4: Convert date columns to datetime format
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Step 5: Extract weekday from AppointmentDay
df['AppointmentWeekday'] = df['AppointmentDay'].dt.day_name()

# Step 6: No-show statistics
print("\nNo-show value counts:\n", df['No-show'].value_counts())
no_show_rate = df['No-show'].value_counts(normalize=True) * 100
print("\nNo-show rate in %:\n", no_show_rate)

# Step 7: Analyze by gender
gender_show = df.groupby(['Gender', 'No-show']).size().unstack()
gender_show_percent = gender_show.div(gender_show.sum(axis=1), axis=0) * 100
print("\nGender-wise No-show %:\n", gender_show_percent)

# Step 8: Visualization - No-show by gender
sns.barplot(x=gender_show_percent.index, y=gender_show_percent['Yes'])
plt.title('No-show % by Gender')
plt.ylabel('No-show %')
plt.show()

# Step 9: Analyze impact of SMS reminders
sms_show = df.groupby(['SMS_received', 'No-show']).size().unstack()
sms_show_percent = sms_show.div(sms_show.sum(axis=1), axis=0) * 100
print("\nSMS-wise No-show %:\n", sms_show_percent)

# Step 10: Age group analysis
bins = [0, 12, 18, 35, 60, 100]
labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

age_show = df.groupby(['AgeGroup', 'No-show']).size().unstack()
age_show_percent = age_show.div(age_show.sum(axis=1), axis=0) * 100
print("\nAge Group-wise No-show %:\n", age_show_percent)

# Step 11: Visualization - No-show by age group
age_show_percent.plot(kind='bar', stacked=True)
plt.title('No-show % by Age Group')
plt.ylabel('Percentage')
plt.show()
