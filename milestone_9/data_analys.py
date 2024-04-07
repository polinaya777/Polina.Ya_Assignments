import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("iris")

# Display the first few rows of the dataset and describe the dataset
print(data.head())
print(data.describe())

# ## Summary Statistics

# Calculate and print the mean of the 'petal_length' column
mean_petal_length = data['petal_length'].mean()
print(f"Mean petal length: {mean_petal_length}")

# Calculate and print the median of the 'petal_length' column
median_petal_length = data['petal_length'].median()
print(f"Median petal length: {median_petal_length}")

# Calculate and print the mode of the 'petal_length' column
mode_petal_length = data['petal_length'].mode()
print(f"Mode petal length: {mode_petal_length}")

# ## Data Visualization

# Plot a histogram of the 'petal_length' column
plt.figure(figsize=(10, 6))
sns.histplot(data['petal_length'], bins=20, kde=True)
plt.title('Distribution of Petal Lengths')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

# Plot a boxplot of the 'petal_length' column
plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='petal_length', data=data)
plt.title('Petal Lengths by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length')
plt.show()

# ## Conclusion

print("""The histogram shows that the distribution of petal lengths is approximately normal.
The boxplot shows that the petal lengths vary by species, with setosa having the shortest 
petals and virginica having the longest petals.""")