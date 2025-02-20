# 📊 Statistics for Data Science – Complete Notes  

### 📝 Author: Shivam Mishra  
📌 [GitHub](https://github.com/Shivam30Mishra) | [LinkedIn](https://www.linkedin.com/in/shivam-mishra-777026280/)  

---

## 📌 Study Log  

| **Date**       | **Time**    | **Topics Covered** |
|---------------|-----------|--------------------|
| **Feb 20, 2025** | **10:00 AM - 11:30 AM** | Population Mean, Sample Mean |
| **Feb 20, 2025** | **2:00 PM - 3:30 PM**  | Discrete & Continuous Random Variables |
| **Feb 20, 2025** | **6:00 PM - 7:30 PM**  | Gaussian Distribution |

---

## 📌 1. Population Mean vs. Sample Mean  

### **📍 Definition**  
- **Population Mean (μ)**: The average of all data points in a dataset.  
- **Sample Mean (x̄)**: The average of a subset taken from the population.  

### **📍 Formula**  
\[
\mu = \frac{\sum X}{N}
\]
\[
\bar{x} = \frac{\sum X}{n}
\]
where **N** is the total population size, and **n** is the sample size.  

### **📍 Real-Life Example**  
- **Population Mean**: The average salary of **all employees** in India.  
- **Sample Mean**: The average salary of **100 randomly selected employees**.  

---

## 📌 2. Discrete vs. Continuous Random Variables  

### **📍 Definition**  
- **Discrete Random Variable**: Can take only specific, countable values (e.g., Number of students in a class).  
- **Continuous Random Variable**: Can take any value within a range (e.g., Height of a person).  

### **📍 Real-Life Example**  
| **Scenario** | **Type** |
|-------------|---------|
| Number of bank accounts a person has | Discrete |
| Height of a person | Continuous |
| Number of mobile phones owned | Discrete |
| Temperature outside | Continuous |

---

## 📌 3. Gaussian (Normal) Distribution  

### **📍 Definition**  
- The **Gaussian distribution** (Normal Distribution) is a symmetric probability distribution around the mean.  
- The **mean, median, and mode are equal**.  
- **The 68-95-99.7 Rule**:  
  - **68%** of data falls within **1 standard deviation (σ)**.  
  - **95%** falls within **2σ**.  
  - **99.7%** falls within **3σ**.  

### **📍 Formula**  
\[
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
\]
where **μ** is mean and **σ** is standard deviation.  

### **📍 Real-Life Example**  
- Heights of people follow **normal distribution**.  
- Exam scores often follow a **bell curve**.  

---

## 📝 Questions & Answers  

### ❓ **1. What is the key difference between population mean and sample mean?**  
✅ **Answer:**  
- **Population mean (μ):** The mean of an entire dataset.  
- **Sample mean (x̄):** The mean of a randomly selected subset of the population.  

---

### ❓ **2. Why do we use sample mean instead of population mean in real life?**  
✅ **Answer:**  
- **Collecting population data is impractical** (large, costly, and time-consuming).  
- **Sample mean provides a good estimate** of the population mean with **less effort**.  

---

### ❓ **3. Identify whether the following are discrete or continuous random variables:**  
**a) Number of bank accounts a person has**  
**b) Height of a person**  

✅ **Answer:**  
- **Number of bank accounts** → **Discrete Random Variable** (countable whole numbers).  
- **Height of a person** → **Continuous Random Variable** (varies within a range).  

---

### ❓ **4. Is age a discrete or continuous random variable?**  
✅ **Answer:** **Continuous Random Variable.**  
- Although we measure age in whole numbers (e.g., 20 years), the actual value can be **20.5, 20.75, etc.**  

---

### ❓ **5. If we take multiple random samples from a dataset, how would their means compare?**  
✅ **Answer:**  
- The means would be **approximately equal** but may have slight variations.  
- **Central Limit Theorem (CLT)** states that sample means follow a **normal distribution**.  

---

## 📌 Applications in Data Science  

### **📍 Population vs. Sample Mean in Data Science**  
- Used in **data preprocessing** to normalize features (feature scaling).  
- Sample mean helps in **estimating population trends** without analyzing the full dataset.  
- **Example:** Finding the **average customer spending** in an e-commerce platform.  

### **📍 Discrete vs. Continuous Variables in Machine Learning**  
- **Discrete variables** are useful in **classification problems** (e.g., predicting customer churn based on number of transactions).  
- **Continuous variables** are used in **regression models** (e.g., predicting house prices based on area size).  

### **📍 Gaussian Distribution in Machine Learning**  
- Many machine learning algorithms assume **normal distribution** (e.g., Linear Regression, Naive Bayes).  
- Standardization of features is often done using **Z-score normalization** based on Gaussian distribution.  

---

## 🛠️ Code Examples  

### **📌 Calculate Sample & Population Mean in Python**
```python
import numpy as np

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Population Mean
population_mean = np.mean(data)

# Sample Mean (Taking a random subset)
sample = np.random.choice(data, size=5, replace=False)
sample_mean = np.mean(sample)

print("Population Mean:", population_mean)
print("Sample Mean:", sample_mean)
