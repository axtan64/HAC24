import easyocr
import cv2

def extract_text_from_image(image_path):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Read text from the image
    result = reader.readtext(image_path)

    # Extract and return the text
    extracted_text = ';'.join([entry[1] for entry in result])

    # Remove text from the image
    image = cv2.imread(image_path)
    for detection in result:
        # Get the bounding box coordinates of the detected text
        bbox = detection[0]

        # Extract coordinates
        x_min, y_min = map(int, [bbox[0][0], bbox[0][1]])
        x_max, y_max = map(int, [bbox[2][0], bbox[2][1]])


    # Save the image with text removed
    output_image_path = "if_test4.png"
    cv2.imwrite(output_image_path, image)

    return extracted_text, output_image_path

# Example usage:
input_image_path = "if_test4.png"
extracted_text, output_image_path = extract_text_from_image(input_image_path)
print("Extracted Text:", extracted_text)
print("Output Image with Text Removed:", output_image_path)
