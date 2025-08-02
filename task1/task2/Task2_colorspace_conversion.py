"""
ID: 10953117
Name: Osei Samuel Boakye
"""
import cv2
import matplotlib.pyplot as plt
import os

def main():
    # Load color image
    image_path = "photo.jpg"  # Change this to your image path
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return
    
    # Convert image to different color spaces
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # For display
    
    # Display each converted image
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    
    axes[0, 0].imshow(rgb)
    axes[0, 0].set_title('Original')
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(grayscale, cmap='gray')
    axes[0, 1].set_title('Grayscale')
    axes[0, 1].axis('off')
    
    axes[1, 0].imshow(hsv)
    axes[1, 0].set_title('HSV')
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(lab)
    axes[1, 1].set_title('LAB')
    axes[1, 1].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Save each converted image
    cv2.imwrite('photo_grayscale.jpg', grayscale)
    cv2.imwrite('photo_hsv.jpg', cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR))
    cv2.imwrite('photo_lab.jpg', cv2.cvtColor(lab, cv2.COLOR_LAB2BGR))
    
    # Plot histogram of grayscale image
    plt.figure(figsize=(8, 6))
    hist = cv2.calcHist([grayscale], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.title('Histogram of Grayscale Image')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.show()
    
    print("Images saved:")
    print("- photo_grayscale.jpg")
    print("- photo_hsv.jpg")
    print("- photo_lab.jpg")

if __name__ == "__main__":
    main()
