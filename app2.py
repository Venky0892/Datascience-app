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
        background-color: #D6EAF8;
    }
    </style>
        """, unsafe_allow_html=True)
    # st.title("Data Science Cheat App")
    # type = ["Python Basics", "Pandas Basics", "Numpy Basics", "ML Algorithms"]
    # st.sidebar.markdown('Choose the cheat sheet to learn')
    # activity = st.sidebar.radio("Choose one from down", type)
    # if "Python Basics" in activity:
    st.subheader("Numpy Basics")
    col1, col2, col3 = st.beta_columns(3)

    col1.subheader('Creating Arrays')
    col1.code('''
 
>>> a = np.array([1,2,3])
>>> b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
>>> c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],
dtype = float)
    ''')

    # Display text

    col1.subheader('Initial Placeholders')
    col1.code('''
>>> np.zeros((3,4))        ------- Create an array of zeros
>>> np.ones((2,3,4),dtype=np.int16) ------- Create an array of ones
>>> d = np.arange(10,25,5) ------- Create an array of evenly
>>> np.linspace(0,2,9) ------- Create an array of evenly spaced values (number of samples)
>>> e = np.full((2,2),7) ------- Create a constant array
>>> f = np.eye(2) ------- Create a 2X2 identity matrix
>>> np.random.random((2,2)) ------- Create an array with random values
>>> np.empty((3,2)) ------- Create an empty array
    ''')

    # Display data

    col1.subheader('I/O')
    col1.write('saving & Loading On Disk')
    col1.code('''
>>> np.save('my_array', a)
>>> np.savez('array.npz', a, b) 
>>> np.load('my_array.npy')
 
    ''')

    # Display media

    col1.write('Saving & Loading Text Files')
    col1.code('''
>>> np.loadtxt("myfile.txt")
>>> np.genfromtxt("my_file.csv", delimiter=',') 
>>> np.savetxt("myarray.txt", a, delimiter=" ")
    ''')

    # Display interactive widgets
    col1.subheader('Data Types')
    col1.code('''
>>> np.int64    ------- Signed 64-bit integer types
>>> np.float32  ------- Standard double-precision floating point
>>> np.complex  ------- Complex numbers represented by 128 floats
>>> np.bool     ------- Boolean type storing TRUE and FALSE values
>>> np.object   ------- Python object type
>>> np.string_  ------- Fixed-length string type
>>> np.unicode_ ------- Fixed-length unicode type
    ''')
    col1.subheader('Inspecting Your Array')
    col1.code('''
>>> a.shape     ------- Array dimensions
>>> len(a)      ------- Length of array
>>> b.ndim      ------- Number of array dimensions
>>> e.size      ------- Number of array elements
>>> b.dtype     ------- Data type of array elements
>>> b.dtype.name ------- Name of data type
>>> b.astype(int) ------- Convert an array to a different type
    ''')

    # Libraries

    col1.subheader('Subsetting, Slicing, Indexing')
    col1.write('Subsetting')
    col1.code('''
    >>> a[2] 1 2 3  ------- Select the element at the 2nd index
        3
    >>> b[1,2]      ------- Select the element at row 1 column 2 
        1.5 2 3 6.0         ( equivalent to b[1][2])

        ''')

    col2.write('Slicing')
    col2.code('''
    >>> a[0:2]                  ------- Select items at index 0 and 1
        array([1, 2])
    >>> b[0:2,1]                ------- Select items at rows 0 and 1 in column 1
        array([ 2., 5.])
    >>> b[:1]                   ------- Select all items at row 0 (equivalent to b[0:1, :])
        array([[1.5, 2., 3.]])
    >>> c[1,...]                ------- Same as [1,:,:]
        array([[[3., 2., 1.],
        [4., 5., 6.]]])
    >>> a[ : :-1]               ------- Reversed array a
        array([3, 2, 1])
            ''')
    # Placeholders, help, and options

    col2.write('Boolean Indexing')
    col2.code('''
    >>> a[a<2] array([1])   ------- Select elements from a less than 2
        ''')

    # Mutate data
    col2.write('Fancy Indexing')
    col2.code('''
    >>> b[[1, 0, 1, 0],[0, 1, 2, 0]]            ------- Select elements (1,0),(0,1),(1,2) and (0,0)
        array([4.,2.,6.,1.5])
    >>> b[[1, 0, 1, 0]][:,[0,1,2,0]]            -------- Select a subset of the matrix’s rows and columns
        array([[4.,5.,6.,4.], [1.5,2.,3.,1.5], 
        [4.,5.,6.,4.], [1.5,2.,3.,1.5]])
        ''')


    col2.subheader('Array Mathematics')
    col2.write('Arithmetic Operations')
    col2.code('''
>>> g = a - b 
        array([[-0.5, 0. , 0. ],       ------- Subtraction
        [-3. , -3. , -3. ]])
>>> np.subtract(a,b)                   ------- Subtraction
>>> b + a                              ------- Addition
    array([[ 2.5, 4. , 6. ],
        [ 5. , 7. , 9. ]])
>>> np.add(b,a)                        ------- Addition
>>> a / b                              ------- Division
    array([[ 0.66666667, 1.
        , 1. ], , 0.5 ]])
>>> a * b                              ------- Multiplication
    array([[ 1.5, 4. , 9. ],
        [ 4. , 10. , 18. ]])
>>> np.multiply(a,b)                   ------- Multiplication
>>> np.exp(b)                          ------- Exponentiation
>>> np.sqrt(b)                         ------- Square root
>>> np.sin(a)                          ------- Print sines of an Array
>>> np.cos(b)                          ------- Element-wise cosine
>>> np.log(a)                          ------- Element-wise natural logarithm
>>> e.dot(f)                           ------- Dot product
array([[ 7., 7.], [ 7., 7.]])
    ''')

    col2.write('Comparison')
    col2.code('''
>> a == b
    array([[False, True, True],             ------- Element-wise comparison
    [False, False, False]], dtype=bool) 
>>> a < 2                                   ------- Element-wise comparison
    array([True, False, False], dtype=bool) 
>>> np.array_equal(a, b)                    ------- Array-wise comparison
    ''')

    col3.write('Aggregate Functions')
    col3.code('''
>>> a.sum()           ------- Array-wise sum
>>> a.min()           ------- Array-wise minimum value
>>> b.max(axis=0)     ------- Maximum value of an array row
>>> b.cumsum(axis=1)  ------- Cumulative sum of the elements
>>> a.mean()          ------- Mean
>>> b.median()        ------- Median
>>> a.corrcoef()      ------- Correlation coefficient
>>> np.std(b)         ------- Standard deviation
        ''')

    # Control flow

    col3.subheader('Copy Arrays')
    col3.code('''
>>> h = a.view()    ------- Create a view of the array with the same data
>>> np.copy(a)      ------- Create a copy of the array
>>> h = a.copy()    ------- Create a deep copy of the array
    ''')

    # Lay out your app

    col3.subheader('Sorting Arrays')
    col3.code('''
>>> a.sort()       ------- Sort an array
>>> c.sort(axis=0) ------- Sort the elements of an array's axis
    ''')





    col3.subheader('Array Manipulation')
    col3.write('Transposing Array')
    col3.code('''
>>> i = np.transpose(b) ------- Permute array dimensions
>>> i.T                 ------- Permute array dimensions
        ''')

    col3.write('Changing Array Shape')
    col3.code('''
>>> b.ravel()       ------- Flatten the array
>>> g.reshape(3,-2) ------- Reshape but don't change the data 
            ''')

    col3.write('Adding/Removing Elements')
    col3.code('''
>>> h.resize((2,6))     ------- Return a new array with shape (2,6)
>>> np.append(h,g)      ------- Append items to an array
>>> np.insert(a, 1, 5)  ------- Insert items in an array
>>> np.delete(a,[1])    ------- Delete items from an array
    ''')

    # Optimize performance

    col3.write('Combining Array')
    col3.code('''
>>> np.concatenate((a,d),axis=0)  ------- Concatenate arrays
    array([ 1, 2, 3, 10, 15, 20])  
>>> np.vstack((a,b))              ------- Stack arrays vertically (row-wise)    
>>> np.r_[e,f]                    ------- Stack arrays vertically (row-wise)
>>> np.hstack((e,f))              ------- Stack arrays horizontally (column-wise)
    array([[ 7., 7., 1., 0.],
          [7., 7., 0., 1.,]])
>>> np.column_stack((a,d))        ------- Create stacked column-wise arrays
    array([[ 1, 10], 
           [ 2, 15],
           [ 3, 20]])
>>> np.c_[a,d]                    ------- Create stacked column-wise arrays
    ''')

    col3.write('Splitting Array')
    col3.code('''
>>> np.hsplit(a,3)                      ------- Split the array horizontally at the 3rd index
    [array([1]),array([2]),array([3])]
>>> np.vsplit(c,2)                      ------- Split the array vertically at the 2nd index
    [array([[[ 1.5, 2. , 1. ],
            [ 4. , 5. , 6. ]]]), 
    array([[[ 3., 2., 3.],
    [ 4., 5., 6.]]])]
    ''')

    return None

# Run main()

if __name__ == '__main__':
    main()