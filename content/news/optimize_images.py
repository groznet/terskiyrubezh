import os
from PIL import Image

# -----------------------------------
# Settings
# -----------------------------------
MAX_WIDTH = 1600
QUALITY = 75
CONVERT_TO_WEBP = False   # True = convert every image to WebP

IMAGE_EXT = {'.jpg', '.jpeg', '.png', '.webp'}  # Allowed extensions


# -----------------------------------
# Helper: check if file is an image
# -----------------------------------
def is_image(path):
    ext = os.path.splitext(path)[1].lower()
    return ext in IMAGE_EXT


# -----------------------------------
# Compress one image
# -----------------------------------
def compress_image(path):
    try:
        print(f"→ Processing: {path}")

        img = Image.open(path)

        # Convert to RGB if PNG has transparency
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Resize if needed
        w, h = img.size
        if w > MAX_WIDTH:
            ratio = MAX_WIDTH / float(w)
            img = img.resize((MAX_WIDTH, int(h * ratio)), Image.LANCZOS)
            print(f"   Resized to: {img.size}")

        # Output path
        if CONVERT_TO_WEBP:
            new_path = os.path.splitext(path)[0] + ".webp"
            img.save(new_path, "WEBP", quality=QUALITY, method=6)
        else:
            img.save(path, optimize=True, quality=QUALITY)

        print(f"   ✔ Compressed\n")

    except Exception as e:
        print(f"   ✖ Error: {e}\n")


# -----------------------------------
# Walk folders
# -----------------------------------
def compress_recursive(folder):
    processed = 0

    for root, _, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)

            if not is_image(full_path):
                # Ignore all non-image files
                continue

            compress_image(full_path)
            processed += 1

    print(f"\nDone. Images processed: {processed}")


# -----------------------------------
# Run
# -----------------------------------
if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()
    compress_recursive(folder)
