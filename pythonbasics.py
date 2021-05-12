"""
Datascience Cheat Sheet
There is also an accompanying png version
https://github.com/daniellewisDL/streamlit-cheat-sheet
v0.71.0 November 2020 Daniel Lewis and Austin Chen
"""

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
#     st.sidebar.code('$ pip install streamlit')
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
        background-color: #d6ffe8;
    }
    </style>
        """, unsafe_allow_html=True)
    # st.title("Data Science Cheat App")
    # type = ["Python Basics", "Pandas Basics", "Numpy Basics", "ML Algorithms"]
    # st.sidebar.markdown('Choose the cheat sheet to learn')
    # activity = st.sidebar.radio("Choose one from down", type)
    # if "Python Basics" in activity:
    st.subheader("Python Basics")
    col1, col2, col3 = st.beta_columns(3)

    col1.subheader('Variables and Data Types')
    col1.code('''# Variable Assignment `st.write()`
\'\'\' _This_ is some __Markdown__ \'\'\'
>>> x = 10
>>> x
5
    ''')

    # Display text

    col1.subheader('Calculation With Variables')
    col1.code('''
>> x+2      ------- Sum of two variable 
7
>>> x-2     ------- Subtraction of two variables 
3
>>> x*2     ------- Multiplication of two variables 
10
>>> x**2    ------- Exponentiation of a Variable 
25
>>> x%2     ------- Remainder of a Variable
1
>>> x/float(2) ------- Division of a variable
2.5
# * optional kwarg unsafe_allow_html = True
    ''')

    # Display data

    col1.subheader('Types and Type Conversion')
    col1.code('''
str()      '5', '3.45', 'True'     ------- Variables to strings 

int()       5, 3, 1                ------- Variables to integers

float()     5.0, 1.0               ------- Variables to floats

bool()      True, True, True       ------- Variables to booleans

    ''')

    # Display charts

    col1.subheader('String')
    col1.code('''
>>> my_string = 'thisStringIsAwesome'
>>> my_string
'thisStringIsAwesome'
    ''')

    # Display media

    col1.write('String Operations')
    col1.code('''
>>> my_string * 2
'thisStringIsAwesomethisStringIsAwesome' 
>>> my_string + 'Innit'
'thisStringIsAwesomeInnit' 
>>> 'm' in my_string
 True
    ''')

    col1.write('String Methods')
    col1.code('''
>>> my_string.upper()            ------- String to uppercase
>>> my_string.lower()            ------- String to lowercase
>>> my_string.count('w')         ------- Count String elements
>>> my_string.replace('e', 'i')  ------- Replace String elements
>>> my_string.strip()            ------- Strip whitespaces
        ''')

    # Display interactive widgets

    col2.subheader('Lists')
    col2.code('''
>> a = 'is'
>>> b = 'nice'
>>> my_list = ['my', 'list', a, b] 
>>> my_list2 = [[4,5,6,7], [3,4,5,6]]
    ''')
    col2.subheader('Selecting List Elements')
    col2.write('Subset')
    col2.code('''
>>> my_list[1]     ------- Select item at index 1 
>>> my_list[-3]    ------- Select 3rd last item
    ''')

    col2.write('Slice')
    col2.code('''
>>> my_list[1:3]   ------- Select items at index 1 and 2
>>> my_list[1:]    ------- Select items after index 0
>>> my_list[:3]    ------- Select items before index 3
>>> my_list[:]     ------- Copy my_list
    ''')

    col2.write('Subset List of Lists')
    col2.code('''
>>> my_list2[1][0]     ------- my_list[list][itemOfList]
>>> my_list2[1][:2]    
        ''')

    # Control flow

    col2.subheader('List Operations')
    col2.code('''
>>> my_list + my_list
['my', 'list', 'is', 'nice', 'my', 'list', 'is', 'nice'] 
>>> my_list * 2
['my', 'list', 'is', 'nice', 'my', 'list', 'is', 'nice'] 
>>> my_list2 > 4
True
    ''')

    # Lay out your app

    col2.subheader('List Methods')
    col2.code('''
>>> my_list.index(a)        ------- Get the index of an item
>>> my_list.count(a)        ------- Count an item
>>> my_list.append('!')     ------- Append an item at a time
>>> my_list.remove('!')     ------- Remove an item
>>> del(my_list[0:1])       ------- Remove an item
>>> my_list.reverse()       ------- Reverse the list
>>> my_list.extend('!')     ------- Append an item
>>> my_list.pop(-1)         ------- Remove an item
>>> my_list.insert(0,'!')   ------- Insert an item
>>> my_list.sort()          ------- Sort the list
    ''')



    # Libraries

    col3.subheader('Libraries')
    col3.write('Import Libraries')
    col3.code('''
>>> import numpy 
>>> import numpy as np
    ''')

    col3.write('Selective import')
    col3.code('''
>>> from math import pi
        ''')
    # Placeholders, help, and options

    col3.subheader('Numpy Arrays')
    col3.code('''
>>> my_list = [1, 2, 3, 4]
>>> my_array = np.array(my_list)
>>> my_2darray = np.array([[1,2,3],[4,5,6]])
    ''')

    # Mutate data
    col3.subheader('Selecting Numpy Array Elements')
    col3.write('Subset')
    col3.code('''
>>> my_array[1] 2       ------- Select item at index 1
    ''')
    col3.write('Slice')
    col3.code('''
>>> my_array[0:2]       ------- Select items at index 0 and 1
    array([1, 2])
        ''')

    col3.write('Subsets 2D Numpy Arrays')
    col3.code('''
>>> my_2darray[:,0]     ------- my_2darray[rows, columns]
    array([1, 4])
            ''')

    col3.subheader('Numpy Array Operations')
    col3.code('''
>>> my_array > 3
    array([False, False, False, True], dtype=bool) 
>>> my_array * 2
    array([2, 4, 6, 8])
>>> my_array + np.array([5, 6, 7, 8])
    array([6, 8, 10, 12])
    ''')

    # Optimize performance

    col3.subheader('Numpy Array Functions')
    col3.code('''
>>> my_array.shape              ------- Get the dimensions of the array
>>> np.append(other_array)      ------- Append items to an array   
>>> np.insert(my_array, 1, 5)   ------- Insert items in an array
>>> np.delete(my_array,[1])     ------- Delete items in an array
>>> np.mean(my_array)           ------- Mean of the array
>>> np.median(my_array)         ------- Median of the array
>>> my_array.corrcoef()         ------- Correlation coefficient
>>> np.std(my_array)            ------- Standard deviation
    ''')

    return None

# Run main()

if __name__ == '__main__':
    main()


