function sendValue(value) {
  Streamlit.setComponentValue(value)
}

function sendValue_continue(pressed_key, value, suggestion) {
  
  const input = document.getElementById("input_box");
  if (pressed_key == 'ArrowRight') {
    input.value = input.value + suggestion.split(" ")[0] + " "
    document.getElementById("suggestion").innerText = suggestion.split(" ").slice(1,).join(" ")
  }
  Streamlit.setComponentValue(value)
}

function onRender(event) {
  // Only run the render code the first time the component is loaded.
  if (!window.rendered) {
    // Grab the label and default value that the user specified
    const {label, suggestion, value} = event.detail.args;

    const label_el = document.getElementById("label")
    label_el.innerText = label

    const input = document.getElementById("input_box");

    if (value && !input.value) {
      input.value = value
    }
    // input.value = event.target.value + suggestion
    if (suggestion) {
      const suggestion_ = document.getElementById("suggestion")
      suggestion_.innerText = suggestion
    }

    // On the keyup event, send the new value to Python
    // input.keydown = event => sendValue(event.target.value);
    // input.onkeyup = sendValue_continue(event, input.value);
    input.onkeyup = (e) => sendValue_continue(e.key, input.value, document.getElementById("suggestion").innerText);


    window.rendered = true
  }
}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, (e) => {
  if (document.getElementById("suggestion").innerText == "") {
    document.getElementById("suggestion").innerText = e.data.args.suggestion
  }
})
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
Streamlit.setFrameHeight(100)
