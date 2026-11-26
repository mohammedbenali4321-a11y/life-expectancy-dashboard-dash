# Life Expectancy Dashboard (`life-expectancy-dashboard-dash`)

An interactive data visualization web application built with **Python**, **Plotly Dash**, and **Pandas** to explore historical life expectancy trends across countries using the **Gapminder** dataset.

---

##  Overview

This project demonstrates how to build a reactive analytical dashboard from scratch using Dash components (`dash.html`, `dash.dcc`, and `dash.dash_table`). Users can select any country from a dropdown menu to dynamically update a life expectancy time-series chart while browsing, sorting, and filtering the underlying dataset side-by-side.

###  Key Features
* **Interactive Country Selection:** Dynamic `dcc.Dropdown` menu (defaulting to *Canada*) connected via Dash `@callback` decorators.
* **Real-Time Line Chart:** Interactive `px.line` visualization tracking life expectancy (`lifeExp`) over time (`year`).
* **Interactive Data Table:** Paginated `dash_table.DataTable` (`10` rows per page) with native column filtering (`filter_action="native"`) and sorting (`sort_action="native"`).
* **Progressive Layout Architecture:** Structured CSS Flexbox layout with styled containers separating controls, charts, and tabular data.

---

##  Tech Stack & Environment

* **Language:** Python 3.14
* **IDE:** PyCharm
* **Core Libraries:**
  * [Dash](https://dash.plotly.com/) (HTML components, Core Components, DataTable, Callbacks)
  * [Plotly Express](https://plotly.com/python/plotly-express/)
  * [Pandas](https://pandas.pydata.org/)

---

##  Project Structure

```text
life-expectancy-dashboard-dash/
├── gapminder_unfiltered.csv   # Source dataset (country, continent, year, lifeExp, pop, gdpPercap)
├── table  html.py             # Final consolidated dashboard script (Code 3 active)
├── table  html_2.py           # Progressive development iterations (Code 1, Code 2, Code 3)
└── README.md                  # Project documentation
```

### Evolution of Implementations
1. **Step 1 (Basic Prototype):** Title header, country dropdown, and reactive line chart.
2. **Step 2 (Styled Containers):** Nested outer (green) and inner (red) bordered containers with centered controls.
3. **Step 3 (Final Split-View Dashboard):** Side-by-side Flexbox layout combining the interactive line graph on the left and the filterable/sortable `DataTable` on the right.

---

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/life-expectancy-dashboard-dash.git
cd life-expectancy-dashboard-dash
```

### 2. Install Dependencies
```bash
pip install dash plotly pandas
```

### 3. Configure Dataset Path
Before running the script on a new machine, update the CSV file path in the Python script from the local Windows path to a relative path:
```python
df = pd.read_csv("gapminder_unfiltered.csv")
```

### 4. Run the Application
```bash
python "table  html.py"
```
Once running, open your browser and navigate to:
```text
http://127.0.0.1:8050/
```

---

## 🎓 Academic & Author Information

* **Project Name:** Create dash use python
* **Author:** Mohamed BEN ALI
* **Institution:** Cité des Métiers et des Compétences (CMC) Rabat-Salé-Kénitra (RSK)
* **Field of Study (Filière):** Digital & Artificial Intelligence (*Digital et Intelligence Artificielle*)
* **Specialty (Spécialité):** Artificial Intelligence & Data Analytics (*Technicien Spécialisé - 2nd Year*)
* **Professor:** Yassine
* **Creation Date:** November 25, 2026
* **Publication Date:** November 26, 2026
