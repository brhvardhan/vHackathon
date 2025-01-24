import gradio as gr

def process_request(image,prompt):
    # ML CODE GOES HERE
    msg = "Your result will appear here ---- " + prompt
    return msg

demo = gr.Interface(
    fn=process_request,
    inputs=[gr.Image(label="Image"), gr.Text(label="Enter your Prompt")],
    outputs=[gr.Text(label="Output")],
)
demo.launch()
