import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- 1. The Physical Model ---
def primordial_vorticity_model(z, z_c):
    prob_aligned = 1 - np.exp(-((1 + z) / (1 + z_c))**2)
    return 0.5 + 0.5 * prob_aligned

# --- 2. The Observational Data with Errors ---
z_observed = np.array([3.0, 4.0, 5.0, 6.0])
sigma_observed = np.array([0.66, 0.74, 0.78, 0.81])
errors = np.array([0.03, 0.04, 0.04, 0.05]) # These errors are crucial for the test.

# --- 3. Perform a Rigorous Measurement of z_c using curve_fit ---
initial_guess = [4.0] 
popt, pcov = curve_fit(primordial_vorticity_model, z_observed, sigma_observed, p0=initial_guess, sigma=errors)
z_c_measured = popt[0]
z_c_uncertainty = np.sqrt(np.diag(pcov))[0]

# --- 4. Test the Model and Calculate Goodness of Fit ---
sigma_predicted = primordial_vorticity_model(z_observed, z_c_measured)

# Calculate the Chi-Squared statistic
residuals = sigma_observed - sigma_predicted
chi_squared = np.sum((residuals / errors)**2)

# Calculate the degrees of freedom (dof)
# dof = (Number of data points) - (Number of fitted parameters)
dof = len(z_observed) - 1 

# Calculate the Reduced Chi-Squared
reduced_chi_squared = chi_squared / dof


# --- 5. Print the New, Scientific Comparison ---
print("="*75)
print("--- Primordial Vorticity Model: Statistical Goodness of Fit Test ---")
print(f"\nMeasured Parameter from Data: z_c = {z_c_measured:.2f} ± {z_c_uncertainty:.2f}\n")
print(f"{'Redshift (z)':<15} {'JWST Observed':<20} {'Model Prediction':<20} {'Difference':<15}")
print("-" * 70)
for i in range(len(z_observed)):
    diff = sigma_observed[i] - sigma_predicted[i]
    print(f"{z_observed[i]:<15.1f} {sigma_observed[i]:<20.2f} {sigma_predicted[i]:<20.3f} {diff:<15.3f}")
print("-" * 70)

# Print the objective statistical results
print("\n--- Statistical Validation ---")
print(f"Chi-Squared (χ²): {chi_squared:.3f}")
print(f"Degrees of Freedom (dof): {dof}")
print(f"Reduced Chi-Squared (χ²/dof): {reduced_chi_squared:.3f}")

# Interpret the result based on the standard statistical rule
if 0.5 <= reduced_chi_squared <= 1.5:
    print("--> Verdict: ✅ Excellent. The model is statistically consistent with the data.")
elif reduced_chi_squared < 0.5:
    print("--> Verdict: 🟡 The model fits the data surprisingly well (errors might be overestimated).")
else:
    print("--> Verdict: ❌ Poor Fit. The model is not statistically consistent with the data.")
print("="*75)


# --- 6. Visualization ---
# The plot remains the same, but our interpretation of it is now backed by statistics.
z_smooth = np.linspace(2, 9, 200)
sigma_smooth = primordial_vorticity_model(z_smooth, z_c_measured)

plt.figure(figsize=(10, 7))
plt.errorbar(z_observed, sigma_observed, yerr=errors, fmt='o', color='red', capsize=5, 
             markersize=8, label=f'JWST Observations with Errors', zorder=5)
plt.plot(z_smooth, sigma_smooth, color='green', linewidth=2, 
         label=f'PVF Model with Best-Fit z_c ≈ {z_c_measured:.2f}')
plt.title('B-Space: Statistical Test of the PVF Model vs. JWST Data')
plt.xlabel('Redshift (z)')
plt.ylabel('Galaxy Spin Alignment Fraction (σ_align)')
plt.xlim(2, 9)
plt.ylim(0.5, 1.0)
plt.grid(True, linestyle=':')
plt.legend(loc='lower right')
plt.show()