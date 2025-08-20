# Allegheny County Crash Data

This folder contains the bulk of my work, organized in the order I created them.

---

## 1. Crash Data Cleanup
- **Description**: Cleaned the PENNDOT crash data and extracted the relevant categories and values.  
- **Libraries Used**:  
  - `pandas`

---

## 2. Density Map
- **Description**: Using the cleaned crash data, created a density map with the **Folium** library.  
- **Libraries Used**:  
  - `pandas`  
  - `branca`  
  - `folium`

---

## 3. Time Series Crash Map
- **Description**: Applied a linear time series weight model to the density map to remove noise in the crash data.  
- **Libraries Used**:  
  - `matplotlib`  
  - `numpy`  
  - *(plus all libraries used previously)*

---

## Other Graphs
- **Description**: exploratory analysis on some possible crash causing factors, each python file will output a graph of some sort
---


## Installation

To install all required libraries, run:

```bash
pip install pandas folium branca matplotlib numpy
