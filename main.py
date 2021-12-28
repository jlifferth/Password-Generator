import streamlit as st
import random


def generate_password(length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    print(len(chars))
    password = ''
    for i in range(length):
        index = random.randint(0, (len(chars) - 1))
        print(index)
        char = chars[index]
        password += char
    return password


# pass_length = int(input('password length : '))
# print(generate_password(12))


st.title('Random Password Generator')
number = st.number_input('Password length', min_value=1)
st.write('Password length : ' + str(number))

if st.button('Generate Password'):
    st.text(generate_password(int(number)))
else:
    st.text('Password will display here')
