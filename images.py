import os
import re
import shutil

# Paths
posts_dir = r"C:\Users\dealv\Documents\davidblog\content\posts"
attachments_dir = r"C:\Users\dealv\Documents\David\images"
static_images_dir = r"C:\Users\dealv\Documents\davidblog\static\images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        print(f"Processing Markdown file: {filepath}")
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Step 2: Find all image links using regex
        images = re.findall(r'!\[.*?\]\((.*?)\)', content)
        
        for image in images:
            # Extract the image filename from the link
            image_filename = os.path.basename(image).replace('%20', ' ').strip()
            print(f"Image found in Markdown: {image_filename}")

            # Replace spaces with %20 for the URL (not the file path)
            markdown_image = f"/images/{image_filename.replace(' ', '%20')}"
            content = content.replace(image, markdown_image)

            # Step 4: Copy the image to the Hugo static/images directory
            image_source = os.path.join(attachments_dir, image_filename)
            image_dest = os.path.join(static_images_dir, image_filename)

            print(f"Looking for: {image_source}")
            if os.path.exists(image_source):
                shutil.copy(image_source, image_dest)
                print(f"Copied: {image_filename}")
            else:
                print(f"Image not found: {image_filename}")
                print(f"Attachments directory contains: {os.listdir(attachments_dir)}")

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
