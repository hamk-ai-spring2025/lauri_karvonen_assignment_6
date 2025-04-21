import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
from file_util import fetch_url, save_binary_file, find_new_file_name

# Load environment variables from .env file
load_dotenv()

def get_size_from_aspect(aspect):
    # Return a string "widthxheight" based on common aspect ratios.
    aspect_ratios = {
        "1:1": "1024x1024",
        "16:9": "1792x1024",
        "4:3": "1024x768",
        "3:4": "768x1024"
    }
    return aspect_ratios.get(aspect, "1792x1024")  # Default to 16:9

def main():
    print("Welcome to the Image Generator Utility!")
    print("This utility generates images using OpenAI's DALL-E 3 model.")
    print("Supported aspect ratios: 1:1, 16:9, 4:3, 3:4")
    print("Supported styles: natural, vivid")
    
    prompt_text = input("Enter image prompt: ").strip()
    if not prompt_text:
        print("Error: Prompt cannot be empty.")
        return
    
    aspect_ratio = input("Enter aspect ratio (default 16:9): ").strip()
    if aspect_ratio not in ["1:1", "16:9", "4:3", "3:4"]:
        print(f"Using default aspect ratio (16:9) instead of '{aspect_ratio}'")
        aspect_ratio = "16:9"
        
    seed_input = input("Enter seed (or leave blank for random): ").strip()
    seed = None
    if seed_input:
        try:
            seed = int(seed_input)
        except ValueError:
            print(f"Invalid seed value '{seed_input}'. Using random seed instead.")
    
    style = input("Enter image style (default 'natural'): [natural, vivid] ").strip() or "natural"
    if style not in ["natural", "vivid"]:
        print(f"Invalid style '{style}'. Using 'natural' instead.")
        style = "natural"
    
    num_images = 1  # Fixed at 1 image

    # Determine the size parameter based on aspect ratio
    size = get_size_from_aspect(aspect_ratio)

    # Prepare additional parameters
    extra_params = {}
    if seed is not None:
        extra_params["seed"] = seed

    # Pull the API key from the .env file
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in the .env file.")
        return

    client = OpenAI(api_key=api_key)

    try:
        print("Generating image... this may take a moment.")
        # Build the generation payload
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt_text,
            size=size,
            quality="hd",
            style=style,
            n=num_images,
            **extra_params
        )

        for index, data_item in enumerate(response.data):
            image_url = data_item.url
            print(f"Image {index+1} URL: {image_url}")

            print(f"Downloading image {index+1}...")
            # Download the image
            image_data = fetch_url(image_url)
            if image_data is not None:
                file_name = find_new_file_name(f"generated_{index+1}.png")
                if save_binary_file(data=image_data, filename=file_name):
                    print(f"Image successfully saved to {file_name}")
                else:
                    print(f"Failed to save image {index+1}.")
            else:
                print(f"Failed to download image {index+1}.")
    
    except Exception as e:
        print(f"Error generating or downloading image: {str(e)}")

if __name__ == "__main__":
    main()