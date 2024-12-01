---
title: My Blog
date: 2024-12-01
draft: false
tags:
  - david
  - blog
---

# This is just the beginning 

- I'm going to upload a lot of info about my ideas and stuff that I think is important here from now on 

## I've been using Discord for note taking thus far :P

- I know its stupid but the only way for me to really ***Sync*** my thoughts across multiple devices
- Now I'm going to be using ***Obsidian*** and use a pipeline with Hugo 

# Going forward

- Now is the time for me to become more organized. 
- I'll start by cleaning my room after this pipeline is completed and I can seamlessly blog from Obsidian to my _blog_


![[Pasted image 20241201155218.png]]

```python
import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\Users\dealv\Documents\davidblog\content\posts"
attachments_dir = r"C:\Users\dealv\Documents\David\Attachments"
static_images_dir = r"C:\Users\dealv\Documents\davidblog\static\images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"![Image Description](/images/{image.replace('%20',%20'%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")

```

### Hello I am now updating remotely !!!