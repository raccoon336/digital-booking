import streamlit as st

#ตั้งค่าหน้าเว็ปไซต์
st.set_page_config(
    page_title = "ระบบจองตั๋วคอนเสิร์ต",
    page_icon = "🎟️"
)

#กำหนดราคาตั๋ว
prices = {
    "Standerd": 100,
    "VIP": 250,
    "Premium": 400
}

#แสดงหัวข้อเว็ปไซต์
st.title("🎟️ระบบจองตั๋วคอนเสิร์ต")
st.write("DIGITAL BOOKING")

st.divider()

#แสดงประเภทตั๋ว
st.subheader("ประเภทตั๋ว")
col1, col2, col3 = st.columns(3)
with col1:
  st.info("standard")
  st.write("100 บาท")
with col1:
  st.info("VIP")
  st.write("250 บาท")
with col1:
  st.info("Premium")
  st.write("400 บาท")
st.divider()

#แบบฟอร์มสั่งซื้อ
st.subheader("แบบฟอร์มสั่งซื้อ")
name = st.text_input("ชื่อผู้ซื้อ")
ticket = st.selectbox(
    "เลือกประเภทตั๋ว",
    ["Standerd","VIP","Premium"]
)

quantity = st.number_input(
    "จำหน่วนตั๋ว",
    min_value=1,
    max_value=10,
    value=1
)

#คำนวนราคา
price = prices[ticket]
total = price*quantity

st.write("ราคาตต่อตั๋ว:" ,price,"บาท")
st.write("จำนวน:" ,quantity,"ใบ")
st.sudheader(f"ยอดรวม{total:,}บาท")

st.divider()

#ยืนยันคำสั่งซื้อ
if st.button("ยืนยันการสั่งซื้อ"):
  if name == "":
    st.error("กรุณากรอกชื่อผู้ซื้อ")
  else:
    st.success("สั่งซื้อตั๋วเรียบร้อยแล้ว!")

    st.subheader("สรุปค่าสั่งซื้อ")
    st.write("ชื่อผู้ซื้อ:",name)
    st.write("ประเภทตั๋ว:",ticket)
    st.write("จำนวน:",quantity,"ใบ")
    st.write("ราคาต่อตั๋ว:",price,"บาท")

    st.success(f"ยอดชำระ{total:,} บาท")
st.caption("DIGITAL BOOKING")
