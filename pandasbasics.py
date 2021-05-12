import streamlit as st
from pathlib import Path
import base64


# Initial page config

# st.set_page_config(
#      page_title='Datascience cheat sheet',
#      layout="wide",
#      initial_sidebar_state="expanded",
# )

def main():
    cs_sidebar()
    cs_body()

    return None


# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


# sidebar

def cs_sidebar():
    #
    #
    #     st.sidebar.markdown('Import convention')
    #     st.sidebar.code('>>> import streamlit as st')
    #
    #     st.sidebar.markdown('__Add widgets to sidebar__')
    #     st.sidebar.code('''
    # st.sidebar.<widget>
    # >>> a = st.sidebar.radio(\'R:\',[1,2])
    #     ''')
    #
    #     st.sidebar.markdown('__Command line__')
    #     st.sidebar.code('''
    # $ streamlit --help
    # $ streamlit run your_script.py
    # $ streamlit hello
    # $ streamlit config show
    # $ streamlit cache clear
    # $ streamlit docs
    # $ streamlit --version
    #     ''')
    #
    #     st.sidebar.markdown('__Pre-release features__')
    #     st.sidebar.markdown('[Beta and experimental features](https://docs.streamlit.io/en/0.70.0/api.html#beta-and-experimental-features)')
    #     st.sidebar.code('''
    # pip uninstall streamlit
    # pip install streamlit-nightly --upgrade
    #     ''')

    # st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://github.com/daniellewisDL/streamlit-cheat-sheet) <small>st.cheat_sheet v0.71.0 | Nov 2020</small>'''.format(img_to_bytes("brain.png")), unsafe_allow_html=True)

    return None


##########################
# Main body of cheat sheet
##########################
#
def cs_body():
    # Magic commands
    st.markdown("""
    <style>
    body {
        color: #00628B;
        background-color: #F5B7B1;
    }
    </style>
        """, unsafe_allow_html=True)
    # st.title("Data Science Cheat App")
    # type = ["Python Basics", "Pandas Basics", "Numpy Basics", "ML Algorithms"]
    # st.sidebar.markdown('Choose the cheat sheet to learn')
    # activity = st.sidebar.radio("Choose one from down", type)
    # if "Python Basics" in activity:
    st.subheader("Pandas Basics")
    col1, col2, col3 = st.beta_columns(3)

    col1.subheader('Pandas Data Structures')
    col1.write('Series')
    col1.code('''
A one-dimensional labeled array capable of holding any data type
>>> s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
    ''')

    # Display text

    col1.write('DataFrame')
    col1.code('''
>> data = {'Country': ['Belgium', 'India', 'Brazil'], 
            'Capital': ['Brussels', 'New Delhi', 'Brasília'],
                        'Population': [11190846, 1303171035, 207847528]}
>>> df = pd.DataFrame(data,
                columns=['Country', 'Capital', 'Population'])
    ''')

    # Display data

    col1.subheader('I/O')
    col1.write('Read and Write to CSV')
    col1.code('''
>>> pd.read_csv('file.csv', header=None, nrows=5) 
>>> df.to_csv('myDataFrame.csv')
    ''')

    # Display media

    col1.write('Read and Write to Excel')
    col1.code('''
>>> pd.read_excel('file.xlsx')
>>> pd.to_excel('dir/myDataFrame.xlsx', sheet_name='Sheet1')
///Read multiple sheets from the same file///
>>> xlsx = pd.ExcelFile('file.xls')
>>> df = pd.read_excel(xlsx, 'Sheet1')
    ''')

    # Display interactive widgets
    col1.subheader('Selection')
    col1.write('Getting')
    col1.code('''
>>> s['b'] -5                   ------ Get one element
>>> df[1:]                      ------ Get subset of a Dataframe
    Country Capital Population
    1 India New Delhi 1303171035
    2 Brazil Brasília 207847528
    ''')
    col2.write('By Position')
    col2.code('''
>>> df.iloc([0],[0]) 'Belgium' ------- Select single value by row & column
>>> df.iat([0],[0]) 'Belgium'
    ''')

    # Libraries

    col2.write('By Label')
    col2.code('''
>>> df.loc([0], ['Country']) 'Belgium' ------------- Select single value by row & column labels
>>> df.at([0], ['Country']) 'Belgium'

        ''')

    col2.write('By Label/Position')
    col2.code('''
>>> df.ix[2] Country Brazil      ------- Select single row of subset of rows
            Capital    Brasília
            Population  207847
>>> df.ix[:,'Capital']           ------- Select a single column of subset of columns
            0 Brussels
            1 New Delhi
            2 Brasília
>>> df.ix[1,'Capital']           ------- Select rows and columns
        'New Delhi'
            ''')
    # Placeholders, help, and options

    col2.write('Boolean Indexing')
    col2.code('''
>>> s[~(s > 1)]                     ------- Series s where value is not >1
                                            s where value is <-1 or >2
>>> s[(s < -1) | (s > 2)]             
>>> df[df['Population']>1200000000] ------- Set index a of Series s to 6
        ''')

    # Mutate data
    col2.write('Dropping')
    col2.code('''
>>> s.drop(['a', 'c'])         ------- Drop values from rows (axis=0)
>>> df.drop('Country', axis=1) ------- Drop values from columns(axis=1)
        ''')

    col2.write('Sort & Rank')
    col2.code('''
>>> df.sort_index()                     ------- Sort by labels along an axis
>>> df.sort_values(by='Country')        ------- Sort by the values along an axis
>>> df.rank()                           ------- Assign ranks to entries
    ''')
    col3.subheader('Retrieving Series/DataFrame Information')
    col3.write('Basic Information')
    col2.code('''
>>> df.shape   ------- (rows,columns) 
>>> df.index   ------- Describe index
>>> df.columns ------- Describe DataFrame columns
>>> df.info()  ------- Info on DataFrame
>>> df.count() ------- Number of non-NA values
    ''')

    col3.write('Summary')
    col3.code('''
>>> df.sum()                ------- Sum of values
>>> df.cumsum()             ------- Cummulative sum of values
>>> df.min()/df.max()       ------- Minimum/maximum values
>>> df.idxmin()/df.idxmax() ------- Minimum/Maximum index value
>>> df.describe()           ------- Summary statistics
>>> df.mean()               ------- Mean of values
>>> df.median()             ------- Median of values
        ''')

    # Control flow

    col3.subheader('Applying Functions')
    col3.code('''
>>> f = lambda x: x*2
>>> df.apply(f)    ------- Apply function
>>> df.applymap(f) ------- Apply function element-wise
    ''')

    # Lay out your app

    col3.subheader('Data Alignment')
    col3.write('Internal Data Alignment')
    col3.code('''
>>> s3 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])
>>> s + s3  
        a 10.0 
        b NaN 
        c 5.0 
        d 7.0
    ''')

    col3.write('Arithmetic Operations with Fill Methods')
    col3.code('''
 >>> s.add(s3, fill_value=0) a 10.0
b -5.0
c 5.0
d 7.0
>>> s.sub(s3, fill_value=2) 
>>> s.div(s3, fill_value=4) 
>>> s.mul(s3, fill_value=3)
        ''')

    return None


# Run main()

if __name__ == '__main__':
    main()