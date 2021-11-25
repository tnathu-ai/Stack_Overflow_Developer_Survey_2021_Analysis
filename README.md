# Assignment 1: Data Exploration

This is submission for Assignment 1 for student **s3879312**

Analyzing the [Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey) Results 2021 dataset

**[Github repo for this Assignment](https://github.com/tnathu-ai/Stack_Overflow_Developer_Survey_2021_Analysis)**

# Analyzing the Stack Overflow Developer Survey Results 2021 dataset. The dataset contains three files:

- `README.txt` - Information about the dataset
- `survey_results_schema.csv` - The list of questions, and shortcodes for each question
- `survey_results_public.csv` - The full list of responses to the questions
- `assignment1.ipynb` - The main jupyter notebook you should run
- `assignment1.py` - The python file contains all functions I used
- `Dash` - The folder for Dash Web App
- `interactive_html` - The folder for opening each interactive Dash Visualization files in local browser

# Files to the Development Folder (Dash folder)

* `app.py`    a Dash application
* `.gitignore`    used by git, identifies files that won’t be pushed to production
* `Procfile`    used for deployment
* `requirements.txt`    describes your Python dependencies, can be created automatically

python version 3.8.8

# Option 1: WORKING ON YOUR LOCAL COMPUTER

1. Install Conda
   by [following these instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Add Conda
   binaries to your system `PATH`, so you can use the `conda` command on your terminal.

2. Install jupyter lab and jupyter notebook on your terminal

+ `pip install jupyter lab`
+ `pip install jupyter notebook`

### Jupyter Lab

1. Download the 3879312 zipped project folder. Unzip it by double-clicking on it.

2. In the terminal, navigate to the directory containing the project and install these packages and libraries

```
pip install pandas 

pip install scikit-learn 

pip install matplotlib 

pip install seaborn 

pip install statsmodel

pip install dash

pip install dash-auth

pip install dash-renderer

pip install dash-bootstrap-components

pip install cufflinks

pip install --upgrade pandas

pip install plotly==5.3.1 

pip install plotly --upgrade

pip install dash_daq 

pip install dash-html-components 

pip install dash_bootstrap_components 

pip install dash-core-components

pip install numpy

pip install WordCloud
```

3. Enter the newly created directory using `cd directory-name` and start the Jupyter Lab.

```
jupyter lab

```

You can now access Jupyter's web interface by clicking the link that shows up on the terminal or by
visiting http://localhost:8888 on your browser.

4. Click on assignment1.ipynb in the browser tab. This will open up my main file in the Jupyter Lab.

5. Follow the steps in the Jupyter Lab. If you get to Task 4, you can look at `dash_as1.ipynb` for better understanding
of **Visualization Dashboard** before running the web app on the local machine.

### Note: If the Jupyter Notebook is not responding due to many requests

Error [(The page is not responding)](https://stackoverflow.com/questions/48615535/jupyter-notebook-takes-forever-to-open-and-then-pages-unresponsive-mathjax-i)

I had to restart the notebook; and it did not work. This is because I was printing out too much and the following
scripts resolved the issue by clear out all the output to run through the whole kernal:

1. `conda install -c conda-forge nbstripout` or `pip install nbstripout`

2. `nbstripout filename.ipynb`


### Deploying Dash Web App on the local machine

1. Enter the newly created directory using `cd directory-name` and start the Web App.

2. First create a **virtual environment** with conda or venv inside a temp folder, then activate it.

```
virtualenv venv

# Windows
py -m venv .env
.env\Scripts\activate

# Or Linux
source venv/bin/activate

```

3. Run the app

```

python app.py

```


# Option 2: RUNNING USING ONLINE RESOURCES (1-click)

The easiest way to start executing this notebook is to click the "Run" button at the top of this page, and select "Run
on Binder". This will run the notebook on [mybinder.org](https://mybinder.org), a free online service for running
Jupyter notebooks. You can also select "Run on Colab" or "Run on Kaggle".

You can access my full version of jupyter notebook here: 
+ **Task 1:** https://plotly.com/~tnathu/17/assignment-1-data-exploration-this-is/
+ **Task 1.8:** https://plotly.com/~tnathu/18/assignment-1-data-exploration-this-is/
+ **Task 2:** https://plotly.com/~tnathu/19/assignment-1-data-exploration-this-is/
+ **Task 4:** https://plotly.com/~tnathu/20/task-4-visualisation-dashboard-this-is/



## Demo:

The following are screenshots for the app in this repo:

![img.png](compensation_women.png)

![img.png](compensation_men.png)

![img.png](participation_onl_dev.png)

![screenshot](comp_gender.png)




## Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver 



## Future improvement:
+ Labeling: For supervised learning, then I need to make sure that my labels are accurate. 

+ Feature space coverage: Ensure that my training dataset has examples that cover the same feature space as the request that my future model will receive. 

+ Minimal Dimensionality & Maximum predictive data: I also want to reduce the dimensionality of your feature vector to optimize my system performance while retaining or enhancing the predictive information on my data. 

+ Fairness:  I will need to consider and measure the fairness of my data and model, especially for rare conditions, for example, in this case, where gender inequality prerequisites may be critical to success. 
