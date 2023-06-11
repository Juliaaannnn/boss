import streamlit as st
import openai
import os

openai.api_key = st.secrets["api_key"]

def correct_grammar(input_string):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Correct this to standard English: " + input_string + "\n",
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        temperature=0.0,
        stop="\n\n",
    )
    answer = response.choices[0].text.strip()
    return answer

def main():
    st.title("Grammar Correction")

    input_string = st.text_input("Enter a sentence:")
    if input_string:
        output = correct_grammar(input_string)
        st.text(f"Input: {input_string}")
        st.text(f"Output: {output}")

if __name__ == "__main__":
    main()
