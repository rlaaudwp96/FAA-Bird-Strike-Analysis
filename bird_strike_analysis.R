# FAA Bird Strike Analysis: California vs. other U.S. states
# Primary R script for cleaning, grouping, and visualizing the data.

library(tidyverse)

birds <- read_csv("birds.csv", show_col_types = FALSE)

phase_summary <- birds |>
  filter(!is.na(phase_of_flt), !is.na(time_of_day), !is.na(state)) |>
  mutate(region = if_else(state == "CA", "California", "Other states")) |>
  count(region, phase_of_flt, sort = TRUE)

time_summary <- birds |>
  filter(!is.na(time_of_day), !is.na(state)) |>
  mutate(region = if_else(state == "CA", "California", "Other states")) |>
  count(region, time_of_day, sort = TRUE)

print(phase_summary)
print(time_summary)

ggplot(phase_summary, aes(x = reorder(phase_of_flt, n), y = n, fill = region)) +
  geom_col(position = "dodge") +
  coord_flip() +
  labs(title = "Bird strikes by flight phase", x = "Flight phase", y = "Collisions", fill = "Region") +
  theme_minimal()
