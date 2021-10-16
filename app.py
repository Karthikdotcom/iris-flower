# import streamlit as st
# st.title("Hello World")

# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')


import streamlit as st
st.title("IRIS API")



# Webpage
sl = st.slider('Sepal Length', 4.3, 7.9, 5.9)
sw = st.slider('Sepal Width', 4.5, 3.5, 2.0)
pl = st.slider('Petal Length', 1.0, 6.9, 5.1)
pw = st.slider('Petal Width', 0.1, 2.5, 2.6)



# Model
from sklearn.datasets import load_iris
iris=load_iris()
# iris.keys()
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(iris.data,iris.target)
op=model.predict([[sl,sw,pl,pw]])
op=iris.target_names[op[0]]
st.title(f'The flower species is {op}')
