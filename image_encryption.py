# Taking path of image as input
path = r"C:\Users\nikhi\OneDrive\Desktop\chhatu\legend.jpg"

# Taking encryption key as input
key = int(input('Enter Key for encryption of image: '))

# Print path of image file and encryption key that we are using
print('The path of file:', path)
print('Key for encryption:', key)

# Open file for reading purpose
with open(path, 'rb') as fin:
    # Storing image data in variable "image"
    image = fin.read()

# Converting image into byte array to perform encryption easily on numeric data
image = bytearray(image)

# Perform XOR operation on each value of bytearray
for index, value in enumerate(image):
    image[index] = value ^ key

# Open file for writing purpose
with open(path, "wb") as fin:
    # Writing encrypted data in image
    fin.write(image)

print("Encryption done!!")
