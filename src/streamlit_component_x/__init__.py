from pathlib import Path
from typing import Any, Callable, Dict, Optional, Tuple

import streamlit as st
import streamlit.components.v1 as components
from utils import load_model, inference

# Tell streamlit that there is a component called streamlit_component_x,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_component_x", path=str(frontend_dir)
)

# Create the python function that will be called
def streamlit_component_x(
    label: str,
    suggestion: str,
    value: Optional[str] = "",
    key: Optional[str] = None,
    on_change: Optional[Callable] = None,
):

    if key is None:
        key = "streamlit_component_x_" + label

    component_value = _component_func(
        label=label,
        suggestion=suggestion,
        value=value,
        key=key,
    )

    if on_change is not None:
        if "__previous_values__" not in st.session_state:
            st.session_state["__previous_values__"] = {}
        if component_value != st.session_state["__previous_values__"].get(key, value):
            st.session_state["__previous_values__"][key] = component_value
            if on_change:
                on_change()

    return component_value

def run():
    if "cur_msg" in st.session_state and st.session_state.cur_msg is not None:
        # model = load_model()
        # result = inference(st.session_state.cur_msg, model)
        # st.session_state.suggestion = result
        st.session_state.suggestion = "1 2 3."

def main():
    if "suggestion" not in st.session_state:
        st.session_state.suggestion = ""
    st.title("Email Copilot")
    st.text_input("Current mail subject: ", key="cur_sub", on_change=run)
    value2 = streamlit_component_x(label="Current message: ", suggestion=st.session_state.suggestion, key="cur_msg", on_change=run)
    st.write(value2)
    # st.write(st.session_state.suggestion)
    

if __name__ == "__main__":
    main()
