import streamlit as st
import random


def generate_password(length, special):
    if special:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    else:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    # print(len(chars))
    password = ''
    for i in range(length):
        index = random.randint(0, (len(chars) - 1))
        # print(index)
        char = chars[index]
        password += char
    return password


# pass_length = int(input('password length : '))
# print(generate_password(12))


st.title('Random Password Generator')
number = st.number_input('Password length', min_value=1)
st.write('Password length : ' + str(number))

special_chars = True
if st.checkbox('Include Special characters'):
    special_chars = True
else:
    special_chars = False

if st.button('Generate Password'):
    st.text(generate_password(int(number), special=special_chars))
else:
    st.text('Password will display here')
