import os
from flask import Flask, render_template, request

app = Flask(__name__)

def get_color(text):
    colors = {
        "red": "#FF0000", "blue": "#0000FF", "green": "#00FF00",
        "yellow": "#FFFF00", "purple": "#9D00FF", "orange": "#FFA500",
        "black": "#111", "white": "#FFF", "gold": "#FFD700", "silver": "#C0C0C0"
    }
    for name, hex_code in colors.items():
        if name in text.lower(): return hex_code
    return "#FF0000" # Default

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_scene = ""
    prompt = ""
    
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        obj_color = get_color(prompt)
        
        objects_html = ""
        sky_color = "#87CEEB"
        
        if "night" in prompt.lower(): sky_color = "#050505"
        
        # LOGIC: CAR
        if "car" in prompt.lower():
            objects_html += '<a-plane rotation="-90 0 0" width="100" height="100" color="#333"></a-plane>'
            objects_html += f'<a-box position="0 1 -5" width="2" height="1" depth="4" color="{obj_color}"></a-box>'
            objects_html += '<a-cylinder position="-1 0.5 -3" rotation="0 0 90" radius="0.5" height="0.5" color="#000"></a-cylinder>'
            objects_html += '<a-cylinder position="1 0.5 -3" rotation="0 0 90" radius="0.5" height="0.5" color="#000"></a-cylinder>'
            
        # LOGIC: CITY
        elif "city" in prompt.lower():
            objects_html += '<a-plane rotation="-90 0 0" width="100" height="100" color="#222"></a-plane>'
            objects_html += f'<a-box position="-5 5 -10" height="10" width="4" color="{obj_color}"></a-box>'
            objects_html += f'<a-box position="5 7 -10" height="14" width="4" color="{obj_color}"></a-box>'
            
        # LOGIC: DEFAULT
        else:
             objects_html += f'<a-sphere position="0 2 -5" radius="2" color="{obj_color}"></a-sphere>'

        generated_scene = f"""
        <a-sky color="{sky_color}"></a-sky>
        <a-entity>{objects_html}</a-entity>
        """

    return render_template('index.html', generated_scene=generated_scene, prompt=prompt)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
