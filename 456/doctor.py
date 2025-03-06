import streamlit as st
from pathlib import Path
import google.generativeai as genai

from api_key import api_key

#confiq genai with api key
genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 0.4,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

system_prompt="""
As a highly skilled medical practitioner specializing in image analysis, you are tasked with medical images for a reowned hospitals. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the image.

Your Responsibilities include:

1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in the structured formats.
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests and treatment as applicable.
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.
5. Hospital list: Top 10 hospitals in banglore

Important Notes:

50

1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are unable to be determined basedon the provided image.
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions.
4. Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis adhering to the structured approach outlined above.

Please provide me output responses with these 4 headings
Detailed Analysis, Findings Report, Recommendations and Next Steps, Treatment Suggestions, Hospital list.

"""



#model config
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

# Set page config
st.set_page_config(page_title="DEEP-FAKE VIDEOS DETECTOR", page_icon=":robot:")

# Set logo
# st.image("logo.jpeg", width=200)  # Adjust width as needed

# Title
st.title("DEEP-FAKE VIDEOS DETECTOR")

#set subtitle
st.header("Make sure about the authenticity of your video!!")
uploaded_file=st.file_uploader("Drop your video",type=[ "jpg", "jpeg", "png"])


submit_btn=st.button("Generate analysis")

if submit_btn:
    #processing uploaded image
    image_data=uploaded_file.getvalue()
    #making image ready
    image_parts=[
        {
            "mime_type": "image/jpeg",
            "data": image_data
        },
    ]
    #making our own prompt
    prompt_parts=[
        
        image_parts[0],
        system_prompt,
    ]
    #generate a response based on prompt and image
    response = model.generate_content(prompt_parts)
    st.write(response.text)