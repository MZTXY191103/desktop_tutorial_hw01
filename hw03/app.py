import streamlit as st
import numpy as np
from PIL import Image
from face_utils import detect_faces, draw_face_boxes, get_face_encodings

st.title("🧑‍💻 人脸识别 Demo")

uploaded_file = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"])
example_option = st.selectbox("或选择示例图", ["None", "Example 1"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
elif example_option != "None":   
    image = Image.open("tests/example.jpg")
    image_np = np.array(image)
else:
    st.info("请上传图片或选择示例图")
    st.stop()

st.subheader("原始图片")
st.image(image, use_column_width=True)

face_locations = detect_faces(image_np)
face_count = len(face_locations)
st.subheader(f"检测结果：共发现 {face_count} 张人脸")

if face_count > 0:
    image_with_boxes = draw_face_boxes(image_np.copy(), face_locations)
    st.image(image_with_boxes, use_column_width=True)

    face_encodings = get_face_encodings(image_np)
    st.write(f"提取到 {len(face_encodings)} 个人脸特征编码（128维）")
else:
    st.warning("未检测到人脸")