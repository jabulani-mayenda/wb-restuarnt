import sys

filepath = r"c:\Users\lusun\Downloads\wb resturant\index.html"
try:
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

new_lines = []
for i, line in enumerate(lines):
    if i == 0 and line.startswith("<<<<<<< HEAD"):
        continue
    
    if line.startswith("======="):
        new_lines.append("</html>\n")
        break

    # Replace the chef image to use the founder image
    if 'alt="Chef"' in line and 'images.unsplash.com/photo-1583394293214' in line:
        line = '                        <img src="images/founder.jpg" alt="Chef & Founder" />\n'
    
    # Remove the onerror fallback from founder image
    if 'alt="Mr. Billy Nyasulu"' in line and 'onerror' in line:
        line = '                        <img src="images/founder.jpg" alt="Mr. Billy Nyasulu" />\n'
        
    new_lines.append(line)

try:
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("Successfully fixed index.html")
except Exception as e:
    print(f"Error writing file: {e}")
