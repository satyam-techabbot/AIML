# Exploratory Data Analysis

Process of examining or understanding the data and extracting insights dataset to identify patterns or main characteristics of the data. 

EDA is generally classified into two methods, i.e. graphical analysis and non-graphical analysis.


## Basic opertions to do
- Structure check
- Missing values
- Duplicates
- Summary statistics
- Univariate analysis
- Bivariate analysis
- Correlation check
- Outlier detection
- Skewness check
- Feature insights

## How to Extract Useful Insights in Data Analysis (EDA Guide)

### 1️⃣ Understand the Business Question First

Before touching code, ask:
* What problem are we solving?
* What decision could this analysis influence?
* Who is the stakeholder?

In a shopping dataset, typical business questions:
* What drives revenue?
* Which customers are most valuable?
* What factors influence spending?
* Are discounts effective?
* Are there seasonal trends?


### 2️⃣ Types of Relationships to Explore

#### A) Numeric vs Numeric

Use:

* Correlation
* Scatterplots
* Regression

Example:
* Purchase Amount vs Rating
* Age vs Spending

⚠️ If correlation ≈ 0 → move on.

---

#### B) Categorical vs Numeric (VERY POWERFUL)

Use:
* Groupby mean
* Boxplot
* Barplot

Example:
* Category vs Purchase Amount
* Gender vs Spending
* Season vs Revenue

This is where most business insights come from.

Example code pattern:

```
df.groupby("Category")["Purchase Amount (USD)"].mean().sort_values(ascending=False)
```

This answers:
> “Which category generates highest spending?”

---

#### C) Categorical vs Categorical

Use:
* Crosstab
* Percentage distribution
* Heatmaps

Example:
```
pd.crosstab(df["Gender"], df["Category"], normalize="index") * 100
```

This answers:
> “What do males vs females prefer?”

---

### 3️⃣ Always Compare Averages AND Totals
Both matter.

Example:
```
# Average purchase
df.groupby("Category")["Purchase Amount (USD)"].mean()

# Total revenue
df.groupby("Category")["Purchase Amount (USD)"].sum()
```

Why?
* High average ≠ high revenue
* High revenue might come from volume

---

### 4️⃣ Segment the Data (VERY IMPORTANT)
Raw variables often show weak correlation.

Instead, create segments:
#### Age Groups
```python
pd.cut()
```

#### Spending Quartiles
```python
pd.qcut()
```

#### High vs Low Customers

```python
df["High Spender"] = df["Purchase Amount (USD)"] > df["Purchase Amount (USD)"].median()
```
Segmented analysis reveals hidden patterns.

---

### 5️⃣ Look for Business Levers

Ask:

* Does discount increase spending?
* Does subscription status affect frequency?
* Do repeat customers spend more?

Example:

```python
df.groupby("Discount Applied")["Purchase Amount (USD)"].mean()
```

This gives actionable insight.

---

### 6️⃣ Check Distribution, Not Just Means

Use:
* Histogram
* Boxplot
* Violinplot

Sometimes:
* Means are similar
* But variability is different

Outliers can also tell a story.

---

### 7️⃣ Don’t Overtrust Correlation

Your heatmap showed near-zero correlations.
That does NOT mean:
> “There are no insights.”

It means:
> “Relationships are not linear numeric ones.”

Retail data is usually:
* Behavioral
* Segment-based
* Categorical-heavy

---

### 8️⃣ How to Turn Findings into Insights
Bad statement:
> “The correlation is 0.031.”

Good insight:
> “Customer satisfaction appears independent of transaction size, suggesting that spending more does not guarantee higher ratings.”

Always interpret.

---

### 9️⃣ What Makes an Insight Strong?

A strong insight is:
✔ Relevant
✔ Clear
✔ Quantified
✔ Actionable

Example:
Weak:
> “Males buy more footwear.”

Strong:
> “Males spend 23% more on Footwear than females, indicating a potential opportunity for targeted promotions.”

---

### 🔟 Common EDA Mistakes

❌ Making too many random plots
❌ Reporting statistics without interpretation
❌ Ignoring business meaning
❌ Only focusing on correlation
❌ Not checking distributions

---

### 🧠 Professional EDA Workflow

1. Data cleaning
2. Univariate analysis (single variable)
3. Bivariate analysis (relationships)
4. Segmentation
5. Business interpretation
6. Summary insights


