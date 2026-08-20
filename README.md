# 🦅 FAA Aircraft Bird Strike Analysis: CA vs. Other States

## Business Problem & Overview
Bird strikes pose significant safety risks and financial costs to aviation safety. Understanding when and where these strikes occur—such as during specific flight phases or times of day—helps airports and flight operators optimize wildlife management and hazard mitigation protocols.

This project analyzes the **FAA Bird Strike Dataset** using **R** to evaluate collision frequencies across flight phases (`phase_of_flt`) and times of day (`time_of_day`), with a special comparative focus on **California (CA)** versus **other US states**.

---

## Key Results & Insights
* **Primary Collision Phase:** Across all regions, the majority of bird strikes occur during the **Approach** and **Landing** flight phases. This aligns with lower altitude and lower speed operations where bird density is highest.
* **Regional Distribution Differences:**
  * **California (CA):** Collision frequencies are relatively evenly spread across multiple flight phases compared to other regions.
  * **Other States:** Bird strikes are heavily concentrated specifically in the **Approach** phase.
* **Temporal Patterns:** In both California and other states, collisions predominantly occur during **Daytime** compared to Night, Dawn, or Dusk.

---

## Data & Feature Preprocessing
* **Dataset Source:** `openintro::birds` dataset containing historical FAA wildlife collision logs.
* **Data Cleaning:**
  1. Handled missing records (`NA`) across key categorical factors (`phase_of_flt`, `time_of_day`, `state`).
  2. Filtered and recoded geographical state categories into binary indicators (`CA` vs. `Other States`).
  3. Re-ordered factor levels based on frequency using `forcats` (`fct_infreq`, `fct_rev`) for clear visual reporting.

---

## 💻 Core R Code Snippets

### 1. Data Cleaning & Regional Classification
```R
library(tidyverse)
library(openintro)

# Cleaning and mapping region indicators
birds_CA <- birds %>%
  select(phase_of_flt, time_of_day, state) %>%
  na.omit() %>%
  filter(state == "CA") %>%
  mutate(
    phase_of_flt = as.factor(phase_of_flt),
    time_of_day = as.factor(time_of_day)
  )
```

### 2. Visualizing Collision Frequency by Flight Phase & Region
```R
library(gridExtra)

# Comparing California vs Other States
p1 <- ggplot(birds_CA, aes(x = fct_rev(fct_infreq(phase_of_flt)), fill = phase_of_flt)) +
  geom_bar(show.legend = FALSE) +
  coord_flip() +
  labs(title = "Frequency by Phase: CA", y = "Collision Frequency", x = "Phase of Flight")

p2 <- ggplot(birds_Otherst, aes(x = fct_rev(fct_infreq(phase_of_flt)), fill = phase_of_flt)) +
  geom_bar(show.legend = FALSE) +
  coord_flip() +
  labs(title = "Frequency by Phase: Other States", y = "Collision Frequency", x = "Phase of Flight")

grid.arrange(p1, p2, nrow = 1)
```

---

## 👥 Contributors
This project was conducted as part of our data analysis coursework:

* **Myungje Kim**
* **Jennifer Soper**
* **Gizem Ozyildirim**

---

## 📁 Project Structure
```text
├── birds.csv                # Raw bird strike dataset
├── Final_Project.qmd        # Quarto Markdown script with EDA & Visualizations
└── README.md                # Project documentation
```

---

## 🚀 How to Reproduce
1. **Clone this repository:**
   ```bash
   git clone [https://github.com/rlaaudwp96/FAA-Bird-Strike-Analysis.git](https://github.com/rlaaudwp96/FAA-Bird-Strike-Analysis.git)
   cd FAA-Bird-Strike-Analysis
   ```
2. **Open Project:** Open `Final_Project.qmd` in **RStudio**.
3. **Install Packages:** Run the following command in the R console:
   ```R
   install.packages(c("tidyverse", "openintro", "gridExtra"))
   ```
4. **Render Document:** Render the Quarto document to PDF or HTML to reproduce all comparative bar charts and distribution summaries.

---

## 🛠️ Tech Stack
* **Language:** R
* **Libraries:** `tidyverse` (`ggplot2`, `dplyr`, `forcats`), `openintro`, `gridExtra`
