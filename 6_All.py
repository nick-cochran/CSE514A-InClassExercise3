import numpy as np
import pandas as pd

h_data = pd.read_csv(r"C:\Users\Ben Dizdar\Downloads\hSamples.csv", header=None)
m_data = pd.read_csv(r"C:\Users\Ben Dizdar\Downloads\mSamples.csv", header=None)
# Need to change file paths above ^ 
test_sample = [3, 4, 4, 6, 2, 3, 7, 7, 2, 7, 5, 11, 3, 8, 3, 10]

total_samples = len(h_data) + len(m_data)
p_H = len(h_data) / total_samples
p_M = len(m_data) / total_samples

print(f"P(H) = {p_H}")
print(f"P(M) = {p_M}")

mean_h = h_data.mean(numeric_only=True)
std_h = h_data.std(numeric_only=True)
mean_m = m_data.mean(numeric_only=True)
std_m = m_data.std(numeric_only=True)

print("\nFeature Means for H:")
for i, mean in enumerate(mean_h, 1):
    print(f"Mean of feature {i} for H is: {mean}")

print("\nFeature Means for M:")
for i, mean in enumerate(mean_m, 1):
    print(f"Mean of feature {i} for M is: {mean}")

# Display feature standard deviations for each class
print("\nFeature Standard Deviations for H:")
for i, std in enumerate(std_h, 1):
    print(f"Standard deviation of feature {i} for H is: {std}")

print("\nFeature Standard Deviations for M:")
for i, std in enumerate(std_m, 1):
    print(f"Standard deviation of feature {i} for M is: {std}")

# Part 3: Calculate P(feature = x | class = H) and P(feature = x | class = M) for each feature in the test sample
def gaussian_pdf(x, mean, std):
    return (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))

# Initialize likelihood products
likelihood_h = 1
likelihood_m = 1

# Calculate the product of likelihoods for each feature in the test sample
print("\nFeature Likelihoods for test sample:")
for i, x in enumerate(test_sample):
    p_x_given_h = gaussian_pdf(x, mean_h.iloc[i], std_h.iloc[i])
    p_x_given_m = gaussian_pdf(x, mean_m.iloc[i], std_m.iloc[i])
    likelihood_h *= p_x_given_h
    likelihood_m *= p_x_given_m
    print(f"P(feature{i+1} = {x} | class = H) = {p_x_given_h}")
    print(f"P(feature{i+1} = {x} | class = M) = {p_x_given_m}")
    print()

# Calculate proportional probabilities for H and M
proportional_h = likelihood_h * p_H
proportional_m = likelihood_m * p_M

# Make a final prediction based on the higher proportional probability
if proportional_h > proportional_m:
    prediction = "H"
else:
    prediction = "M"

# Output the results
print("Proportional Probability for class H:", proportional_h)
print("Proportional Probability for class M:", proportional_m)
print("Final Prediction:", prediction)
