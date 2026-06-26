import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Family GPS Safe-Link", page_icon="🛡️", layout="wide")

st.title("🛡️ Family GPS Safe-Link Prototype")
st.caption("Secure location sharing via browser-level hardware GPS authorization.")

st.markdown("""
### 📲 How to use this link:
1. Send this app link to your family member.
2. When their phone asks for **Location Permissions**, they must click **'Allow'**.
3. Their real-time security anchor will render on the command grid below.
""")

st.markdown("---")

st.markdown("### 🛰️ SATELLITE HARDWARE HARVESTER")
location = streamlit_js_eval(data_of='getCurrentPosition', component_value=None, target_element=None)

if location:
    lat = location['coords']['latitude']
    lon = location['coords']['longitude']
    accuracy = location['coords']['accuracy']
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="📍 TARGET LATITUDE", value=f"{lat:.6f}")
    with col2:
        st.metric(label="📍 TARGET LONGITUDE", value=f"{lon:.6f}")
    with col3:
        st.metric(label="🎯 SIGNAL ACCURACY (METERS)", value=f"{accuracy:.1f}m")
        
    st.markdown("---")
    st.markdown("### 🗺️ LIVE SECURITY COMMAND MAP")
    
    m = folium.Map(location=[lat, lon], zoom_start=16, tiles="OpenStreetMap")
    folium.Marker(
        [lat, lon], 
        popup="🚨 Secured Family Member Location", 
        tooltip="Click for telemetry data",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)
    
    st_folium(m, width=1400, height=500, returned_objects=[])

else:
    st.warning("⏳ Waiting for hardware coordinates. Please click 'Allow Location Access' if prompted by your device.")