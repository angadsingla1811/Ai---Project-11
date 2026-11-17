
import cv2

# Upload an image
image_path = input("Enter the image path: ")
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
else:
    # Store the original image
    original = image.copy()

    # RGB intensity values
    red = 100
    green = 100
    blue = 100

    while True:

        # Split image into colour channels
        b, g, r = cv2.split(original)

        # Adjust colour intensity
        b = cv2.convertScaleAbs(b, alpha=blue / 100)
        g = cv2.convertScaleAbs(g, alpha=green / 100)
        r = cv2.convertScaleAbs(r, alpha=red / 100)

        # Combine colour channels
        filtered_image = cv2.merge((b, g, r))

        # Display the filtered image
        cv2.imshow("Real-Time Colour Filter", filtered_image)

        key = cv2.waitKey(1) & 0xFF

        # Increase red intensity
        if key == ord('r'):
            red = min(200, red + 10)

        # Decrease red intensity
        elif key == ord('t'):
            red = max(0, red - 10)

        # Increase green intensity
        elif key == ord('g'):
            green = min(200, green + 10)

        # Decrease green intensity
        elif key == ord('h'):
            green = max(0, green - 10)

        # Increase blue intensity
        elif key == ord('b'):
            blue = min(200, blue + 10)

        # Decrease blue intensity
        elif key == ord('n'):
            blue = max(0, blue - 10)

        # Save the filtered image
        elif key == ord('s'):
            filename = input("Enter filename (example: filtered.jpg): ")
            cv2.imwrite(filename, filtered_image)
            print("Image saved successfully!")

        # Reset all colours
        elif key == ord('0'):
            red = 100
            green = 100
            blue = 100

        # Exit
        elif key == 27:
            break

    cv2.destroyAllWindows()
