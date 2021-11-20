# import libraries general libraries
import pandas as pd
import numpy as np

# Modules for data visualization
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot, \
    plot  # iplot() = plots the figure(fig) that is created by data and layout
import plotly.express as px

pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)

plt.rcParams['figure.figsize'] = [6, 6]

# ignore DeprecationWarning Eror Messages
import warnings

warnings.filterwarnings('ignore')


# style: https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.background_gradient.html
# color: https://matplotlib.org/stable/tutorials/colors/colormaps.html
def style(table):
    """
    quick styling
    """
    view = table.style.background_gradient(cmap='Pastel1')
    return view


def percentage(s):
    """
    Converts a series to round off - percentage string format.
    """
    x = s.apply(lambda x: round(x / s[:].sum() * 100, 2))
    x = x.apply(lambda x: str(x) + '%')
    return x


def query_this(col, look):
    """
    Easy == Query
    """
    query_to_return = survey_public.query('{} == "{}"'.format(col, look))
    return query_to_return


def missing_bar(df) -> go.Figure:
    """Plots Missing Data for Whole Dataset."""
    title = 'Stack Overflow Developer Survey Results 2021 <b>Missing Data by Features</b>'

    # counts missing data
    missing_data = df.isna().sum()
    missing_data = missing_data.to_frame().reset_index().rename(
        columns={'index': 'data_cols', 0: 'counts'})
    missing_data = missing_data.sort_values(by='counts', ascending=False)
    missing_perc = np.round(
        (df.isna().sum().sum() / df.size) * 100, 2)

    # figure colors
    colors = ['#f2f0eb'] * len(missing_data)
    colors[:10] = ['pink']

    # create figure
    fig = go.Figure()
    for labels, values \
            in zip(missing_data.data_cols.to_list(), missing_data.counts):
        fig.add_trace(go.Bar(
            y=[labels],
            x=[values],
            name=labels,
            orientation='h'))

    # tweak layout
    fig.update_traces(marker_color=colors)
    fig.update_xaxes(title='Missing Counts')
    fig.update_yaxes(title='Features', tickmode='linear')

    fig.add_annotation(xref='paper', yref='paper',
                       x=0.71, y=0.70, text=f"""
            {missing_perc}%""",
                       font={'size': 20, 'color': 'White'},
                       showarrow=False)

    fig.add_annotation(xref='paper', yref='paper',
                       x=0.68, y=0.67, text=f"""Missing""",
                       font={'size': 15, 'color': 'gray'},
                       showarrow=False)

    add_bubble(fig)

    return paste_px_format(
        fig, title=title, height=1000, showlegend=False)


def missing_percentage(df):
    for col in df.columns:
        missing_percentage = df[col].isnull().mean()
        print(f'{col} - {missing_percentage :.1%}')


# Describing data
def group_median_aggregation(df, group_var, agg_var):
    # Grouping the data and taking median
    grouped_df = df.groupby([group_var])[agg_var].median().sort_values(ascending=False)
    return grouped_df


# Create the scatter plot
def scatter_plot(df):
    sns.lmplot(x="YearsCode", y="CompTotal", data=df)
    # Remove excess chart lines and ticks for a nicer looking plot
    sns.despine()


def split_multicolumn(col_series):
    result_df = col_series.to_frame()
    options = []
    # Iterate over the column
    for idx, value in col_series[col_series.notnull()].iteritems():
        # Break each value into list of options
        for option in value.split(';'):
            # Add the option as a column to result
            if not option in result_df.columns:
                options.append(option)
                result_df[option] = False
            # Mark the value in the option column as True
            result_df.at[idx, option] = True
    return result_df[options]


# function that imputes median
def impute_median(series):
    return series.fillna(series.median())


def calculate_min_max_whisker(df):
    """
    Calculates the values of the 25th and 75th percentiles
    It takes the difference between the two to get the interquartile range (IQR).
    Get the length of the whiskers by multiplying the IQR by 1.5
    Calculate the min and max whisker value by subtracting
    Add the whisker length from the 25th and 75th percentile values.
    """
    q_df = df.quantile([.25, .75])
    q_df.loc['iqr'] = q_df.loc[0.75] - q_df.loc[0.25]
    q_df.loc['whisker_length'] = 1.5 * q_df.loc['iqr']
    q_df.loc['max_whisker'] = q_df.loc['whisker_length'] + q_df.loc[0.75]
    q_df.loc['min_whisker'] = q_df.loc[0.25] - q_df.loc['whisker_length']
    return q_df


# credit: https://www.kaggle.com/jaepin
# Visualization to check % of missing values in each column
def paste_px_format(figure, **kwargs):
    """Updates Layout of the Figure with custom setting"""
    return figure.update_layout(**kwargs,
                                font={'color': 'Gray', 'size': 10},
                                width=780, margin={'pad': 10})


def add_bubble(fig, **kwargs):
    """Creates shape ontop of the figure"""
    return fig.add_shape(
        type="circle",
        line_color="white",
        fillcolor="pink",
        opacity=0.6,
        xref='paper', yref='paper',
        x0=0.5, y0=0.6)


def whitespace_remover(df):
    """
    The function will remove extra leading and trailing whitespace from the data.
    Takes the data frame as a parameter and checks the data type of each column.
    If the column's datatype is 'Object.', apply strip function; else, it does nothing.
    Use the whitespace_remover() process on the data frame, which successfully removes the extra whitespace from the columns.
    https://www.geeksforgeeks.org/pandas-strip-whitespace-from-entire-dataframe/
    """
    # iterating over the columns
    for i in df.columns:

        # checking datatype of each columns
        if df[i].dtype == 'str':

            # applying strip function on column
            df[i] = df[i].map(str.strip)
        else:
            # if condition is False then it will do nothing.
            pass

    def confusion_matrix(data, actual_values, model):
        """
            Confusion matrix

            Parameters
            ----------
            data: data frame or array
            data is a data frame formatted in the same way as your input data (without the actual values)
            e.g. const, var1, var2, etc. Order is essential!
            actual_values: data frame or array
            These are the actual values from the test_data
            In the case of logistic regression, it should be a single column with 0s and 1s

            model: a LogitResults object
            this is the variable where you have the fitted model
            , e.g., results_log in this course
            ----------

            Predict the values using the Logit model
        """
        pred_values = model.predict(data)
        # Specify the bins
        bins = np.array([0, 0.5, 1])
        # Create a histogram, where if values are between 0 and 0.5 tell will be considered 0
        # if they are between 0.5 and 1, they will be considered 1
        cm = np.histogram2d(actual_values, pred_values, bins=bins)[0]
        # Calculate the accuracy
        accuracy = (cm[0, 0] + cm[1, 1]) / cm.sum()
        # Return the confusion matrix and the accuracy
        return cm, accuracy
