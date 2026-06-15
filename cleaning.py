

import pandas as pd

df = pd.read_csv("nfhs1.csv")

df_clean = pd.DataFrame()

# Water
df_clean["Water"] = pd.to_numeric(
    df["Population living in households with an improved drinking-water source1 (%)"],
    errors="coerce"
)

# Sanitation
san_cols = [
    "Population living in households that use an improved sanitation facility2 (%)",
    "Households using clean fuel for cooking3 (%)"
]

for col in san_cols:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.extract(r'(\d+\.?\d*)')[0],
        errors="coerce"
    )

df_clean["Sanitation"] = df[san_cols].mean(axis=1)

# Electricity
df_clean["Electricity"] = pd.to_numeric(
    df["Population living in households with electricity (%)"],
    errors="coerce"
)

# Education
edu_cols = [
    "Female population age 6 years and above who ever attended school (%)",
    "Women (age 15-49) who are literate4 (%)",
    "Women (age 15-49)  with 10 or more years of schooling (%)"
]

for col in edu_cols:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.extract(r'(\d+\.?\d*)')[0],
        errors="coerce"
    )

df_clean["Education"] = df[edu_cols].mean(axis=1)

# Nutrition
# Nutrition
nut_cols = [
    "Total children age 6-23 months receiving an adequate diet16, 17  (%)",
    "Children under age 6 months exclusively breastfed16 (%)"
]

for col in nut_cols:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.extract(r'(\d+\.?\d*)')[0],
        errors="coerce"
    )

df_clean["Nutrition"] = df[nut_cols].mean(axis=1)


print(df_clean.head())

# df_clean.to_csv("readyy.csv", index=False)

