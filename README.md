# Historical Pittsburgh Crash Heat Map

This repository contains data and scripts for analyzing crash data in Pittsburgh.

![Sample Map Area](Sample%20Map%20Area.png)

---

<details>
<summary><strong>Folder: Allegheny County Crash Data</strong></summary>

This folder contains the bulk of my work, organized in the order I created them.

### 1. Crash Data Cleanup

- **Description**: Cleaned the PENNDOT crash data and extracted the relevant categories and values.
- **Libraries Used**:
  - `pandas`

---

### 2. Density Map

- **Description**: Using the cleaned crash data, created a density map with the **Folium** library.
- **Libraries Used**:
  - `pandas`
  - `branca`
  - `folium`

---

### 3. Time Series Crash Map

- **Description**: Applied a linear time series weight model to the density map to remove noise in the crash data.
- **Libraries Used**:
  - `matplotlib`
  - `numpy`
  - _(plus all libraries used previously)_

---

### Other Graphs

- **Description**: Exploratory analysis on possible crash-causing factors.  
  Each Python file will output a graph of some sort.

</details>

---

<details>
<summary><strong>Folder: Greater Pittsburgh Food Bank</strong></summary>

- **Data Source**: CSV file scraped from the Greater Pittsburgh Food Bank [distribution list](https://pittsburghfoodbank.org/get-involved/volunteer/distributions/).
- **Usage**: The merged map overlays the GPFB distribution locations on the crash density map (without time series calculations).

</details>

---

<details>
<summary><strong>Folder: Pittsburgh Street Centerline</strong></summary>

This folder contains the original files downloaded from the **City of Pittsburgh GIS Data Hub**:  
[GIS Dataset Link](https://pghgishub-pittsburghpa.opendata.arcgis.com/datasets/db12137760a64e86bc4ea74574c4dd30_0/explore?location=40.442481%2C-79.962726%2C13.01)

</details>

---

<details>
<summary><strong>Folder: West End Bridge Map</strong></summary>

This folder contains two OSM files representing the selected sample area: the stretch of the **West End Bridge** and its immediate surroundings.

The area was selected for analysis using **SUMO** and **TraCI** because of:

- **High historical crash density**
- **Simple road geometry** (only a few roads feeding in and out)
- **Length** (longer distances are easier to simulate)

</details>

---

## Installation

To install all required libraries, run:

```bash
pip install pandas folium branca matplotlib numpy
```
