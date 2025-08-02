"""
ID: 10953117
Name: Osei Samuel Boakye
This Task loads an image and converts it to Grayscale
"""
import cv2
def convert_to_grayscale(input_path):
    # Load the image
    original_image = cv2.imread(input_path)
    
    if original_image is None:
        print("Error: Could not load the image. Please check the file path.")
        return
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    
    # Display both images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image', gray_image)
    
    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the grayscale image
    output_path = input_path.replace('.jpg', '_gray.jpg')
    cv2.imwrite(output_path, gray_image)
    print(f"Grayscale image saved as {output_path}")

# Example usage
if __name__ == "__main__":
    input_image_path = "photo.jpg"  # Change this to your image path
    convert_to_grayscale(input_image_path)
